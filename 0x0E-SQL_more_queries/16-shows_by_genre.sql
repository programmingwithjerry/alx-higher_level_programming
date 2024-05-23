-- Select show titles and genre names using table aliases
SELECT s.title, g.name
FROM tv_shows AS s
LEFT OUTER JOIN tv_show_genres AS sg
ON sg.show_id = s.id
LEFT OUTER JOIN tv_genres AS g
ON g.id = sg.genre_id
ORDER BY s.title ASC, g.name ASC;
