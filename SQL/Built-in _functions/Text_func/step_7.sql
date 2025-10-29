SELECT english, russian
FROM Palindromes
WHERE english = REVERSE(english) AND russian = REVERSE(russian)
ORDER BY english