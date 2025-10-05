
from etl_movies.config import Settings

def test_settings_defaults():
    s = Settings(tmdb_api_key="", database_url="")
    assert s.tmdb_api_key == ""
    assert s.database_url == ""
