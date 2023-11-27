from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.BaseModel import Base
from dotenv import load_dotenv
import os

load_dotenv()
class Database:
    _instance = None
    DATABASE_URL = f"postgresql+psycopg2://{os.environ.get('USER_DB', 'admin')}:{os.environ.get('USER_DB_PWD')}@{os.environ.get('DB_IP')}/{os.environ.get('DB_NAME')}"
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)

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
        print('entro de create_database')
        db = Database()
        try:
            Base.metadata.create_all(bind=self.engine, checkfirst=True)
            db.get_session().commit()
            print('se creo la base de datos desde DATABASE')

        except Exception as e:
            db.get_session().rollback()
            print(f"Error al crear las tablas: {e}")

        finally:
            db.get_conn().close()
            db.get_session().close()
