from fastapi import APIRouter

route_personas = APIRouter()

@route_personas.get('/example')
def example_endpoint():
    return 'Endpoint de personas'