from typing import Optional
from pydantic import BaseModel, field_validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')
        return value



cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algoritimos e Lógica de Programção', aulas=52, horas=109),
]