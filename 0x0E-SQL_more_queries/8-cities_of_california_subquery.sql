-- Use the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Select all columns from `cities` where the state name is 'California'
-- Use a derived table (subquery in the FROM clause)
SELECT cities.*
FROM cities, (SELECT id FROM states WHERE name = 'California') AS cali
WHERE cities.state_id = cali.id
ORDER BY cities.id ASC;

