SELECT 
    CONCAT(name, ' ',surname) AS staffer,
    MAKEDATE(hire_year, hire_day) AS hire_date
FROM Staff
ORDER BY hire_date DESC