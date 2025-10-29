SELECT name, surname, 
    REPLACE(email, SUBSTRING_INDEX(email, '@', -1), 'pygen.ru') AS email 
FROM Directors
WHERE SUBSTRING_INDEX(email, '@', -1) = 'outlook.com'
ORDER BY email