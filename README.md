# world-energy-stats

AIRFLOW
HADOOP HDFS
SPARK
DOCKER
MAP REDUCE
PLOTLY
JUPYTER
HIVE

Airflow
1 - copies file from local to hdfs - Hadoop FS
2 - run spark transformation jobs - SPARK / SPARK SQL
3 - create intermediate views/tables - HIVE SQL
4 - runs sql queries and saves to hadoop fs - HIVE SQL
5 - copies the final clean data from hadoop fs for plotting - HIVE SQL
6 - creates plots and runs the dashboard - XX


`docker compose up -d` - Spin up the containers.

### Links

| App     | Server             | Link                          |
| ------- | ------------------ | ----------------------------- |
| Hadoop  | ResourceManager UI | http://localhost:8088/cluster |
| Hadoop  | Namenode UI        | http://localhost:9870/        |
| Jupyter | Notebook UI        | http://localhost:8888/        |
| Spark   | Master             | http://localhost:8080/        |
| Airflow |                    |                               |



### Tasks

- [x] Forward fill missing data
- [x] combine airflow
- [ ] airflow dags
- [x] remove presto
- [x] mount hadoop
- [x] mount notebooks

### References

https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-all-spark-notebook
https://hub.docker.com/r/apache/hadoop
https://stackoverflow.com/questions/38088279/communication-between-multiple-docker-compose-projects

Hannah Ritchie, Max Roser and Pablo Rosado (2022) - "Energy". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/energy' [Online Resource]
https://ourworldindata.org/energy#citation

docker rmi $(docker images -a -q)

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'

docker compose up airflow-init


.
├── README.md
├── _archive
│   ├── DS8003 Final Project Ideas.pdf
│   ├── airflow
│   │   └── docker-compose.yml
│   ├── app
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   └── templates
│   ├── app.py
│   ├── app_v0.py
│   ├── app_v1.py
│   ├── app_v2.py
│   ├── app_v3.py
│   ├── duckdb-load.py
│   ├── energy-clean-data.db
│   ├── highcharts
│   │   ├── highcharts-viz.ipynb
│   │   └── map_data.ipynb
│   ├── hive_queries_renewables.ipynb
│   ├── index.html
│   ├── old
│   │   ├── app_old.py
│   │   ├── insight_1_old.py
│   │   ├── insight_2.py
│   │   ├── insight_3.py
│   │   └── insight_3_5.py
│   ├── routes.py
│   ├── spark_etl_regions.ipynb
│   └── streamlit-app.py
├── airflow
│   ├── config
│   ├── dags
│   │   └── run_data_transformation.py
│   ├── logs
│   │   ├── dag_id=data_transformation
│   │   ├── dag_processor_manager
│   │   └── scheduler
│   └── plugins
├── dash-app
│   ├── assets
│   │   ├── big-players.png
│   │   ├── data
│   │   ├── electricity-mix.png
│   │   ├── energy-consumption.png
│   │   ├── energy-gdp-pop.png
│   │   ├── energy-mix.png
│   │   ├── old
│   │   ├── old_v2
│   │   └── styles.css
│   └── components
│       ├── insight_1.py
│       ├── insight_2.py
│       ├── insight_3.py
│       ├── insight_4.py
│       ├── insight_4a.py
│       ├── insight_4b.py
│       └── insight_5.py
├── docker-compose.env
├── docker-compose.yml
├── energy-data
│   ├── README.md
│   ├── owid-energy-codebook.csv
│   └── owid-energy-data.csv
├── notebooks
│   ├── clean
│   │   ├── biofuel.csv
│   │   ├── coal.csv
│   │   ├── electricity_imports.csv
│   │   ├── fossil.csv
│   │   ├── gas.csv
│   │   ├── general.csv
│   │   ├── greenhouse_gas.csv
│   │   ├── hydro.csv
│   │   ├── low_carbon.csv
│   │   ├── nuclear.csv
│   │   ├── oil.csv
│   │   ├── other_renewables.csv
│   │   ├── renewables.csv
│   │   ├── solar.csv
│   │   ├── wind.csv
│   │   └── world.csv
│   ├── eda.ipynb
│   ├── hive_queries_ak-1.ipynb
│   ├── hive_queries_ak.ipynb
│   ├── hive_queries_kc.ipynb
│   ├── output
│   │   ├── 1_energy_overview.csv
│   │   ├── 2_energy_consumption_pct_rem.sql.csv
│   │   ├── 2_energy_consumption_pct_top15.csv
│   │   ├── 2_energy_consumption_top15.csv
│   │   ├── 3_energy_breakdown_top15.csv
│   │   ├── 4_electricity_gen_top15.csv
│   │   ├── 4_electricity_share_top15.csv
│   │   └── 5_population_correlation.csv
│   ├── spark_etl_countries.ipynb
│   ├── spark_etl_world.ipynb
│   ├── spark_hive_test.ipynb
│   └── utils.py
├── requirements.txt
├── scripts
│   ├── hadoop
│   │   ├── eda_pandas_mapper.py
│   │   ├── eda_pandas_reducer.py
│   │   ├── null_percent_mapper.py
│   │   └── null_percent_reducer.py
│   └── pyspark
│       ├── data_categorization.py
│       ├── data_transformation.py
│       └── utils.py
├── setup.sh
└── sql
    ├── 1_energy_overview.sql
    ├── 2_energy_consumption_pct_rem.sql
    ├── 2_energy_consumption_pct_top15.sql
    ├── 2_energy_consumption_top15.sql
    ├── 3_energy_breakdown_top15.sql
    ├── 4_electricity_gen_top15.sql
    ├── 4_electricity_share_top15.sql
    ├── 5_population_correlation.sql
    ├── combined_energy_data.sql
    └── energy_share.sql

30 directories, 94 files