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
    "hdfs_data_upload",
    default_args=default_args,
    schedule_interval=None,    #"timedelta(days=1)",
    tags=["world-energy-data"],
    catchup=False  # Prevents backfilling
)

# Task 1: Create directory in HDFS
create_directory = BashOperator(
    task_id="create_hdfs_directory",
    bash_command="docker exec resourcemanager /bin/bash -c 'hadoop fs -mkdir -p /energy-data/output'",
    dag=dag,
)

# Task 1: Create directory in HDFS
clear_files = BashOperator(
    task_id="clear_files",
    bash_command="docker exec resourcemanager /bin/bash -c 'hadoop fs -rm -f -R /energy-data/owid-energy-data.csv'",
    dag=dag,
)

# Task 1: Create directory in HDFS
clear_scripts = BashOperator(
    task_id="clear_scripts",
    bash_command="docker exec resourcemanager /bin/bash -c 'hadoop fs -rm -f -R /energy-data/*.py'",
    dag=dag,
)

# Task 2: Change directory and upload file
upload_file = BashOperator(
    task_id="upload_file_to_hdfs",
    bash_command="docker exec resourcemanager /bin/bash -c 'cd /opt/energy-data && hadoop fs -put owid-energy-data.csv /energy-data/'",
    dag=dag,
)

#
upload_scripts = BashOperator(
    task_id="upload_scripts_to_hdfs",
    bash_command="docker exec resourcemanager /bin/bash -c 'cd /opt/scripts/hadoop && hadoop fs -put *.py /energy-data/'",
    dag=dag,
)

# Task 3: List contents of the directory
list_directory = BashOperator(
    task_id="list_hdfs_directory",
    bash_command="docker exec resourcemanager /bin/bash -c 'hadoop fs -ls /energy-data/'",
    dag=dag,
)

# Setting up dependencies
create_directory >> clear_files >> clear_scripts >> upload_file >>  upload_scripts >> list_directory
