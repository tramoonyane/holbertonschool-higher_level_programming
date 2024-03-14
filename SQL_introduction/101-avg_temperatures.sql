-- Query retrieves the average temperature for each city from the temperatures table.
-- The results are ordered in descending order of average temperature.
SELECT city, AVG(value) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
