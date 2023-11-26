#!/usr/bin/python3

# Import required packages
import sys
import pandas as pd

# Read input csv file
energy_data = pd.read_csv(sys.stdin, header=None)

data_dict = {}  # Initialize dictionary to store data stats for each column

# Pass list of column names
col_list = [
    "iso_code",
    "country",
    "year",
    "coal_prod_change_pct",
    "coal_prod_change_twh",
    "gas_prod_change_pct",
    "gas_prod_change_twh",
    "oil_prod_change_pct",
    "oil_prod_change_twh",
    "energy_cons_change_pct",
    "energy_cons_change_twh",
    "biofuel_share_elec",
    "biofuel_elec_per_capita",
    "biofuel_cons_change_pct",
    "biofuel_share_energy",
    "biofuel_cons_change_twh",
    "biofuel_consumption",
    "biofuel_cons_per_capita",
    "carbon_intensity_elec",
    "coal_share_elec",
    "coal_cons_change_pct",
    "coal_share_energy",
    "coal_cons_change_twh",
    "coal_consumption",
    "coal_elec_per_capita",
    "coal_cons_per_capita",
    "coal_production",
    "coal_prod_per_capita",
    "electricity_generation",
    "biofuel_electricity",
    "coal_electricity",
    "fossil_electricity",
    "gas_electricity",
    "hydro_electricity",
    "nuclear_electricity",
    "oil_electricity",
    "other_renewable_electricity",
    "other_renewable_exc_biofuel_electricity",
    "renewables_electricity",
    "solar_electricity",
    "wind_electricity",
    "energy_per_gdp",
    "energy_per_capita",
    "fossil_cons_change_pct",
    "fossil_share_energy",
    "fossil_cons_change_twh",
    "fossil_fuel_consumption",
    "fossil_energy_per_capita",
    "fossil_cons_per_capita",
    "fossil_share_elec",
    "gas_share_elec",
    "gas_cons_change_pct",
    "gas_share_energy",
    "gas_cons_change_twh",
    "gas_consumption",
    "gas_elec_per_capita",
    "gas_energy_per_capita",
    "gas_production",
    "gas_prod_per_capita",
    "hydro_share_elec",
    "hydro_cons_change_pct",
    "hydro_share_energy",
    "hydro_cons_change_twh",
    "hydro_consumption",
    "hydro_elec_per_capita",
    "hydro_energy_per_capita",
    "low_carbon_share_elec",
    "low_carbon_electricity",
    "low_carbon_elec_per_capita",
    "low_carbon_cons_change_pct",
    "low_carbon_share_energy",
    "low_carbon_cons_change_twh",
    "low_carbon_consumption",
    "low_carbon_energy_per_capita",
    "nuclear_share_elec",
    "nuclear_cons_change_pct",
    "nuclear_share_energy",
    "nuclear_cons_change_twh",
    "nuclear_consumption",
    "nuclear_elec_per_capita",
    "nuclear_energy_per_capita",
    "oil_share_elec",
    "oil_cons_change_pct",
    "oil_share_energy",
    "oil_cons_change_twh",
    "oil_consumption",
    "oil_elec_per_capita",
    "oil_energy_per_capita",
    "oil_production",
    "oil_prod_per_capita",
    "other_renewables_elec_per_capita",
    "other_renewables_share_elec",
    "other_renewables_cons_change_pct",
    "other_renewables_share_energy",
    "other_renewables_cons_change_twh",
    "other_renewable_consumption",
    "other_renewables_energy_per_capita",
    "per_capita_electricity",
    "population",
    "primary_energy_consumption",
    "renewables_elec_per_capita",
    "renewables_share_elec",
    "renewables_cons_change_pct",
    "renewables_share_energy",
    "renewables_cons_change_twh",
    "renewables_consumption",
    "renewables_energy_per_capita",
    "solar_share_elec",
    "solar_cons_change_pct",
    "solar_share_energy",
    "solar_cons_change_twh",
    "solar_consumption",
    "solar_elec_per_capita",
    "solar_energy_per_capita",
    "gdp",
    "wind_share_elec",
    "wind_cons_change_pct",
    "wind_share_energy",
    "wind_cons_change_twh",
    "wind_consumption",
    "wind_elec_per_capita",
    "wind_energy_per_capita",
]

# Initialize dictionary
for ind in col_list:
    data_dict[ind] = {
        "null_c": 0,
        "min": float("inf"),
        "max": float("-inf"),
        "sum": 0,
        "count": 0,
    }

# Processing data
for ind, col_name in enumerate(col_list):
    series = energy_data[ind]

    # Convert series to numeric, non-convertible values will become NaN
    series = pd.to_numeric(series, errors="coerce")

    # non_null_series = series.dropna()
    data_dict[col_name]["null_c"] = series.isna().sum()
    data_dict[col_name]["min"] = series.min() if not series.empty else "NA"
    data_dict[col_name]["max"] = series.max() if not series.empty else "NA"
    data_dict[col_name]["sum"] = series.sum()
    data_dict[col_name]["count"] = series.count()

# Output results
for column, val in data_dict.items():
    mean_val = round(val["sum"] / val["count"], 3) if val["count"] > 0 else "NA"
    min_val = val["min"] if val["min"] != float("inf") else "NA"
    max_val = val["max"] if val["max"] != float("-inf") else "NA"
    print(
        "{}\tNull_Count:{}\tMin:{}\tMax:{}\tSum:{}\tCount:{}\tMean:{}".format(
            column,
            val["null_c"],
            min_val,
            max_val,
            val["sum"],
            val["count"],
            mean_val,
        )
    )
