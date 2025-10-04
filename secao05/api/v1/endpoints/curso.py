from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )
    db.add(novo_curso)
    await db.commit()
    return novo_curso


@router.get('/', response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos
    
@router.get('/{curso_id}', response_model=CursoModel)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        return curso
    
@router.put('/{curso_id}', response_model=CursoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(
    curso_id: int,
    curso: CursoModel,
    db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_db = result.scalar_one_or_none()
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

        curso_db.titulo = curso.titulo
        curso_db.aulas = curso.aulas
        curso_db.horas = curso.horas

        session.add(curso_db)
        await session.commit()
        await session.refresh(curso_db)
        return curso_db


@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_db = result.scalar_one_or_none()
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

        await session.delete(curso_db)
        await session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)        
       