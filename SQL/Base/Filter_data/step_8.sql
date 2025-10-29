SELECT title, director, running_time
FROM Films
WHERE (director = 'John Lasseter' OR director = 'Andrew Stanton') AND running_time > 100
ORDER BY director, title