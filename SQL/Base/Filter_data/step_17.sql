SELECT title, director
FROM Films
WHERE NOT(title LIKE CAST('%t%' AS BINARY))
ORDER BY title