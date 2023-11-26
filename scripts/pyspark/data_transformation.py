from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import last, first
import pyspark.sql.functions as F

# Spark session & context
spark = (
    SparkSession.builder.appName("world-energy-stats")
    .master("spark://spark-master:7077")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)

# Read the dataset from HDFS
df = (
    spark.read.format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("hdfs://namenode:9000/energy-data/owid-energy-data.csv")
)


df = df.filter(df["iso_code"].isNotNull())

df = df[df["year"] >= 1990]


# Dropping irrelevant columns
cols_to_drop = [
    col
    for col in df.columns
    if "_per_gdp"
    if "_per_capita" in col or "_change_pct" in col or "_change_twh" in col
]
df = df.drop(*cols_to_drop)

# Forward fill missing data
temp_column = [column for column in df.columns if "year" not in column]
temp_column = [column for column in temp_column if "country" not in column]
temp_column

# Define the windows for forward fill and backward fill
ffill_window = "(partition by country order by year rows between unbounded preceding and current row)"
# bfill_window = "(partition by country order by year rows between current row and unbounded following)"

for col in temp_column:
    df = df.withColumn(
        col, F.expr(f"case when isnan({col}) then null else {col} end")
    ).withColumn(col, F.expr(f"coalesce({col}, last({col}, true) over {ffill_window})"))
    # .withColumn(col, F.expr(f"coalesce({col}, first({col}, true) over {bfill_window})")))


# Write the DataFrame to a Hive table
df.write.saveAsTable("wes.transformed_energy_data")

# Stop the SparkSession
spark.stop()
