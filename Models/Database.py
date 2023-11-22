from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models.Models import *


class Database:
    _instance = None
    DATABASE_URL = "mysql+pymysql://root:Sup3rSecret0@localhost:3306/fastapi"
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine = cls.engine
            cls._instance._SessionLocal = cls.SessionLocal
            cls._instance._session = cls.SessionLocal()
            cls._instance._conn = cls.engine.connect()
        return cls._instance

    def get_session(self):
        return self._session

    def get_conn(self):
        return self._conn

    def create_database(self):
        db = Database()
        try:
            Base.metadata.create_all(bind=self.engine, checkfirst=True)
            db.get_session().commit()

        except Exception as e:
            db.get_session().rollback()
            print(f"Error al crear las tablas: {e}")

        finally:
            db.get_conn().close()
            db.get_session().close()
