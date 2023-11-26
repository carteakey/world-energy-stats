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
    "run_mapreduce_jobs",
    default_args=default_args,
    schedule_interval=None,  # or as needed
    tags=["world-energy-data"],
    catchup=False,
)

# Replace these paths with your actual paths
mapper_script_path = "hdfs://namenode:9000/energy-data/eda_pandas_mapper.py"
mapper = "eda_pandas_mapper.py"
reducer_script_path = "hdfs://namenode:9000/energy-data/eda_pandas_reducer.py"
reducer = "eda_pandas_reducer.py"
input_path = "/energy-data/owid-energy-data.csv"
output_path = "/energy-data/output/eda_output"

clear_output_folder_eda = BashOperator(
    task_id="clear_output_folder_eda",
    bash_command=("docker exec resourcemanager hadoop fs -rm -f -R {output}").format(
        output=output_path
    ),
    dag=dag,
)

eda_job = BashOperator(
    task_id="run_mapreduce_job_eda",
    bash_command=(
        "docker exec resourcemanager "
        "hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar "
        "-files {mapper_path},{reducer_path} "
        "-mapper {mapper} "
        "-reducer {reducer} "
        "-input {input} "
        "-output {output}"
        " -verbose "
    ).format(
        mapper_path=mapper_script_path,
        reducer_path=reducer_script_path,
        mapper=mapper,
        reducer=reducer,
        input=input_path,
        output=output_path,
    ),
    dag=dag,
)


# Replace these paths with your actual paths
mapper_script_path = "hdfs://namenode:9000/energy-data/null_percent_mapper.py"
mapper = "null_percent_mapper.py"
reducer_script_path = "hdfs://namenode:9000/energy-data/null_percent_reducer.py"
reducer = "null_percent_reducer.py"
input_path = "/energy-data/owid-energy-data.csv"
output_path = "/energy-data/output/null_percent"


clear_output_folder_np = BashOperator(
    task_id="clear_output_folder_np",
    bash_command=("docker exec resourcemanager hadoop fs -rm -f -R {output}").format(
        output=output_path
    ),
    dag=dag,
)

np_job = BashOperator(
    task_id="run_mapreduce_job_np",
    bash_command=(
        "docker exec resourcemanager "
        "hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar "
        "-files {mapper_path},{reducer_path} "
        "-mapper {mapper} "
        "-reducer {reducer} "
        "-input {input} "
        "-output {output}"
        " -verbose "
    ).format(
        mapper_path=mapper_script_path,
        reducer_path=reducer_script_path,
        mapper=mapper,
        reducer=reducer,
        input=input_path,
        output=output_path,
    ),
    dag=dag,
)

clear_output_folder_np >> np_job >> clear_output_folder_eda >> eda_job 
