SELECT id, name, surname, LEFT(email, LOCATE('@', email)) AS local_part
FROM Directors
ORDER BY id DESC
