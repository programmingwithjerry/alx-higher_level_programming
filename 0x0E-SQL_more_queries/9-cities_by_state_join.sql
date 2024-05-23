-- Use the `hbtn_0d_usa` database
USE hbtn_0d_usa;
-- Select specific columns from `cities` and `states` using a LEFT
-- JOIN with a NULL check to mimic INNER JOIN behavior
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
WHERE states.id IS NOT NULL;

