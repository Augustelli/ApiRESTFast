import uvicorn

from Models.Database import Database
from fastapi import FastAPI
from Controllers.LocalidadController import router_localidades
from Controllers.PersonaController import route_personas
from Controllers.DomicilioController import route_domicilio
from Controllers.LibrosController import route_libros
from Controllers.AutorController import route_autores


db = Database()
db.create_database()


app = FastAPI()
baseUrl = '/api/v1/apiRestFake/'
app.include_router(router_localidades, prefix=f"{baseUrl}localidades", tags=['localidades'])
app.include_router(route_personas, prefix=f"{baseUrl}personas", tags=['personas'])
app.include_router(route_domicilio, prefix=f"{baseUrl}domicilios", tags=['domicilios'])
app.include_router(route_libros, prefix=f"{baseUrl}libros", tags=['libros'])
app.include_router(route_autores, prefix=f"{baseUrl}autores", tags=['autores'])

uvicorn.run(app, host="127.0.0.1", port=8000)
