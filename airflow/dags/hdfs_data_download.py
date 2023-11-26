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
    "hdfs_data_download",
    default_args=default_args,
    schedule_interval=None,  # "timedelta(days=1)",
    tags=["world-energy-data"],
    catchup=False,  # Prevents backfilling
)

clear_data_task = BashOperator(
    task_id="clear_data",
    bash_command="docker exec resourcemanager rm -rf /opt/data/output",
    dag=dag,
)


copy_data_task = BashOperator(
    task_id="copy_data_from_hdfs",
    bash_command="docker exec resourcemanager hadoop fs -get /energy-data/output/ /opt/data",
    dag=dag,
)

rename_task = BashOperator(
    task_id='rename_csv_file',
     bash_command=(
        "docker exec resourcemanager /bin/bash -c "
        "'for d in /opt/data/output/*/; do "
        "dir_name=$(basename \"$d\" .csv); "  # Removes the .csv extension from the directory name
        "mv \"$d\"*.csv \"/opt/data/${dir_name}.csv\"; "  # Moves and renames the CSV file
        "rm -rf \"$d\"; "  # Removes the empty directory
        "done'"
    ),
    dag=dag,
)

clear_data_task >> copy_data_task >> rename_task