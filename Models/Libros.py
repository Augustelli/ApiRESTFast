from sqlalchemy import Column, Integer, String, Table, ForeignKey, MetaData

meta = MetaData()

# Tabla intermedia


libro = Table(
    'libros', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('titulo', String(255)),
    Column('fecha', Integer),
    Column('genero', String(255)),
    Column('paginas', Integer),
    # Relacion con personas 1 Persona N Libros
    Column('persona_id', Integer, ForeignKey('personas.id'))
)


libro_autor_association = Table(
    'libro_autor_association', meta,
    Column('libro_id', Integer, ForeignKey('libros.id')),
    Column('autor_id', Integer, ForeignKey('autores.id'))
)
