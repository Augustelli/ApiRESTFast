from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer)

    domicilio_id = Column(Integer, ForeignKey('domicilio.id'))
    domicilio = relationship('Domicilio', uselist=False, back_populates='persona')

    libros = relationship('Libro', cascade='all, delete-orphan', secondary='persona_libro', back_populates='persona')

persona_libro_association = Table(
    'persona_libro',
    Base.metadata,
    Column('persona_id', Integer, ForeignKey('persona.id')),
    Column('libro_id', Integer, ForeignKey('libro.id'))
)
