SELECT title, price*0.7 as discount_price
FROM Films 
WHERE price*0.7 < 4
ORDER BY discount_price