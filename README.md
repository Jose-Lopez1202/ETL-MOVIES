
# ETL Movies (TMDB) → SQL

Proyecto de práctica para **Python + SQL**: extracción de películas desde la API de TMDB, limpieza con `pandas` y carga a una base de datos relacional usando **SQLAlchemy**.

## 🚀 Características
- Extract: películas populares o por año/fecha desde TMDB (paginado).
- Transform: normaliza columnas y descompone géneros a una tabla puente.
- Load: inserta en tablas `movies`, `genres` y `movie_genres`.
- SQL: `sql/schema.sql` (DDL) + `sql/analytics.sql` (consultas útiles).
- Config por **variables de entorno** (`.env`).

## 📦 Instalación
```bash
# Python 3.10+ recomendado
python -m venv .venv && source .venv/bin/activate  # en Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .
```

## 🔑 Configuración
Crea un archivo `.env` en la raíz (usa `.env.example` como guía):

```
TMDB_API_KEY=TU_API_KEY_DE_TMDB
# Usa una de estas URLs de conexión:
# PostgreSQL
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/midb

# SQL Server (ODBC Driver 18)
# DATABASE_URL=mssql+pyodbc://usuario:password@localhost:1433/midb?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes
```

> **Nota**: para Postgres instala `psycopg2-binary`. Para SQL Server, instala `pyodbc` y el driver ODBC 18.

## 🗃️ Crear esquema
Ejecuta `sql/schema.sql` en tu motor (psql/SSMS/Azure Data Studio).

## ▶️ Ejecutar ETL
Ejemplos:
```bash
# Películas populares (por defecto 2 páginas)
python -m etl_movies.cli --mode popular --pages 2

# Filtrar por año específico
python -m etl_movies.cli --mode by_year --year 2024 --pages 5
```

## 📊 Consultas de ejemplo
Revisa `sql/analytics.sql` para KPIs (top rentabilidad, promedio de votos por género, etc.).

## 🧪 Tests
```bash
pytest -q
```

## 🏗️ Estructura
```
src/etl_movies/      # Código fuente (extract/transform/load/cli)
sql/                 # Esquema y consultas
data/                # Carpeta para dumps opcionales
tests/               # Pruebas
```

---

Si quieres agregar un dashboard, puedes montar uno rápido con Streamlit leyendo desde el mismo `DATABASE_URL`.
