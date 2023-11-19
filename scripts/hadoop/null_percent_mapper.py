#!/anaconda/envs/py38_default/bin/python3

# Import required packages
import sys
import pandas as pd
import numpy as np

# Read input csv file
energy_data = pd.read_csv(sys.stdin, header=None)

dict = {}  # Initialize dictionary to store null percentage

energy_data = energy_data[energy_data[2] != "year"]  # remove header row if present

min_year = energy_data[2].astype(int).min()  # Get start year
max_year = energy_data[2].astype(int).max()  # Get leatest year

for year in range(min_year, max_year + 1):
    key = year

    # Count nulls and toal records if data is considered starting this year
    temp_df = energy_data[energy_data[2].astype(int) >= year]

    null_count = temp_df.isna().sum().sum()
    total_count = np.product(temp_df.shape)

    dict[year] = {"null_count": null_count, "total_count": total_count}

for year, val in dict.items():
    # Print all the values
    print(f"{year}\tnull_count:{val['null_count']}\ttotal_count:{val['total_count']}")
