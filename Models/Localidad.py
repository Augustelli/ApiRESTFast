from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Localidad(Base):
    __tablename__ = 'localidad'

    id = Column(Integer, primary_key=True, index=True)
    denominacion = Column(String)
