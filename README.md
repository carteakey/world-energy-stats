# world-energy-stats

`docker compose up -d` - Spin up the containers.

### Links

| App     | Server             | Link                          |
| ------- | ------------------ | ----------------------------- |
| Hadoop  | Namenode UI        | http://localhost:9870/        |
| Hadoop  | ResourceManager UI | http://localhost:8088/cluster |
| Jupyter | Notebook UI        | http://localhost:8888/        |
| Spark   | Master             | http://localhost:8080/        |
<<<<<<< HEAD
| Spark   | Master             | http://localhost:8080/        |
| Spark   | Master             | http://localhost:8080/        |


Airflow
1 - copies file from local to hdfs - Hadoop FS
2 - run spark transformation jobs - SPARK / SPARK SQL
3 - create intermediate views/tables - HIVE SQL
4 - runs sql queries and saves to hadoop fs - HIVE SQL
5 - copies the final clean data from hadoop fs for plotting - HIVE SQL
6 - creates plots and runs the dashboard - XX 
=======
>>>>>>> 63e8d118139e32bbf7366b02f6147c200153f82f


### Tasks

- [x] Forward fill missing data
- [ ] combine airflow
- [x] remove presto
- [x] mount hadoop
- [x] mount notebooks

### COMMANDS

nohup FLASK_APP=app && flask run --host=0.0.0.0  --debug 1>flask-server.log &








### References


https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-all-spark-notebook
https://hub.docker.com/r/apache/hadoop
https://stackoverflow.com/questions/38088279/communication-between-multiple-docker-compose-projects


Hannah Ritchie, Max Roser and Pablo Rosado (2022) - "Energy". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/energy' [Online Resource]
https://ourworldindata.org/energy#citation


docker rmi $(docker images -a -q)

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'

docker compose up airflow-init
