
from typing import Tuple
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

MOVIE_COLUMNS = [
    "id","title","original_language","release_date","popularity","vote_average","vote_count",
    "adult","video","overview","original_title"
]

def normalize_movies(raw_list: list[dict]) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    df = pd.DataFrame(raw_list)
    if df.empty:
        return df, pd.DataFrame(), pd.DataFrame()

    # Asegurar columnas
    for col in MOVIE_COLUMNS:
        if col not in df.columns:
            df[col] = None

    # Normal movie table
    movies = df[MOVIE_COLUMNS].copy()
    movies["release_date"] = pd.to_datetime(movies["release_date"], errors="coerce").dt.date

    # Genres (list of dicts)
    explode = df[["id","genre_ids"]].explode("genre_ids")
    explode = explode.rename(columns={"id": "movie_id", "genre_ids": "genre_id"}).dropna()

    # Genres master (from TMDB static ids not included; we'll derive from provided IDs only)
    genres = explode[["genre_id"]].drop_duplicates().rename(columns={"genre_id":"id"})
    genres["name"] = None  # TMDB requiere otra llamada para nombres; opcionalmente puedes mapear luego.

    # Bridge
    movie_genres = explode.drop_duplicates().reset_index(drop=True)

    # Simple schema validation
    movie_schema = DataFrameSchema({
        "id": Column(int),
        "title": Column(str, nullable=True),
    }, coerce=True)

    movie_schema.validate(movies, lazy=True)
    return movies, genres, movie_genres
