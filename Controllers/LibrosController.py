from fastapi import APIRouter

route_libros = APIRouter()

@route_libros.get('/example')
def example_endpoint():
    return 'Endpoint de libros'