from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),  # Adjust this date as needed
    "email_on_failure": False,
    "email_on_retry": False,
    # Optional: 'retries': 1,
    # Optional: 'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    "hive_create_database",
    default_args=default_args,
    schedule_interval=None,  # Run this DAG once or as needed
    tags=["world-energy-data"],
    catchup=False,
)

create_database = BashOperator(
    task_id="create_hive_database",
    bash_command="docker exec hive-server hive -e 'CREATE DATABASE wes'",
    dag=dag,
)
