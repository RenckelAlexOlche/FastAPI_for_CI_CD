import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URL = "mysql://{user}:{password}@{host}:{port}/{db}".format(
    user     = os.environ.get('MYSQL_USER', 'root'),
    password = quote_plus(os.environ.get('MYSQL_PASSWORD', 'password')),
    host     = os.environ.get('MYSQL_HOST', 'localhost'),
    port     = os.environ.get('MYSQL_PORT', '3306'),
    db       = os.environ.get('MYSQL_DB', 'mydb')
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base: DeclarativeMeta = declarative_base()
