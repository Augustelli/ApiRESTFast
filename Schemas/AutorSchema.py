from typing import Optional
from Models.BaseModel import BaseModel


class  AutorSchema(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    biografia: Optional[str]