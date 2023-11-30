from Repositories.BaseRepositoryImp import BaseRepositoryImpl
from Models.Autores import Autores


class AutoresRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Autores)