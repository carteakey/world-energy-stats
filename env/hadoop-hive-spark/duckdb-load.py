import duckdb
import os
from glob import glob

# Specify the path to the DuckDB database file (replace 'mydatabase.db' with your desired name)
db_path = "energy-clean-data.db"

# Specify the folder path where part files are located
folder_path = "notebooks/clean/"

# Connect to the DuckDB database (create one if it doesn't exist)
con = duckdb.connect(db_path)

# # List part files in the folder
part_files = [f for f in glob(folder_path + "*.csv")]

print(part_files)

# Iterate through each part file and read it into a DuckDB table
for part_file in part_files:
    table_name = os.path.splitext(os.path.basename(part_file))[
        0
    ]  # Extract table name from file name
    print(
        f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM read_csv_auto('{part_file}', header=true);"
    )
    con.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM read_csv_auto('{part_file}', header=true);"
    )

# Close the DuckDB connection
con.close()
