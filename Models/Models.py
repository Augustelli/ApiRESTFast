from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
libro_autor_association = Table(
    'libro_autor_association', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libros.id')),
    Column('autor_id', Integer, ForeignKey('autores.id'))
)

class Domicilios(Base):
    __tablename__ = 'domicilios'
    id = Column(Integer, primary_key=True, index=True)
    calle = Column(String(255), nullable=False)
    numero = Column(Integer, nullable=False)
    localidad_id = Column(Integer, ForeignKey('localidades.id'))
    localidad = relationship('Localidades', back_populates='domicilios', cascade='all')

    # Relación 1 a 1 con Personas
    personas = relationship('Personas', back_populates='domicilio')


class Localidades(Base):
    __tablename__ = 'localidades'
    id = Column(Integer, primary_key=True, index=True)
    denominacion = Column(String(255))
    domicilios = relationship('Domicilios', back_populates='localidad')


class Personas(Base):
    __tablename__ = 'personas'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    dni = Column(Integer, nullable=False)

    # Relacion con domicilio 1 a 1
    domicilio_id = Column(Integer, ForeignKey('domicilios.id'))
    domicilio = relationship('Domicilios', back_populates='persona', uselist=False, cascade='all')

    # Relación 1 a N con Libros
    libros = relationship('Libros', back_populates='persona', cascade='all, delete-orphan')



class Libros(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255))
    fecha = Column(Integer)
    genero = Column(String(255))
    paginas = Column(Integer)

    # Relacion con personas 1 Persona N Libros
    autores = relationship('Autores', secondary=libro_autor_association, back_populates='libros')

    # Relación 1 a N con Personas
    persona_id = Column(Integer, ForeignKey('personas.id'))
    persona = relationship('Personas', back_populates='libros')



class Autores(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    biografia = Column(String(1500))

    # RELACION
    libros = relationship('Libro', secondary=libro_autor_association, back_populates='autores')







