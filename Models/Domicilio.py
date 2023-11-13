from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Domicilio(Base):
    __tablename__ = 'domicilio'

    id = Column(Integer, primary_key=True, index=True)
    calle = Column(String)
    numero = Column(Integer)

    # Relación many-to-one con la tabla Localidad
    localidad_id = Column(Integer, ForeignKey('localidad.id'))
    localidad = relationship('Localidad', back_populates='domicilios')
