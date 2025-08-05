from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from src.config import settings 

engine = create_engine(
    settings.DATABASE_URL,
    echo=True, 
)

Session = sessionmaker(
    bind=engine
)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

