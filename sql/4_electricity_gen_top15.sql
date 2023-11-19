SELECT
  country,
  year,
  SUM(fossil_electricity) AS total_fossil_electricity,
  SUM(
    renewables_electricity + other_renewable_electricity + fossil_electricity
  ) AS total_consumption,
  ROUND(
    SUM(fossil_electricity) / SUM(
      renewables_electricity + other_renewable_electricity + fossil_electricity
    ) * 100,
    2
  ) AS non_renewable_percentage,
  ROUND(
    100 - (
      SUM(fossil_electricity) / SUM(
        renewables_electricity + other_renewable_electricity + fossil_electricity
      ) * 100
    ),
    2
  ) AS renewable_percentage
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
    )
GROUP BY
  country,
  year
-- HAVING
--   non_renewable_percentage > 50
ORDER BY
  total_consumption DESC