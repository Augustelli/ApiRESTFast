from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

libro_autor_association = Table(
    'libro_autor_association',
    Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)

class Libro(Base):
    __tablename__ = 'libro'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    fecha = Column(Integer)
    genero = Column(String)
    paginas = Column(Integer)

    autores = relationship('Autor', secondary=libro_autor_association, back_populates='libros')
