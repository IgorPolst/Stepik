SELECT 
    concat(id,'. ', titel) as movie,
    concat('€', price*1.1) as price_in_eur,
    concat(rating * 10, '%') as score
FROM Films
WHERE raiting > 7
ORDER BY rating DESC
