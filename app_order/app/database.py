from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine_ord = create_engine(settings.postgres_url_ord, echo=True)
engine_product = create_engine(settings.postgres_url_product, echo=True)
SessionLocalOrd = sessionmaker(autocommit=False, autoflush=False, bind=engine_ord)
SessionLocalProduct = sessionmaker(autocommit=False, autoflush=False, bind=engine_product)


def get_db_ord():
    db_ord = SessionLocalOrd()
    try:
        yield db_ord
    finally:
        db_ord.close()


def get_db_product():
    db_product = SessionLocalProduct()
    try:
        yield db_product
    finally:
        db_product.close()
