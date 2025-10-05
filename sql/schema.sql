
-- Esquema base para películas (PostgreSQL/SQL Server compatible con ligeros ajustes)
CREATE TABLE IF NOT EXISTS movies (
    id              BIGINT PRIMARY KEY,
    title           VARCHAR(400),
    original_title  VARCHAR(400),
    original_language VARCHAR(20),
    release_date    DATE,
    popularity      NUMERIC(12,3),
    vote_average    NUMERIC(4,2),
    vote_count      INT,
    adult           BOOLEAN,
    video           BOOLEAN,
    overview        TEXT
);

CREATE TABLE IF NOT EXISTS genres (
    id      BIGINT PRIMARY KEY,
    name    VARCHAR(120) NULL
);

CREATE TABLE IF NOT EXISTS movie_genres (
    movie_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);
