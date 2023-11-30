from Repositories.BaseRepositoryImp import BaseRepositoryImpl
from Models.Localidades import Localidades


class LocalidadesRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Localidades)