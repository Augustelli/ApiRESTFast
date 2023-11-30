from Repositories.BaseRepositoryImp import BaseRepositoryImpl
from Models.Libros import Libros


class LibrosRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Libros)