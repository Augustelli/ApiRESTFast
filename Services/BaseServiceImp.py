from typing import Generic, TypeVar, List
from sqlalchemy.ext.declarative import DeclarativeMeta
from Models.Database import Database
from Services.BaseService import BaseService

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)

db = Database()

class BaseServiceImp(BaseService):

    def __init__(self, model: ModelType, schema ):
        self.model = model
        self.schema = schema
        self.session = db.get_session()

    def find_all(self) -> List[ModelType]:
        return self.session.query(self.model).all()

    def find_by_id(self, id: int) -> ModelType:
        return self.session.query(self.model).filter(self.model.id == id).first()

    def save(self, instance: ModelType):
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def update(self, instance: ModelType):
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: ModelType):
        self.session.delete(instance)
        self.session.commit()
