from Repositories.BaseRepositoryImp import BaseRepositoryImpl
from Models.Domicilios import Domicilios


class DomiciliosRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Domicilios)