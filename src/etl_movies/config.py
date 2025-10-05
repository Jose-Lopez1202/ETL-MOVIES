
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    tmdb_api_key: str = os.getenv("TMDB_API_KEY", "")
    database_url: str = os.getenv("DATABASE_URL", "")

    def validate(self) -> None:
        if not self.tmdb_api_key:
            raise ValueError("TMDB_API_KEY no está configurada en el entorno (.env).")
        if not self.database_url:
            raise ValueError("DATABASE_URL no está configurada en el entorno (.env).")

settings = Settings()
