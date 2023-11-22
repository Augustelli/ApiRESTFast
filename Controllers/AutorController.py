from fastapi import APIRouter, HTTPException

from Models.Models import Autores
from Services.Services import AutoresService

route_autores = APIRouter()
autor_service = AutoresService()

@route_autores.get("/example")
def get_all(skip: int = 0, limit: int = 10):
    items = autor_service.find_all(skip=skip, limit=limit)
    return items

@route_autores.get('/{item_id}')
def get_by_id( item_id: int):
    item = autor_service.find_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def create( item_data: dict):
    return autor_service.save(item_data)


def update( item_id: int, updated_data: dict):
    item = autor_service.find_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return autor_service.update(item, updated_data)


def delete( item_id: int):
    item = autor_service.find_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return autor_service.delete(item)

