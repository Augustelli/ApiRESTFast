from pydantic import BaseModel

from .BaseServiceImp import BaseService

class AutoresService(BaseService):
    def __init__(self):
        super().__init__()

class DomiciliosService(BaseService):
    pass

class LibrosService(BaseService):
    pass

class LocalidadesService(BaseService):
    pass

class PersonasService(BaseService):
    pass