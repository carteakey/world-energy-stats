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
    "hadoop_setup_python",
    default_args=default_args,
    schedule_interval=None,  # Run this DAG once or as needed
    tags=["world-energy-data"],
    catchup=False,
)

tasks = []
docker_containers = ["resourcemanager", "datanode", "namenode","nodemanager"]
script_path = "/opt/scripts/install_python.sh"

for container in docker_containers:
    task_id = f"install_python_pip_pandas_{container}"
    task = BashOperator(
        task_id=task_id,
        bash_command=f"docker exec {container} /bin/bash {script_path} ",
        dag=dag,
    )
    tasks.append(task)
