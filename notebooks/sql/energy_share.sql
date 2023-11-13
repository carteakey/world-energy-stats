SELECT
	country,
	year,
	(biofuel_consumption / total_energy_consumption) * 100 AS biofuel_share,
	(coal_consumption / total_energy_consumption) * 100 AS coal_share,
	(gas_consumption / total_energy_consumption) * 100 AS gas_share,
	(oil_consumption / total_energy_consumption) * 100 AS oil_share,
	(nuclear_consumption / total_energy_consumption) * 100 AS nuclear_share,
	(hydro_consumption / total_energy_consumption) * 100 AS hydro_share,
	(solar_consumption / total_energy_consumption) * 100 AS solar_share,
	(wind_consumption / total_energy_consumption) * 100 AS wind_share,
	(other_renewable_consumption / total_energy_consumption) * 100 AS other_renewables_share
FROM
	(
	SELECT
		country,
		year,
		biofuel_consumption,
		coal_consumption,
		gas_consumption,
		oil_consumption,
		nuclear_consumption,
		hydro_consumption,
		solar_consumption,
		wind_consumption,
		other_renewable_consumption,
		(biofuel_consumption + coal_consumption + gas_consumption + oil_consumption + nuclear_consumption + hydro_consumption + solar_consumption + wind_consumption + other_renewable_consumption) AS total_energy_consumption
	FROM
		combined_energy_data) t
WHERE
	country IN (
	SELECT
		COUNTRY
	FROM
		(
		Select
			country,
			primary_energy_consumption
		from
			combined_energy_data
		WHERE
			YEAR = 2022
		ORDER BY
			primary_energy_consumption DESC LIMIT 10) S )
ORDER BY
	1,2 DESC
