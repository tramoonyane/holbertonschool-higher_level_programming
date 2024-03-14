-- Query retrieves the maximum temperature recorded for each state from the temperatures table.
-- Results are grouped by state and ordered alphabetically by state name.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
