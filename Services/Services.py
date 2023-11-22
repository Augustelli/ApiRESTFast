from pydantic import BaseModel

from Models.Models import Autores
from .BaseService import BaseService

class AutoresService(BaseService):
    def __init__(self):
        super().__init__(Autores)

class DomiciliosService(BaseService):
    pass

class LibrosService(BaseService):
    pass

class LocalidadesService(BaseService):
    pass

class PersonasService(BaseService):
    pass