from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.BaseModel import BaseModel
from Models.Libros import libro_autor_association


class Autores(BaseModel):
    __tablename__ = 'autores'

    nombre = Column(String(255))
    apellido = Column(String(255))
    biografia = Column(String(1500))

    # RELACION
    libros = relationship('Libro', secondary=libro_autor_association, back_populates='autores')

    def __init__(self, nombre, apellido, biografia):
        self.nombre = nombre
        self.apellido = apellido
        self.biografia = biografia