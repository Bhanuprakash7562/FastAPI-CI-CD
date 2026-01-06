from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import os

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

# DB_URL = "postgresql+psycopg2://postgres:Iamironman2268$@localhost:5432/fastapiProject"
engine = create_engine(DB_URL)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        