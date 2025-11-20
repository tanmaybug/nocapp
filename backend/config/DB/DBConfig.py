from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException, status
from sqlalchemy.exc import OperationalError

from config.config import settings

# print(settings.POSTGRES_HOST)

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/database_name"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DATABASE}"
# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL) #echo=True # use echo=true to display all the queries

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    # db = SessionLocal()
    try:
        # Attempt a simple operation to check connectivity (e.g., a dummy query)
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("Database connected successfully") 
        yield db
    except OperationalError as e:
        print("Database connection failed:", e)
        # Handle specific database connection errors if needed
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=f"Database connection failed: {str(e)}"
        )
    finally:
        db.close()
