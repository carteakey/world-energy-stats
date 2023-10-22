#!/anaconda/envs/py38_default/bin/python3

# Import required packages
import sys
import pandas as pd

# Read input csv file
energy_data = pd.read_csv(sys.stdin, header=None)

dict = {} # Initialize dictionary to store data stats for each column

# Pass list of column names
col_list = ['iso_code', 'country', 'year', 'coal_prod_change_pct', 'coal_prod_change_twh', 'gas_prod_change_pct', 'gas_prod_change_twh',
     'oil_prod_change_pct', 'oil_prod_change_twh', 'energy_cons_change_pct', 'energy_cons_change_twh', 'biofuel_share_elec', 'biofuel_elec_per_capita',
     'biofuel_cons_change_pct', 'biofuel_share_energy', 'biofuel_cons_change_twh', 'biofuel_consumption', 'biofuel_cons_per_capita', 
     'carbon_intensity_elec', 'coal_share_elec', 'coal_cons_change_pct', 'coal_share_energy', 'coal_cons_change_twh', 'coal_consumption', 
     'coal_elec_per_capita', 'coal_cons_per_capita', 'coal_production', 'coal_prod_per_capita','electricity_generation', 'biofuel_electricity', 
     'coal_electricity', 'fossil_electricity', 'gas_electricity', 'hydro_electricity', 'nuclear_electricity', 'oil_electricity', 'other_renewable_electricity', 
     'other_renewable_exc_biofuel_electricity', 'renewables_electricity', 'solar_electricity', 'wind_electricity', 'energy_per_gdp', 'energy_per_capita', 
     'fossil_cons_change_pct','fossil_share_energy', 'fossil_cons_change_twh', 'fossil_fuel_consumption', 'fossil_energy_per_capita', 'fossil_cons_per_capita',
     'fossil_share_elec', 'gas_share_elec', 'gas_cons_change_pct', 'gas_share_energy', 'gas_cons_change_twh', 'gas_consumption', 'gas_elec_per_capita', 
     'gas_energy_per_capita', 'gas_production', 'gas_prod_per_capita', 'hydro_share_elec','hydro_cons_change_pct', 'hydro_share_energy', 
     'hydro_cons_change_twh', 'hydro_consumption', 'hydro_elec_per_capita', 'hydro_energy_per_capita', 'low_carbon_share_elec', 'low_carbon_electricity', 
     'low_carbon_elec_per_capita','low_carbon_cons_change_pct', 'low_carbon_share_energy', 'low_carbon_cons_change_twh', 'low_carbon_consumption', 
     'low_carbon_energy_per_capita', 'nuclear_share_elec', 'nuclear_cons_change_pct', 'nuclear_share_energy', 'nuclear_cons_change_twh', 
     'nuclear_consumption', 'nuclear_elec_per_capita', 'nuclear_energy_per_capita', 'oil_share_elec','oil_cons_change_pct', 'oil_share_energy', 
     'oil_cons_change_twh', 'oil_consumption', 'oil_elec_per_capita', 'oil_energy_per_capita', 'oil_production', 'oil_prod_per_capita', 
     'other_renewables_elec_per_capita','other_renewables_share_elec', 'other_renewables_cons_change_pct', 'other_renewables_share_energy', 
     'other_renewables_cons_change_twh', 'other_renewable_consumption', 'other_renewables_energy_per_capita', 'per_capita_electricity', 'population', 
     'primary_energy_consumption', 'renewables_elec_per_capita', 'renewables_share_elec', 'renewables_cons_change_pct', 'renewables_share_energy', 
     'renewables_cons_change_twh', 'renewables_consumption', 'renewables_energy_per_capita', 'solar_share_elec', 'solar_cons_change_pct', 'solar_share_energy', 
     'solar_cons_change_twh', 'solar_consumption', 'solar_elec_per_capita', 'solar_energy_per_capita', 'gdp', 'wind_share_elec', 'wind_cons_change_pct', 
     'wind_share_energy', 'wind_cons_change_twh', 'wind_consumption', 'wind_elec_per_capita', 'wind_energy_per_capita']

# Initialize 0 value for each column's null count, min, max, sum, count
for ind in col_list:
    dict[ind] = {'null_c': 0, 'min': 0, 'max': 0, 'sum': 0, 'count': 0}

for ind in range(0,2):
    # for non-numeric column, count number of nulls
    key = col_list[ind] 
    dict[key]['null_c'] = energy_data[ind].isna().sum()

for ind in range(2, len(col_list)):
# For numeric columns, count nulls, min, max, sum
    key = col_list[ind]
    dict[key]['null_c'] = energy_data[ind].isna().sum() # Null Count
    dict[key]['min'] = energy_data[ind].min() # Minimum value
    dict[key]['max'] = energy_data[ind].max() # Maximum Value
    dict[key]['sum'] = energy_data[ind].sum() # Total Sum
    dict[key]['count'] = energy_data.shape[0] - dict[key]['null_c'] # Count Not nulls

for column, val in dict.items():
    # Print all the values
    print(f"{column}\tnull_count:{val['null_c']}\tmin:{val['min']}\tmax:{val['max']}\tsum:{val['sum']}\tcount:{val['count']}")