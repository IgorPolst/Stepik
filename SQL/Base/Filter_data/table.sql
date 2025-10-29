DROP TABLE IF EXISTS Films;
CREATE TABLE Films
(
    id           SERIAL PRIMARY KEY,
    title        VARCHAR(40),
    director     VARCHAR(40)
);

INSERT INTO Films (title, director)
VALUES ('Toy Story 3', 'Lee Unkrich'),
       ('Monsters University', 'Dan Scanlon'),
       ('Toy Story 2', 'John Lasseter'),
       ('WALL-E', 'Andrew Stanton'),
       ('Ratatouille', 'Brad Bird'),
       ('Up', 'Pete Docter'),
       ('Brave', 'Brenda Chapman'),
       ('Finding Nemo', 'Andrew Stanton'),
       ('Toy Story', 'John Lasseter'),
       ('The Incredibles', 'Brad Bird');