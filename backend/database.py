from pathlib import Path # easy path handling
from sqlite3 import connect # connector for sqlite3

from sqlalchemy import create_engine # engine for sqlalchemy
from sqlalchemy.orm import DeclarativeBase, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent # Path to the Base of the Project
DATABASE_PATH = BASE_DIR / "data" / "fleet.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker( # create the db session
    bind=engine,
    autoflush=False, # auto delete entries
    autocommit=False, # auto "save"
)


class Base(DeclarativeBase):
    pass
