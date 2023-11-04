`docker compose up -d` - Spin up the containers.

### Links
|App | Server | Link |
|----|--------|------|
|Hadoop|Namenode UI| http://localhost:9870/ |
|Hadoop|ResourceManager UI | http://localhost:8088/cluster|
|Jupyter|Notebook UI| http://localhost:8888/|
|Spark|Master|http://localhost:8080/|


### Tasks
- [ ] remove presto
- [ ] combine airflow
- [x] mount hadoop
- [x] mount notebooks



### COMMANDS

Open bash shell
```
docker exec -it hadoop-namenode-1 /bin/bash
```

Copy file
```
docker cp /home/kchauhan/repos/world-energy-stats/energy-data/owid-energy-data.csv  hadoop-namenode-1:/home/  
```

### DOCKER

command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

sudo chmod 777 notebooks
sudo chmod 777 data


### REFERENCE
https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-all-spark-notebook

https://hub.docker.com/r/apache/hadoop

https://stackoverflow.com/questions/38088279/communication-between-multiple-docker-compose-projects

### HADOOP

docker exec -it namenode /bin/bash

hadoop fs -mkdir /energy-data

```
hadoop fs -put owid-energy-data.csv /energy-data/
```

```
hadoop fs -ls /energy-data/
```


### NOTEBOOK
Get token
```
docker exec  spark-notebook jupyter server list

Currently running servers:
http://4b8201f80db0:8888/?token=bf8bc07b31ad9c413455ed7376cb3c2f3c31a15863a6f64c :: /home/jovyan

```


