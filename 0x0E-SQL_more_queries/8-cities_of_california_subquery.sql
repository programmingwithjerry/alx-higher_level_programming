-- Use the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Select all columns from `cities` where the state name is 'California'
-- Use a CTE to simplify the query
WITH cali_state AS (
    SELECT id FROM states WHERE name = 'California'
)
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM cali_state)
ORDER BY id ASC;

