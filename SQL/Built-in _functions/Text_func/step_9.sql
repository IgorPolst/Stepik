SELECT name, surname, REPLACE(card_number, '-', '') as card_number
FROM Clients
WHERE LEFT(surname, 1) = 'S'
ORDER BY surname
