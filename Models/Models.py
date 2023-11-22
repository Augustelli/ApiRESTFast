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

    def __init__(self, calle, numero, localidad_id):
        self.calle = calle
        self.numero = numero
        self.localidad_id = localidad_id

    def __repr__(self):
        return f"({self.calle} - {self.numero} - {self.localidad_id})"

class Localidades(Base):
    __tablename__ = 'localidades'
    id = Column(Integer, primary_key=True, index=True)
    denominacion = Column(String(255))
    domicilios = relationship('Domicilios', back_populates='localidad')

    def __init__(self, denominacion, domicilios):
        self.denominacion = denominacion
        self.domicilios = domicilios

    def __repr__(self):
        return f"({self.id} - {self.denominacion} - {self.domicilios})"

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

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return f"({self.nombre} - {self.apellido} - {self.dni})"

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

    def __init__(self, titulo, fecha, genero, paginas):
        self.titulo = titulo
        self.fecha = fecha
        self.genero = genero
        self.paginas = paginas

    def __repr__(self):
        return f"({self.titulo} - {self.fecha} - {self.genero} - {self.paginas})"

class Autores(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    biografia = Column(String(1500))

    # RELACION
    libros = relationship('Libro', secondary=libro_autor_association, back_populates='autores')

    def __init__(self, nombre, apellido, biografia):
        self.nombre = nombre
        self.apellido = apellido
        self.biografia = biografia




