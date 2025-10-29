SELECT 
    CONCAT(UPPER(LEFT(name, 1)), SUBSTRING(name, 2)) AS name,
    
    CONCAT(UPPER(LEFT(surname, 1)), SUBSTRING(surname, 2)) AS surname
FROM Directors
WHERE BINARY name = LOWER(name) 
    OR BINARY surname = LOWER(surname)
ORDER BY name