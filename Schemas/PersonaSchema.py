from typing import Optional

from Schemas.BaseSchema import BaseSchema


class PersonasSchema(BaseSchema):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[int] = None
    domicilio_id: Optional[int] = None