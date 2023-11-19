from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
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
    "data_transformation",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

t1 = DockerOperator(
    task_id="run_data_transformation",
    image="bde2020/spark-master:3.3.0-hadoop3.3",
    api_version="auto",
    docker_url='unix:///var/run/docker.sock',
    # auto_remove=True,
    command="/spark/bin/spark-submit --master spark://spark-master:7077 /opt/scripts/pyspark/data_transformation.py",
    network_mode="bridge",
    dag=dag,
)
