import os

from Controllers.BaseControllerImp import BaseControllerImp, router
from Services.Services import AutoresService
from dotenv import load_dotenv

load_dotenv()
autor_service = AutoresService()

class AutorController(BaseControllerImp):
    def __init__(self):
        super().__init__(autor_service)
        self.router.include_router(self.router, prefix=f"/autores")

