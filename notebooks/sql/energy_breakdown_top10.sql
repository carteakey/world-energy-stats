SELECT year, SUM(coal_consumption), SUM(gas_consumption),  SUM(biofuel_consumption), 
SUM(hydro_consumption), SUM(nuclear_consumption), SUM(oil_consumption), SUM(solar_consumption), 
SUM(wind_consumption)
FROM combined_energy_data
WHERE country IN ('China','United States','India','Russia','Japan','Canada','Brazil','South Korea','Germany','Iran')
GROUP BY year