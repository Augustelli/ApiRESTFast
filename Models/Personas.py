from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Models.BaseModel import BaseModel


class Personas(BaseModel):
    __tablename__ = 'personas'

    nombre = Column(String(255))
    apellido = Column(String(255))
    dni = Column(Integer, nullable=False)

    domicilio_id = Column(Integer, ForeignKey('domicilios.id'))
    domicilio = relationship('Domicilios', back_populates='persona', uselist=False, cascade='all')

    libros = relationship('Libros', back_populates='persona', cascade='all, delete-orphan')

    # __mapper_args__ = {
    #     'inherit_condition': (BaseModel.id == domicilio_id)
    # }

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return f"({self.nombre} - {self.apellido} - {self.dni})"




