from fastapi import APIRouter

base_url = "traer"
autores_endpoint = APIRouter()

@autores_endpoint.get(f"{base_url}")
def get_autores():
    return 'AUTORES ENDPOINT'
