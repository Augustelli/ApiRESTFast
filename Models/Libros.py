from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from Models.BaseModel import BaseModel
Base = declarative_base()

libro_autor_association = Table(
    'libro_autor_association', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libros.id')),
    Column('autor_id', Integer, ForeignKey('autores.id'))
)

class Libros(BaseModel):
    __tablename__ = 'libros'
    titulo = Column(String(255))
    fecha = Column(Integer)
    genero = Column(String(255))
    paginas = Column(Integer)

    # Relacion con personas 1 Persona N Libros
    autores = relationship('Autores', secondary=libro_autor_association, back_populates='libros')

    # Relación 1 a N con Personas
    persona_id = Column(Integer, ForeignKey('personas.id'))
    persona = relationship('Personas', back_populates='libros')

    def __init__(self, titulo, fecha, genero, paginas):
        self.titulo = titulo
        self.fecha = fecha
        self.genero = genero
        self.paginas = paginas

    def __repr__(self):
        return f"({self.titulo} - {self.fecha} - {self.genero} - {self.paginas})"