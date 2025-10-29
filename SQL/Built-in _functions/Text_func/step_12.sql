SELECT 
    RPAD(LEFT(name, 1), CHAR_LENGTH(name), '*') as name,
    RPAD(LEFT(surname, 1), CHAR_LENGTH(surname), '*') as surname
FROM Directors
ORDER BY LEFT(name, 1), LEFT(surname,1)
