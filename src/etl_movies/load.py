
from typing import Tuple
import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine
from .db import get_engine

def load_tables(movies: pd.DataFrame, genres: pd.DataFrame, movie_genres: pd.DataFrame, if_exists: str = "append") -> None:
    engine: Engine = get_engine()
    with engine.begin() as conn:
        movies.to_sql("movies", con=conn, if_exists=if_exists, index=False)
        if not genres.empty:
            genres.to_sql("genres", con=conn, if_exists=if_exists, index=False)
        if not movie_genres.empty:
            movie_genres.to_sql("movie_genres", con=conn, if_exists=if_exists, index=False)

        # Ejemplo de post-proceso: eliminar duplicados básicos (para motores que lo permitan)
        try:
            conn.execute(text("""
                DELETE FROM movies a
                USING movies b
                WHERE a.ctid < b.ctid AND a.id = b.id
            """))
        except Exception:
            pass
