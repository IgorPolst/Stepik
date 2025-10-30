SELECT id,
    SUBSTRING_INDEX(actor, ' ', 1) AS name,
    SUBSTRING_INDEX(actor, ' ', -1) AS surname,
    DATE(birth_date) AS birth_date,
    TIME(birth_date) AS birth_time
FROM Actors