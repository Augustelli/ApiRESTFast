from typing import Optional

from Schemas.BaseSchema import BaseSchema


class DomicilioSchema(BaseSchema):

    calle: Optional[str]
    numero: Optional[int]
    localidad_id: Optional[str]
