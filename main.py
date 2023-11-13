import os

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Libros import Base as LibrosBase
from Models.Personas import Base as PersonasBase
from Models.Domicilio import Base as DomiciliosBase
from Models.Localidad import Base as LocalidadesBase
from Models.Autor import Base as AutoresBase


app = FastAPI()


def main():

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fastapi.db")
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    session = SessionLocal()

    try:
        LibrosBase.metadata.create_all(bind=engine, checkfirst=True)
        PersonasBase.metadata.create_all(bind=engine, checkfirst=True)
        DomiciliosBase.metadata.create_all(bind=engine, checkfirst=True)
        LocalidadesBase.metadata.create_all(bind=engine, checkfirst=True)
        AutoresBase.metadata.create_all(bind=engine, checkfirst=True)
        session.commit()

    except Exception as e:
        session.rollback()
        print(f"Error al crear las tablas: {e}")

    finally:
        session.close()

if __name__ == '__main__':
    main()
