
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from .config import settings


def get_engine(echo: bool = False) -> Engine:
    """Crea un engine de SQLAlchemy a partir de DATABASE_URL."""
    url = settings.database_url
    if not url:
        raise ValueError("DATABASE_URL no está configurada.")
    engine = create_engine(url, echo=echo, future=True)
    return engine

def test_connection() -> str:
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return "Conexión OK"
