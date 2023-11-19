WITH total_consumption AS (
    SELECT
        year,
        (
            SUM(coal_consumption) + SUM(gas_consumption) + SUM(biofuel_consumption) + SUM(hydro_consumption) + SUM(nuclear_consumption) + SUM(oil_consumption) + SUM(solar_consumption) + SUM(wind_consumption)
        ) AS total_consumption
    FROM
        combined_energy_data
    WHERE
        country IN (
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
        )
    GROUP BY
        year
)
SELECT
    e.year,
    SUM(renewables_consumption) / t.total_consumption * 100 AS perc_ren_consumption,
    SUM(coal_consumption) / t.total_consumption * 100 AS perc_coal_consumption,
    SUM(gas_consumption) / t.total_consumption * 100 AS perc_gas_consumption,
    SUM(biofuel_consumption) / t.total_consumption * 100 AS perc_biofuel_consumption,
    SUM(hydro_consumption) / t.total_consumption * 100 AS perc_hydro_consumption,
    SUM(nuclear_consumption) / t.total_consumption * 100 AS perc_nuclear_consumption,
    SUM(oil_consumption) / t.total_consumption * 100 AS perc_oil_consumption,
    SUM(solar_consumption) / t.total_consumption * 100 AS perc_solar_consumption,
    SUM(wind_consumption) / t.total_consumption * 100 AS perc_wind_consumption
FROM
    combined_energy_data e
    LEFT JOIN total_consumption t ON e.year = t.year
WHERE
    e.country IN (
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
    )
GROUP BY
    e.year,
    t.total_consumption
ORDER BY
    1;