from typing import Optional

from Schemas.BaseSchema import BaseSchema


class LibroSchema(BaseSchema):
    titulo: Optional[str]
    fecha: Optional[int]
    genero: Optional[str]
    paginas: Optional[str]
    persona_id: Optional[int]