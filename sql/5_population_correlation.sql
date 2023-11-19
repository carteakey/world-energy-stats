SELECT
    country,
    population,
    (gdp / population) AS gdp_per_capita,
    (primary_energy_consumption / population) AS energy_per_capita
FROM
    general
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
        'United Kingdom',
        'Tanzania'
    )