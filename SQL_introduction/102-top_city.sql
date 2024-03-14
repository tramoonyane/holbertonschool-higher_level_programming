-- Query retrieves the average temperature for each city during July and August from the temperatures table.
-- Results are grouped by city and ordered in descending order of average temperature. The top 3 cities are displayed.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
