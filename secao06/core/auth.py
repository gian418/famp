from datetime import timedelta, datetime
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from configs import settings
from secao06.core.security import verificar_senha
from secao06.models.usuario_model import UsuarioModel

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login",
)

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).where(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario

 def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
     sp = timezone('America/Sao_Paulo')
     expira = datetime.now(tz=sp) + tempo_vida

     payload = {
         "type": tipo_token,
         "exp": expira,
         "iat": datetime.now(tz=sp),
         "sub": sub
     }

     return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

 def criar_token_acesso(sub: str) -> str:
     return _criar_token(
         tipo_token="access_token",
         tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
         sub=sub
     )