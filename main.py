from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.Libros import libro, libro_autor_association
from Models.Personas import personas
from Models.Domicilio import domicilio
from Models.Localidad import localidad
from Models.Autor import autores

from Controllers.AutorController import autores_endpoint

app = FastAPI()

def create_databas():
# USER:PASSWORD -> Meter en variable de entorno.
    DATABASE_URL = "mysql+pymysql://root:Sup3rSecret0@localhost:3306/fastapi"
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    session = SessionLocal()

    try:
        localidad.metadata.create_all(bind=engine, checkfirst=True)
        libro.metadata.create_all(bind=engine, checkfirst=True)
        libro_autor_association.metadata.create_all(bind=engine, checkfirst=True)
        personas.metadata.create_all(bind=engine, checkfirst=True)
        domicilio.metadata.create_all(bind=engine, checkfirst=True)
        autores.metadata.create_all(bind=engine, checkfirst=True)
        session.commit()

        conn = engine.connect()

        return conn

    except Exception as e:
        session.rollback()
        print(f"Error al crear las tablas: {e}")

    finally:
        session.close()

def create_api():
    base_url = '/restFake/v1'
    app = FastAPI()
    app.include_router(autores_endpoint.router, prefix=f"{base_url}/autores", tags=['autores'])


if __name__ == '__main__':
    create_api()

