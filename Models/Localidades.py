from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.BaseModel import BaseModel


class Localidades(BaseModel):
    __tablename__ = 'localidades'
    denominacion = Column(String(255))
    domicilios = relationship('Domicilios', back_populates='localidad')

    def __init__(self, denominacion, domicilios):
        self.denominacion = denominacion
        self.domicilios = domicilios

    def __repr__(self):
        return f"({self.id} - {self.denominacion} - {self.domicilios})"