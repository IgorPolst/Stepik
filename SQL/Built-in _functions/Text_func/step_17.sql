SELECT name, surname, 
    REPLACE(email, SUBSTRING_INDEX(email, '@', 1), REPEAT(CHAR_LENGTH(SUBSTRING_INDEX(email, '@', 1)), '*')) AS email
FROM Directors
ORDER BY SUBSTRING_INDEX(email, '@', 1)