SELECT id, name, surname, 
    LPAD(
        RIGHT(
            REPLACE(card_number, '-', '')
            , 4)
        , 16, '*')
        AS card_number
        
FROM Clients
LIMIT 5