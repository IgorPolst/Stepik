SELECT
    CONCAT('[', a, ';', b, ']') AS range,
    a + RAND() * (b - a) AS random_value
FROM Ranges
ORDER BY id