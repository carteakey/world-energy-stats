from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def run_spark_sql(sql_file_path, save_file=None):
    """
    Executes a SQL query from a file in Spark SQL.

    Parameters:
    sql_file_path (str): Path to the SQL query file.
    save_file (str, optional): Path to save the output. If None, the output is not saved.
    """

    # Start Spark Session
    spark = (
        SparkSession.builder.appName("hive-queries")
        .master("spark://spark-master:7077")
        .config("hive.metastore.uris", "thrift://hive-metastore:9083")
        .enableHiveSupport()
        .getOrCreate()
    )

    # Use WES
    spark.sql("USE wes")

    # Read SQL query from the file
    with open(sql_file_path, "r") as file:
        sql_query = file.read()

    # Execute the SQL query
    result = spark.sql(sql_query)

    # Save the result to a file if a save path is provided
    if save_file:
        result.coalesce(1).write.option("mode", "append").option("header", "true").csv(
            "hdfs://namenode:9000/energy-data/output/" + save_file
        )

    # Show the first 20 rows
    result.show()

    # Stop the Spark Session
    spark.stop()


def filter_df_by_threshold(df, threshold):
    """
    Filter a dataframe based on the threshold of non-null counts in non-primary columns.

    Parameters:
    - df: The input dataframe.
    - threshold: The minimum number of non-null values required across non-primary columns.

    Returns:
    - filtered_df: The filtered dataframe.
    - stats: A dictionary containing statistics about the filtering process.
    """

    # Primary Key Columns
    primary_keys = ["country", "year", "iso_code"]

    # List of columns to check for null values
    columns_to_check = [col for col in df.columns if col not in primary_keys]

    # Count non-null values across all non-primary columns for each country
    agg_exprs = [
        F.count(F.when(F.col(c).isNotNull(), 1)).alias(c + "_non_null_count")
        for c in columns_to_check
    ]
    country_counts = df.groupBy("country").agg(*agg_exprs)

    # Sum the non-null counts across all columns for each country
    total_non_null_counts = sum(F.col(c + "_non_null_count") for c in columns_to_check)
    country_counts = country_counts.withColumn(
        "total_non_null_counts", total_non_null_counts
    )

    # Filter countries based on the threshold
    countries_to_keep_df = country_counts.filter(
        F.col("total_non_null_counts") > threshold
    ).select("country")

    # Find out the countries that were dropped
    all_countries = df.select("country").distinct()
    dropped_countries_df = all_countries.subtract(countries_to_keep_df)
    dropped_countries = [row["country"] for row in dropped_countries_df.collect()]

    # Join with the original DataFrame to get the filtered data
    filtered_df = df.join(countries_to_keep_df, on="country", how="inner")

    original_row_count = df.count()
    filtered_row_count = filtered_df.count()
    rows_dropped = original_row_count - filtered_row_count

    stats = {
        "Original number of rows": original_row_count,
        "Number of rows after filtering": filtered_row_count,
        "Number of rows dropped": rows_dropped,
        "Dropped countries": dropped_countries,
    }

    print(stats)

    return filtered_df

def count_nulls_by_country(df):
    """
    Count the number of null values for each country and each column (except 'country').

    Parameters:
    - df: The input dataframe.

    Returns:
    - null_counts_df: A dataframe with the count of null values for each column and country.
    """

    # Generate the aggregation expressions
    agg_exprs = [
        F.count(F.when(F.col(c).isNull(), c)).alias(c)
        for c in df.columns
        if c != "country"
    ]

    # Group by 'country' and aggregate
    null_counts_df = df.groupBy("country").agg(*agg_exprs)

    return null_counts_df


def filter_rows_by_null_threshold(df):
    """
    Filter rows from a dataframe based on the threshold of null values across non-primary columns.

    Parameters:
    - df: The input dataframe.

    Returns:
    - filtered_df: The filtered dataframe.
    - stats: A dictionary containing statistics about the filtering process.
    """

    # Primary Key Columns
    primary_keys = ["country", "year", "iso_code"]

    # List of columns to check for null values
    columns_to_check = [col for col in df.columns if col not in primary_keys]

    # Set the threshold equal to the number of non-primary key columns
    threshold = len(columns_to_check)

    # Calculate the number of nulls for each row
    null_count = sum(
        F.when(F.col(c).isNull(), 1).otherwise(0) for c in columns_to_check
    )

    # Filter rows based on the threshold
    filtered_df = df.filter(null_count < threshold)

    original_row_count = df.count()
    filtered_row_count = filtered_df.count()
    rows_dropped = original_row_count - filtered_row_count

    stats = {
        "Original number of rows": original_row_count,
        "Number of rows after filtering": filtered_row_count,
        "Number of rows dropped": rows_dropped,
    }

    print(stats)

    return filtered_df

