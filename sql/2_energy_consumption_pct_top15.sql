SELECT
    ROUND(
        (
            SUM(g.primary_energy_consumption) / t.total_energy
        ) * 100,
        2
    )
FROM
    general g
    JOIN (
        SELECT
            year,
            SUM(primary_energy_consumption) AS total_energy
        FROM
            general
        WHERE
            year = 2021
        GROUP BY
            year
    ) t ON g.year = t.year
WHERE
    g.year = 2021
    AND g.country IN (
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
    t.total_energy;