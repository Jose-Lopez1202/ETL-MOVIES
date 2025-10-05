
from typing import Any, Dict, Iterator

import requests

from .config import settings

BASE_URL = "https://api.themoviedb.org/3"

def _get(path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {settings.tmdb_api_key}"} if settings.tmdb_api_key.startswith("ey") else {}
    # Si la API key es v3 (cadena simple), usar como parámetro
    if not headers:
        params = {**params, "api_key": settings.tmdb_api_key}
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()

def iter_movies(mode: str = "popular", year: int | None = None, pages: int = 1) -> Iterator[Dict[str, Any]]:
    """Itera películas según modo: 'popular' o 'by_year'."""
    for page in range(1, pages + 1):
        if mode == "popular":
            data = _get("/movie/popular", {"page": page})
        elif mode == "by_year":
            if year is None:
                raise ValueError("Debes especificar 'year' cuando mode='by_year'.")
            data = _get("/discover/movie", {"page": page, "primary_release_year": year, "sort_by": "popularity.desc"})
        else:
            raise ValueError("Modo no soportado. Usa 'popular' o 'by_year'.")

        for m in data.get("results", []):
            yield m
