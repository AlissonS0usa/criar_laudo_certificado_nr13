from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from app.core.database import SessionLocal
from app.models.laudo_nr13 import LaudoNR13
from app.schemas.laudo_nr13 import LaudoNR13Create, LaudoNR13Out
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

router = APIRouter(prefix="/laudos", tags=["Laudos NR13"])


@router.post("/", response_model=LaudoNR13Out)
async def criar_laudo(
    laudo: LaudoNR13Create,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        novo = LaudoNR13(**laudo.dict(), criado_por_id=usuario.id)
        session.add(novo)
        await session.commit()
        await session.refresh(novo)
        return novo


@router.get("/", response_model=List[LaudoNR13Out])
async def listar_laudos(usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(LaudoNR13))
        laudos = result.scalars().all()
        return laudos


@router.get("/{id}", response_model=LaudoNR13Out)
async def obter_laudo(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(LaudoNR13).where(LaudoNR13.id == id))
        laudo = result.scalar_one_or_none()
        if not laudo:
            raise HTTPException(status_code=404, detail="Laudo não encontrado")
        return laudo


@router.put("/{id}", response_model=LaudoNR13Out)
async def atualizar_laudo(
    id: UUID,
    dados: LaudoNR13Create,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        result = await session.execute(select(LaudoNR13).where(LaudoNR13.id == id))
        laudo = result.scalar_one_or_none()
        if not laudo:
            raise HTTPException(status_code=404, detail="Laudo não encontrado")
        
        for key, value in dados.dict().items():
            setattr(laudo, key, value)

        await session.commit()
        await session.refresh(laudo)
        return laudo


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_laudo(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(LaudoNR13).where(LaudoNR13.id == id))
        laudo = result.scalar_one_or_none()
        if not laudo:
            raise HTTPException(status_code=404, detail="Laudo não encontrado")
        
        await session.delete(laudo)
        await session.commit()
