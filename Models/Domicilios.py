from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Models.BaseModel import BaseModel


class Domicilios(BaseModel):
    __tablename__ = 'domicilios'

    calle = Column(String(255), nullable=False)
    numero = Column(Integer, nullable=False)
    localidad_id = Column(Integer, ForeignKey('localidades.id'))
    localidad = relationship('Localidades', back_populates='domicilios', cascade='all')

    personas = relationship('Personas', back_populates='domicilio')

    def __init__(self, calle, numero, localidad_id):
        self.calle = calle
        self.numero = numero
        self.localidad_id = localidad_id

    def __repr__(self):
        return f"({self.calle} - {self.numero} - {self.localidad_id})"