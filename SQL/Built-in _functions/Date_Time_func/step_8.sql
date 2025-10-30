SELECT name, surname, birth_date
FROM Actors
WHERE DAYOFYEAR(birt_date) < 256
ORDER BY birth_date