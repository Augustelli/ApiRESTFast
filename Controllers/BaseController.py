# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from Services.BaseService import BaseService
#
# from typing import Type, TypeVar
#
# ModelType = TypeVar("ModelType")
#
#
# class BaseController:
#     def __init__(self, service: Type[BaseService[ModelType]], router: APIRouter = None):
#         self.service = service
#         self.router = router or APIRouter()
#
#     def get_router(self):
#         return self.router
#
#     def get_all(self, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#         items = self.service(db).find_all(skip=skip, limit=limit)
#         return items
#
#     def get_by_id(self, item_id: int, db: Session = Depends(get_db)):
#         item = self.service(db).find_by_id(item_id)
#         if item is None:
#             raise HTTPException(status_code=404, detail="Item not found")
#         return item
#
#     def create(self, item_data: dict, db: Session = Depends(get_db)):
#         return self.service(db).save(item_data)
#
#     def update(self, item_id: int, updated_data: dict, db: Session = Depends(get_db)):
#         item = self.service(db).find_by_id(item_id)
#         if item is None:
#             raise HTTPException(status_code=404, detail="Item not found")
#         return self.service(db).update(item, updated_data)
#
#     def delete(self, item_id: int, db: Session = Depends(get_db)):
#         item = self.service(db).find_by_id(item_id)
#         if item is None:
#             raise HTTPException(status_code=404, detail="Item not found")
#         return self.service(db).delete(item)
