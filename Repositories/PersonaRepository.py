from Repositories.BaseRepositoryImp import BaseRepositoryImpl
from Models.Personas import Personas


class PersonaRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Personas)
