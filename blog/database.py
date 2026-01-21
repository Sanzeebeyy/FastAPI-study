from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DB_URL)

LocalSession = sessionmaker(bind=engine, autocommit = False ,autoflush=False)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

