from Controllers.BaseControllerImp import BaseControllerImp

class PersonasController(BaseControllerImp):
    def __init__(self):
        super().__init__('PersonasService')