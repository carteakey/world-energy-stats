#!/usr/bin/python3

# Import required packages
import sys
import pandas as pd
import numpy as np

# Read input csv file
energy_data = pd.read_csv(sys.stdin, header=None)

dict = {}  # Initialize dictionary to store null percentage

# Remove header row if present
energy_data = energy_data[energy_data[1] != "year"]

# Get start year and latest year
min_year = energy_data[1].astype(int).min()
max_year = energy_data[1].astype(int).max()

for year in range(min_year, max_year + 1):
    key = year

    # Count nulls and total records if data is considered starting this year
    temp_df = energy_data[energy_data[1].astype(int) >= year]

    null_count = temp_df.isna().sum().sum()
    total_count = np.product(temp_df.shape)

    dict[year] = {"null_count": null_count, "total_count": total_count}

# Replace the f-string with the format() method for Python 3.5 compatibility
for year, val in dict.items():
    print(
        "{year}\tnull_count:{null_count}\ttotal_count:{total_count}".format(
            year=year, null_count=val["null_count"], total_count=val["total_count"]
        )
    )
