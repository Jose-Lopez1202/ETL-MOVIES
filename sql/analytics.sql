
-- Top 20 películas por promedio de votos (mínimo 500 votos)
SELECT title, release_date, vote_average, vote_count
FROM movies
WHERE vote_count >= 500
ORDER BY vote_average DESC, vote_count DESC
LIMIT 20;

-- Conteo de películas por año
SELECT EXTRACT(YEAR FROM release_date) AS anio, COUNT(*) AS total
FROM movies
GROUP BY 1
ORDER BY 1;

-- Top géneros por cantidad de películas
SELECT g.name, COUNT(*) AS total
FROM movie_genres mg
JOIN genres g ON g.id = mg.genre_id
GROUP BY g.name
ORDER BY total DESC;
