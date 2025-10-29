DROP TABLE IF EXISTS Clients;
CREATE TABLE Clients
(
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(40),
    surname     VARCHAR(40),
    card_number VARCHAR(40)
);

INSERT INTO Clients (name, surname, card_number)
VALUES ('Christopher', 'Nolan', '3409-4719-9958-3769'),
       ('Steven', 'Spielberg', '3757-1304-6041-2423'),
       ('Quentin', 'Tarantino', '3456-7725-6011-8486'),
       ('Martin', 'Scorsese', '3717-9339-7641-9962'),
       ('David', 'Fincher', '3789-9065-8560-1250'),
       ('Ridley', 'Scott', '3711-7949-7232-0127'),
       ('Stanley', 'Kubrick', '3736-9259-2982-7717'),
       ('Clint', 'Eastwood', '3484-1457-1207-8953'),
       ('James', 'Cameron', '3430-5919-7308-6348'),
       ('Tim', 'Burton', '3781-9214-6430-8051');