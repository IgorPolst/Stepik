SELECT name, surname, LPAD(CONCAT(rating, '%'), 4, '00') as rating
FROM Directors
ORDER BY rating 