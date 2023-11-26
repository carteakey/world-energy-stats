# world-energy-stats

https://world-energy-stats-34l3s.ondigitalocean.app/

## Overview

Airflow
1 - copies file from local to hdfs - Hadoop FS
2 - run spark transformation jobs - SPARK / SPARK SQL
3 - create intermediate views/tables - HIVE SQL
4 - runs sql queries and saves to hadoop fs - HIVE SQL
5 - copies the final clean data from hadoop fs for plotting - HIVE SQL
6 - creates plots and runs the dashboard - XX

## Reference
This project uses the awesome data from OWID.

Hannah Ritchie, Max Roser and Pablo Rosado (2022) - "Energy". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/energy' [Online Resource]
https://ourworldindata.org/energy#citation


## Running Locally

```bash
docker compose up airflow-init
```

| App     | Server             | Link                          |
| ------- | ------------------ | ----------------------------- |
| Hadoop  | ResourceManager UI | http://localhost:8088/cluster |
| Hadoop  | Namenode UI        | http://localhost:9870/        |
| Jupyter | Notebook UI        | http://localhost:8888/        |
| Spark   | Master             | http://localhost:8080/        |
| Airflow |                    |                               |


## Project Structure
```~/world-energy-stats# tree --gitignore -L 3
.
├── README.md
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
│   │   └── styles.css
│   └── components
│       ├── insight_1.py
│       ├── insight_2.py
│       ├── insight_3.py
│       ├── insight_4.py
│       └── insight_5.py
├── docker-compose.env
├── docker-compose.yml
├── energy-data
│   ├── README.md
│   ├── owid-energy-codebook.csv
│   └── owid-energy-data.csv
├── notebooks
│   ├── clean
│   ├── eda.ipynb
│   ├── hive_queries_ak-1.ipynb
│   ├── hive_queries_ak.ipynb
│   ├── hive_queries_kc.ipynb
│   ├── output
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

21 directories, 45 files
```

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->