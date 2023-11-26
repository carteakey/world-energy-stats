from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    # Optional: 'retries': 1,
    # Optional: 'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    "run_hive_sql",
    default_args=default_args,
    schedule_interval=None,  # or as needed
    tags=["world-energy-data"],
    catchup=False
)

sql_files = {
    "/opt/sql/combined_energy_data.sql": None,
    "/opt/sql/1_energy_overview.sql": "1_energy_overview.csv",
    "/opt/sql/2_energy_consumption_pct_rem.sql": "2_energy_consumption_pct_rem.csv",
    "/opt/sql/2_energy_consumption_pct_top15.sql": "2_energy_consumption_pct_top15.csv",
    "/opt/sql/2_energy_consumption_top15.sql": "2_energy_consumption_top15.csv",
    "/opt/sql/3_energy_breakdown_top15.sql": "3_energy_breakdown_top15.csv",
    "/opt/sql/4_electricity_gen_top15.sql": "4_electricity_gen_top15.csv",
    "/opt/sql/4_electricity_share_top15.sql": "4_electricity_share_top15.csv",
    "/opt/sql/5_population_correlation.sql": "5_population_correlation.csv",
    "/opt/sql/energy_share.sql": "energy_share.csv"
}

tasks = []  # List to store tasks

for sql_file, output_file in sql_files.items():
    task_id = f"run_{sql_file.split('/')[-1].split('.')[0]}"  # e.g., run_1_energy_overview
    save_file_cmd = f"--save_file {output_file}" if output_file else ""
    bash_command = f"docker exec spark-master /spark/bin/spark-submit --master spark://spark-master:7077 /opt/scripts/pyspark/run_hive_query.py {sql_file} {save_file_cmd}"

    task = BashOperator(
        task_id=task_id,
        bash_command=bash_command,
        dag=dag,
    )

    tasks.append(task)

for i in range(1, len(tasks)):
    tasks[i - 1] >> tasks[i]