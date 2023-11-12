`docker compose up -d` - Spin up the containers.

### Links

| App     | Server             | Link                          |
| ------- | ------------------ | ----------------------------- |
| Hadoop  | Namenode UI        | http://localhost:9870/        |
| Hadoop  | ResourceManager UI | http://localhost:8088/cluster |
| Jupyter | Notebook UI        | http://localhost:8888/        |
| Spark   | Master             | http://localhost:8080/        |

### Tasks

- [ ] combine airflow
- [x] remove presto
- [x] mount hadoop
- [x] mount notebooks

### COMMANDS
sudo chmod 777 notebooks
sudo chmod 777 data

docker exec -it hive-server hive
docker exec -it resourcemanager /bin/bash


hadoop fs -mkdir /energy-data
cd /opt/data
hadoop fs -put owid-energy-data.csv /energy-data/
hadoop fs -ls /energy-data/
docker exec  spark-notebook jupyter server list



### REFERENCE
https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-all-spark-notebook
https://hub.docker.com/r/apache/hadoop
https://stackoverflow.com/questions/38088279/communication-between-multiple-docker-compose-projects



