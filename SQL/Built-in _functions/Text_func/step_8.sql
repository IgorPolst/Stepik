SELECT 
    REPEAT(english, CHAR_LENGTH(english))
        AS english
FROM Palindromes
WHERE NOT (russian = REVERSE(russian))