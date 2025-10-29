SELECT name, surname
FROM Directors
WHERE 
    name = LOWER(name) 
    OR surname = LOWER(surname)
ORDER BY name;