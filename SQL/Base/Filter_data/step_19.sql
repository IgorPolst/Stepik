SELECT title, director
FROM Films
WHERE NOT(title LIKE '% %')
ORDER BY title