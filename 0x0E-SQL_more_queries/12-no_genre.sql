-- Select the `title` and `genre_id` using NOT EXISTS to check for absence of genres
SELECT s.title, NULL AS genre_id
FROM tv_shows AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres AS g
    WHERE s.id = g.show_id
)
ORDER BY s.title ASC;

