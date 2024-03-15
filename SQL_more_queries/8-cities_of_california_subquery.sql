-- SQL query to list all cities of California in the database hbtn_0d_usa using subquery

-- Query to retrieve the state_id for California from the states table
SELECT id
FROM states
WHERE name = 'California';

-- Query to list all cities of California using the retrieved state_id and sorting by cities.id
SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
