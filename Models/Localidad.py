from sqlalchemy import Column, String, Integer
from sqlalchemy import Table
from .Libros import meta


localidad = Table(
    'localidades', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('denominacion', String(255))
)
