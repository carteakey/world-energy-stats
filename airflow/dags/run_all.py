from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

# Define the default arguments for the main DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),  # Adjust this date as needed
    "email_on_failure": False,
    "email_on_retry": False,
    # Optional: 'retries': 1,
    # Optional: 'retry_delay': timedelta(minutes=5),
}
# Create the main DAG
main_dag = DAG(
    "run_all",
    default_args=default_args,
    schedule_interval=None,
    tags=["world-energy-data"],
    catchup=False,
)

trigger_create_db = TriggerDagRunOperator(
    task_id="trigger_hive_create_database",
    trigger_dag_id="hive_create_database",
    dag=main_dag,
)


trigger_hdfs_upload = TriggerDagRunOperator(
    task_id="trigger_hdfs_data_upload",
    trigger_dag_id="hdfs_data_upload",
    dag=main_dag,
)


trigger_mapreduce = TriggerDagRunOperator(
    task_id="trigger_run_mapreduce_jobs",
    trigger_dag_id="run_mapreduce_jobs",
    dag=main_dag,
)


trigger_transform_1 = TriggerDagRunOperator(
    task_id="run_data_transformation",
    trigger_dag_id="data_transformation",
    dag=main_dag,
)

trigger_transform_2 = TriggerDagRunOperator(
    task_id="run_data_categorization",
    trigger_dag_id="data_categorization",
    dag=main_dag,
)

trigger_sql = TriggerDagRunOperator(
    task_id="trigger_run_hive_sql",
    trigger_dag_id="run_hive_sql",
    dag=main_dag,
)


trigger_hdfs_download = TriggerDagRunOperator(
    task_id="trigger_hdfs_data_download",
    trigger_dag_id="hdfs_data_download",
    dag=main_dag,
)

trigger_create_db >> trigger_hdfs_upload
trigger_hdfs_upload >> trigger_mapreduce
trigger_mapreduce >> trigger_transform_1
trigger_transform_1 >> trigger_transform_2
trigger_transform_2 >> trigger_sql
trigger_sql >> trigger_hdfs_download

