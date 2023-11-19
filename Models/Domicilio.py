from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .Libros import meta

domicilio = Table(
    'domicilios', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('calle', String(255), nullable=False),
    Column('numero', Integer, nullable=False),
    # Relacion con localidad
    Column('localidad_id', Integer, ForeignKey('localidades.id'))
)