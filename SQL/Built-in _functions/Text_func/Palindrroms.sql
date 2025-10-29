DROP TABLE IF EXISTS Palindromes;
CREATE TABLE Palindromes
(
    id      SERIAL PRIMARY KEY,
    english VARCHAR(40),
    russian VARCHAR(40)
);

INSERT INTO Palindromes(english, russian)
VALUES ('hut', 'шалаш'),
       ('rotor', 'ротор'),
       ('tenet', 'принцип'),
       ('radar', 'радар'),
       ('flood', 'потоп'),
       ('level', 'уровень'),
       ('madam', 'мадам'),
       ('deed', 'поступок'),
       ('it', 'оно'),
       ('kayak', 'каяк');