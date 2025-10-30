SELECT name, surname, birth_time
FROM Actors
WHERE 
    HOUR(birth_time) = 8
    OR HOUR(birth_time) = 10
    OR HOUR(birth_time) = 18
ORDER BY birth_time
