SELECT LPAD('', CHAR_LENGTH(name), '*') as name, surname
FROM Directors
ORDER BY name DESC, surname