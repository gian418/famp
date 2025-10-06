from v1.endpoints import curso
from fastapi import APIRouter

api_rauter = APIRouter()
api_rauter.include_router(curso.router, prefix="/cursos", tags=["cursos"])