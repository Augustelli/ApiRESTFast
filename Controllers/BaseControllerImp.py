from fastapi import APIRouter, HTTPException

from Controllers.BaseController import BaseController
from Services.BaseServiceImp import BaseService

from typing import Type, TypeVar

ModelType = TypeVar("ModelType")

router = APIRouter()
class BaseControllerImp(BaseController):
    def __init__(self, service):
        self.service = service
        self.router = router


    @router.get("/all")
    def get_all(self, skip: int = 0, limit: int = 10):
        # items = self.service.find_all(skip=skip, limit=limit)
        # return items
        return 'HOLA'

    @router.get("/{item_id}")
    def get_by_id(self, item_id: int):
        # item = self.service.find_by_id(item_id)
        # if item is None:
        #     raise HTTPException(status_code=404, detail="Item not found")
        # return item
        return 'ASJDHASO'

    @router.post("/")
    def create(self, item_data: dict):
        return self.service.save(item_data)


    @router.put("/{item_id}")
    def update(self, item_id: int, updated_data: dict):
        item = self.service.find_by_id(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return self.service.update(item, updated_data)

    @router.delete("/{item_id}")
    def delete(self, item_id: int):
        item = self.service.find_by_id(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        self.service.delete(item)
        
    @property
    def router(self):
        return router