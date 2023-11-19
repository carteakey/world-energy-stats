SELECT
  country,
  year,
  fossil_share_elec,
  renewables_share_elec,
  electricity_demand,
  electricity_generation,
  GREATEST(
    biofuel_share_elec,
    coal_share_elec,
    gas_share_elec,
    oil_share_elec,
    hydro_share_elec,
    nuclear_share_elec,
    solar_share_elec,
    wind_share_elec,
    other_renewables_share_elec,
    low_carbon_share_elec
  ) AS max_share,
  CASE
    WHEN biofuel_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'biofuel_share_elec'
    WHEN coal_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'coal_share_elec'
    WHEN gas_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'gas_share_elec'
    WHEN oil_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'oil_share_elec'
    WHEN hydro_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'hydro_share_elec'
    WHEN nuclear_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'nuclear_share_elec'
    WHEN solar_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'solar_share_elec'
    WHEN wind_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'wind_share_elec'
    WHEN other_renewables_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'other_renewables_share_elec'
    WHEN low_carbon_share_elec = GREATEST(
      biofuel_share_elec,
      coal_share_elec,
      gas_share_elec,
      oil_share_elec,
      hydro_share_elec,
      nuclear_share_elec,
      solar_share_elec,
      wind_share_elec,
      other_renewables_share_elec,
      low_carbon_share_elec
    ) THEN 'low_carbon_share_elec'
  END AS max_share_name
FROM
  combined_energy_data
WHERE
  year = 2021
  AND country IN (
    'China',
    'United States',
    'India',
    'Russia',
    'Japan',
    'Canada',
    'Brazil',
    'South Korea',
    'Germany',
    'Iran',
    'Saudi Arabia',
    'France',
    'Mexico',
    'Indonesia',
    'United Kingdom'
    -- 'Iceland'
  )
ORDER BY
  electricity_generation DESC