from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_rauter

app: FastAPI = FastAPI(title='Curso API - FastAPI e SQLModel', version='1.0.0')
app.include_router(api_rauter, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, log_level='info')