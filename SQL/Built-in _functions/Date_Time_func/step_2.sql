SELECT 
    CONCAT(name, ' ', surname) AS staffer,
    hire_date + INTERVAL '1 6' YEAR_MONTH AS hire_date
FROM Staff
ORDER BY hire_date DESC