from sqlalchemy import Column, String, Integer, ForeignKey, Table
from .Libros import meta

personas = Table(
    'personas', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('nombre', String(255)),
    Column('apellido', String(255)),
    Column('dni', Integer, nullable=False),
    # Relacion con domicilio 1 a 1
    Column('domicilio_id', Integer, ForeignKey('domicilios.id')))