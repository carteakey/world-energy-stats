SELECT
    country,
    iso_code,
    primary_energy_consumption,
    RANK() OVER (
        ORDER BY
            primary_energy_consumption DESC
    ) AS RANK
FROM
    general
WHERE
    year = 2021
ORDER BY
    primary_energy_consumption DESC