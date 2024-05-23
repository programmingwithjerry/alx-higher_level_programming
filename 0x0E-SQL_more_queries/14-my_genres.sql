-- Select distinct genre names using a subquery in the WHERE clause
SELECT DISTINCT g.name
FROM tv_genres AS g
WHERE g.id IN (
    SELECT sg.genre_id
    FROM tv_show_genres AS sg
    INNER JOIN tv_shows AS s
    ON sg.show_id = s.id
    WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;

