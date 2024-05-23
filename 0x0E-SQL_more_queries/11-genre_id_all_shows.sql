-- Select the `title` and `genre_id`, ensuring NULL handling with COALESCE
SELECT s.title, COALESCE(g.genre_id, NULL) AS genre_id
FROM tv_shows AS s
LEFT OUTER JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id ASC;
