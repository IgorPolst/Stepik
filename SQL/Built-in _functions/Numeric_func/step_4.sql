SELECT title, director, 
CONCAT(
    LPAD(runningtime DIV 60, 2, '0'),
    ':',
    LPAD(running_time MOD 60 ,2,'0')
) AS timing
FROM Films
ORDER BY timing DESC
