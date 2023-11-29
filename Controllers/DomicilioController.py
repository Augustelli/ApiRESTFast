from fastapi import APIRouter

from Controllers.BaseControllerImp import BaseControllerImp


class DomicilioController(BaseControllerImp):

    def __init__(self):
        super().__init__('DomicilioService')