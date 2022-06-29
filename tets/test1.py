from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3"
DB_ECHO = True


def create_engine_db():
    return create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)


def create_db(engine: Engine):
    if not database_exists(engine.url):
        create_database(engine.url)
