-- Select the genre and count distinct show IDs to ensure unique count
SELECT g.name AS genre, COUNT(DISTINCT sg.show_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
