from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(256), nullable=False)
    sobrenome: str = Column(String(256), nullable=False)
    email: str = Column(String(256), nullable=False, unique=True, index=True)
    eh_admin: bool = Column(Boolean, default=False)
    senha: str = Column(String(256), nullable=False)
    artigos = relationship(
        "ArtigoModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )