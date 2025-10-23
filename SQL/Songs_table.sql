DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs
(
    id        SERIAL PRIMARY KEY,
    place     INTEGER,
    trackname VARCHAR(50),
    artist    VARCHAR(30)
);

INSERT INTO Songs (place, trackname, artist)
VALUES (4, 'You Just Haven''t Earned It Yet, Baby', 'The Smiths'),
       (3, 'Crazy On You', 'Heart'),
       (2, 'Dark Days', 'Theredsunband'),
       (5, 'Wish You Were Here', 'The Sounds'),
       (1, 'Let Me Kiss You', 'Morrissey');