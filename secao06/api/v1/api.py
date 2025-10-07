from fastapi import APIRouter
from api.v1.endpoints import artigo
from api.v1.endpoints import usuario


api_router = APIRouter()
api_router.include_router(artigo.router, tags=["artigos"], prefix="/artigos")
api_router.include_router(usuario.router, tags=["usuarios"], prefix="/usuarios")