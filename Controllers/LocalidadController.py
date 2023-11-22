from fastapi import APIRouter

router_localidades = APIRouter()

@router_localidades.get('/example')
def example_endpoint():
    return 'Endpoint de Localidad'
