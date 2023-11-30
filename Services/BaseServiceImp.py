from typing import Generic, TypeVar, List, Type
from sqlalchemy.ext.declarative import DeclarativeMeta

from Models.BaseModel import BaseModel
from Models.Database import Database
from Schemas.BaseSchema import BaseSchema
from Services.BaseService import BaseService

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)

db = Database()

class BaseServiceImp(BaseService):

    def __init__(self, model: Type[BaseModel], schema: Type[BaseSchema], repository ):
        self.model = model
        self.schema = schema
        self.repository = repository
        self.session = db.get_session()

    def find_all(self) -> List[ModelType]:
        model_dicts = self.repository.find_all()
        return [self.schema(**model_dict) for model_dict in model_dicts]

    def find_by_id(self, id: int) -> ModelType:
        model_dict = self.repository.find_by_id(id)
        return self.schema(**model_dict)
    def save(self, schema: BaseSchema):
        model = self.to_model(schema)
        model_dict = self.repository.save(model)
        return self.schema(**model_dict)

    def update(self, schema: BaseSchema):
        model = self.to_model(schema)
        model_dict = self.repository.update(id, model)
        return self.schema(**model_dict)

    def delete(self, id : int):
        self.repository.delete(id)


    def to_model(self, schema: BaseSchema) -> BaseModel:
        model_class = type(self.model) if not callable(self.model) else self.model
        model_instance = model_class(**schema.model_dump())
        return model_instance