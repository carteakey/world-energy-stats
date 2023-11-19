SELECT
    year,
    round(SUM(primary_energy_consumption), 2) AS PRIM_ENERGY_CONS
FROM
    general
GROUP BY
    year
ORDER BY
    1;