SELECT title, 
    ROUND(
        (flickmetrix + metcritic + imdb + letterboxd + kinopoisk
        - LEAST(flickmetrix, metcritic, imdb, letterboxd, kinopoisk)
        - GREATEST(flickmetrix, metcritic, imdb, letterboxd, kinopoisk)
        )/3
    ,2)
    AS average_rating
FROM Movies 
ORDER BY average_rating DESC, title