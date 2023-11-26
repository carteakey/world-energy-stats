from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    "data_categorization",
    default_args=default_args,
    schedule_interval=None,     #"timedelta(days=1)",
    tags=["world-energy-data"],
    catchup=False,  # Prevents backfilling
)

t1 = BashOperator(
    task_id="run_data_categorization",
    bash_command="docker exec spark-master /spark/bin/spark-submit --master spark://spark-master:7077 /opt/scripts/pyspark/data_categorization.py",
    dag=dag,
)
