-- Select the genre and count the number of shows using
-- a subquery in the SELECT clause
SELECT g.name AS genre, 
       (SELECT COUNT(show_id) 
        FROM tv_show_genres 
        WHERE genre_id = g.id) AS number_of_shows
FROM tv_genres AS g
ORDER BY number_of_shows DESC;

