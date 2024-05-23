-- Select the genre and count the number of shows using table aliases
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY sg.genre_id
ORDER BY number_of_shows DESC;
