-- Select the `title` and `genre_id` using a LEFT JOIN with a
-- NULL check to mimic INNER JOIN behavior
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
WHERE g.show_id IS NOT NULL
ORDER BY s.title, g.genre_id;

