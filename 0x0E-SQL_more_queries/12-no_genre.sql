-- Select the `title` and `genre_id` using a derived table to filter out shows with genres
SELECT s.title, d.genre_id
FROM tv_shows AS s
LEFT JOIN (
    SELECT show_id, genre_id
    FROM tv_show_genres
    WHERE genre_id IS NULL
) AS d ON s.id = d.show_id
WHERE d.genre_id IS NULL
ORDER BY s.title ASC;

