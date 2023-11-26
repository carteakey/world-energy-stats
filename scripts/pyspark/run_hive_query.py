from utils import run_spark_sql
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Spark SQL script.")
    parser.add_argument("sql_file", help="Path to the SQL query file.")
    parser.add_argument("--save_file", help="Path to save the output.", default=None)

    args = parser.parse_args()

    run_spark_sql(args.sql_file, args.save_file)
