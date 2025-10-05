
import argparse

from .db import test_connection
from .extract import iter_movies
from .load import load_tables
from .transform import normalize_movies


def main():
    parser = argparse.ArgumentParser(description="ETL TMDB → SQL")
    parser.add_argument("--mode", choices=["popular","by_year"], default="popular")
    parser.add_argument("--year", type=int, help="Año cuando mode=by_year")
    parser.add_argument("--pages", type=int, default=2, help="Número de páginas a extraer (20 items por página)")
    args = parser.parse_args()

    print(test_connection())

    raw = list(iter_movies(mode=args.mode, year=args.year, pages=args.pages))
    movies, genres, movie_genres = normalize_movies(raw)
    if movies.empty:
        print("No hay datos para cargar.")
        return

    load_tables(movies, genres, movie_genres)
    print(f"Cargado: movies={len(movies)}, genres={len(genres)}, movie_genres={len(movie_genres)}")

if __name__ == "__main__":
    main()
