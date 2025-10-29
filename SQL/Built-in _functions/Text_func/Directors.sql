DROP TABLE IF EXISTS Directors;
CREATE TABLE Directors
(
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(40),
    surname VARCHAR(40),
    rating  INT
);

INSERT INTO Directors (name, surname, rating)
VALUES ('Christopher', 'Nolan', 90),
       ('Steven', 'Spielberg', 79),
       ('Quentin', 'Tarantino', 95),
       ('Martin', 'Scorsese', 68),
       ('David', 'Fincher', 100),
       ('Ridley', 'Scott', 54),
       ('Stanley', 'Kubrick', 9),
       ('Clint', 'Eastwood', 74),
       ('James', 'Cameron', 8),
       ('Tim', 'Burton', 41);