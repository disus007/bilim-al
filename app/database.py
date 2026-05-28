from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite — файл создаётся автоматически в папке проекта
SQLALCHEMY_DATABASE_URL = "sqlite:///./ai_tutor.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Даёт сессию БД на время запроса, закрывает после."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()