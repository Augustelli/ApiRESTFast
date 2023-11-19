from sqlalchemy import Column, String, Integer, Table
from .Libros import meta


autores = Table(
    'autores', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('nombre', String(255)),
    Column('apellido', String(255)),
    Column('biografia', String(1500))
)