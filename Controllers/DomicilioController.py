from fastapi import APIRouter

route_domicilio = APIRouter()

@route_domicilio.get('/example')
def example_endpoint():
    return 'Endpoint de domicilio'