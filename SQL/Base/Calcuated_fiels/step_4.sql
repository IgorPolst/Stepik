SELECT title, price*purchases as profit
FROM Films
ORDER BY price*purchases DESC
LIMIT 3