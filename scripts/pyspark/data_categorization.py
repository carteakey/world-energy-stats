from pyspark.sql import SparkSession, Window
from utils import filter_df_by_threshold

# Spark session & context
spark = (
    SparkSession.builder.appName("world-energy-stats")
    .master("spark://spark-master:7077")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)

# Read the DataFrame from the Hive table
df = spark.sql("SELECT * FROM wes.transformed_energy_data")

# LEVEL 1 CATEGORIZATION

# Primary Key Columns
primary_keys = ["country", "year", "iso_code"]

# 1. General Information
df_general = df[
    primary_keys
    + [
        "population",
        "gdp",
        "electricity_demand",
        "electricity_generation",
        "primary_energy_consumption",
    ]
]

# 2. Biofuel
df_biofuel = df[
    primary_keys
    + [
        "biofuel_consumption",
        "biofuel_electricity",
        "biofuel_share_elec",
        "biofuel_share_energy",
    ]
]

# 3. Coal
df_coal = df[
    primary_keys
    + [
        "coal_consumption",
        "coal_electricity",
        "coal_production",
        "coal_share_elec",
        "coal_share_energy",
    ]
]

# 4. Gas
df_gas = df[
    primary_keys
    + [
        "gas_consumption",
        "gas_electricity",
        "gas_production",
        "gas_share_elec",
        "gas_share_energy",
    ]
]

# 5. Oil
df_oil = df[
    primary_keys
    + [
        "oil_consumption",
        "oil_electricity",
        "oil_production",
        "oil_share_elec",
        "oil_share_energy",
    ]
]

# 6. Fossil Fuels (Aggregate)
df_fossil = df[
    primary_keys
    + [
        "fossil_electricity",
        "fossil_fuel_consumption",
        "fossil_share_elec",
        "fossil_share_energy",
        "carbon_intensity_elec",
    ]
]

# 7. Greenhouse Gas
df_greenhouse_gas = df[primary_keys + ["greenhouse_gas_emissions"]]

# 8. Hydro
df_hydro = df[
    primary_keys
    + [
        "hydro_consumption",
        "hydro_electricity",
        "hydro_share_elec",
        "hydro_share_energy",
    ]
]

# 9. Nuclear
df_nuclear = df[
    primary_keys
    + [
        "nuclear_consumption",
        "nuclear_electricity",
        "nuclear_share_elec",
        "nuclear_share_energy",
    ]
]

# 10. Renewables (Aggregate)
df_renewables = df[
    primary_keys
    + [
        "renewables_consumption",
        "renewables_electricity",
        "renewables_share_elec",
        "renewables_share_energy",
    ]
]

# 11. Solar
df_solar = df[
    primary_keys
    + [
        "solar_consumption",
        "solar_electricity",
        "solar_share_elec",
        "solar_share_energy",
    ]
]

# 12. Wind
df_wind = df[
    primary_keys
    + ["wind_consumption", "wind_electricity", "wind_share_elec", "wind_share_energy"]
]

# 13. Other Renewables
df_other_renewables = df[
    primary_keys
    + [
        "other_renewable_consumption",
        "other_renewable_electricity",
        "other_renewable_exc_biofuel_electricity",
        "other_renewables_share_elec",
        "other_renewables_share_elec_exc_biofuel",
        "other_renewables_share_energy",
    ]
]

# 14. Low Carbon
df_low_carbon = df[
    primary_keys
    + [
        "low_carbon_consumption",
        "low_carbon_electricity",
        "low_carbon_share_elec",
        "low_carbon_share_energy",
    ]
]

# 15. Electricity Imports
df_electricity_imports = df[
    primary_keys + ["net_elec_imports", "net_elec_imports_share_demand"]
]

# Calling the filter function on each dataframe
filtered_df_general = filter_df_by_threshold(df_general, 0)
filtered_df_biofuel = filter_df_by_threshold(df_biofuel, 0)
filtered_df_coal = filter_df_by_threshold(df_coal, 0)
filtered_df_gas = filter_df_by_threshold(df_gas, 0)
filtered_df_oil = filter_df_by_threshold(df_oil, 0)
filtered_df_fossil = filter_df_by_threshold(df_fossil, 0)
filtered_df_greenhouse_gas = filter_df_by_threshold(df_greenhouse_gas, 0)
filtered_df_hydro = filter_df_by_threshold(df_hydro, 0)
filtered_df_nuclear = filter_df_by_threshold(df_nuclear, 0)
filtered_df_renewables = filter_df_by_threshold(df_renewables, 0)
filtered_df_solar = filter_df_by_threshold(df_solar, 0)
filtered_df_wind = filter_df_by_threshold(df_wind, 0)
filtered_df_other_renewables = filter_df_by_threshold(df_other_renewables, 0)
filtered_df_low_carbon = filter_df_by_threshold(df_low_carbon, 0)
filtered_df_electricity_imports = filter_df_by_threshold(df_electricity_imports, 0)

# save to hive tables - partition by country
filtered_df_general.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.general"
)
filtered_df_biofuel.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.biofuel"
)
filtered_df_coal.write.mode("overwrite").partitionBy("country").saveAsTable("wes.coal")
filtered_df_gas.write.mode("overwrite").partitionBy("country").saveAsTable("wes.gas")
filtered_df_oil.write.mode("overwrite").partitionBy("country").saveAsTable("wes.oil")
filtered_df_fossil.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.fossil"
)
filtered_df_greenhouse_gas.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.greenhouse_gas"
)
filtered_df_hydro.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.hydro"
)
filtered_df_nuclear.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.nuclear"
)
filtered_df_renewables.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.renewables"
)
filtered_df_solar.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.solar"
)
filtered_df_wind.write.mode("overwrite").partitionBy("country").saveAsTable("wes.wind")
filtered_df_other_renewables.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.other_renewables"
)
filtered_df_low_carbon.write.mode("overwrite").partitionBy("country").saveAsTable(
    "wes.low_carbon"
)
filtered_df_electricity_imports.write.mode("overwrite").partitionBy(
    "country").saveAsTable("wes.electricity_imports")

spark.stop()