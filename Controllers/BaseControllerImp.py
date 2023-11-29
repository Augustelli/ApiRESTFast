from fastapi import APIRouter, HTTPException

from Controllers.BaseController import BaseController

from typing import TypeVar

ModelType = TypeVar("ModelType")
class BaseControllerImp(BaseController):

    def __init__(self, service):
        self.service = service
        self.router = APIRouter()

        @self.router.get("/all")
        def get_all():
            # items = self.service.find_all(skip=skip, limit=limit)
            # return items
            return 'HOLA'

        @self.router.get("/{item_id}")
        def get_by_id(item_id: int):
            # item = self.service.find_by_id(item_id)
            # if item is None:
            #     raise HTTPException(status_code=404, detail="Item not found")
            # return item
            return 'ASJDHASO'

        @self.router.post("/")
        def create(item_data: dict):
            return self.service.save(item_data)


        @self.router.put("/{item_id}")
        def update( item_id: int, updated_data: dict):
            item = self.service.find_by_id(item_id)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return self.service.update(item, updated_data)

        @self.router.delete("/{item_id}")
        def delete(item_id: int):
            item = self.service.find_by_id(item_id)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            self.service.delete(item)

    def get_all(self):
        return self.service.find_all()

    def get_by_id(self, item_id : int):
        return self.service.find_by_id()

    def create(self):
        return self.service.save()

    def update(self):
        return self.service.update()

    def delete(self, item_id : int):
        return self.service.delete()

