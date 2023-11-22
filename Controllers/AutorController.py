from fastapi import APIRouter

route_autores = APIRouter()

@route_autores.get("/example")
async def get_autores():
    return 'AUTORES ENDPOINT'
