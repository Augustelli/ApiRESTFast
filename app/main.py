import os

from Models.Database import Database
from fastapi import FastAPI
from Controllers.AutorController import AutorController
from Controllers.LocalidadController import LocalidadesController
from Controllers.LibrosController import LibrosController
from Controllers.DomicilioController import DomicilioController
from Controllers.PersonaController import PersonasController
from dotenv import load_dotenv

load_dotenv()
db = Database()
db.create_database()
app = FastAPI()

baseUrl = os.environ.get('BASE_URL')
print(f"Base URL: {baseUrl}")

app.include_router(AutorController().router, prefix=f"{baseUrl}/autores")
app.include_router(LocalidadesController().router, prefix=f"{baseUrl}/localidades")
app.include_router(LibrosController().router, prefix=f"{baseUrl}/libros")
app.include_router(DomicilioController().router, prefix=f"{baseUrl}/domicilios")
app.include_router(PersonasController().router, prefix=f"{baseUrl}/personas")
