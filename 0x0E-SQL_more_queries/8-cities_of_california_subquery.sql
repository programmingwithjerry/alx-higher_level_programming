-- Use the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Select all columns from `cities` where the state name is 'California'
-- Join `cities` with `states` on `state_id` and `id`
SELECT cities.*
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
