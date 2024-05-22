-- Grouping - Display the count of records for each score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
