from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    create_engine,
    func,
)

from src.config import settings

engine = create_engine(settings.DATABASE_URL)
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)
