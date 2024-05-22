-- Display all records with a score of 10 or higher
-- in the second_table of the hbtn_0c_0 database.
SELECT dt.score, dt.name
FROM (SELECT score, name FROM second_table) AS dt
WHERE dt.score >= 10
ORDER BY dt.score DESC;
