
SELECT  actual_size, limit_deviation, ABS(actual_size - nominal_size) AS difference
FROM Sizes
WHERE ABS(actual_size - nominal_size) <= limit_deviation
ORDER BY actual_size