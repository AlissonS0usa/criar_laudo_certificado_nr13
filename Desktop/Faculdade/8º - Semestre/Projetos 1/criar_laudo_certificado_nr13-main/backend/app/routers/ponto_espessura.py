from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from app.core.database import SessionLocal
from app.models.ponto_espessura import PontoEspessura
from app.schemas.ponto_espessura import PontoEspessuraCreate, PontoEspessuraOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

router = APIRouter(tags=["Pontos de Espessura"])


@router.post("/laudos/{laudo_id}/espessuras", response_model=PontoEspessuraOut)
async def criar_ponto(
    laudo_id: UUID,
    ponto: PontoEspessuraCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        novo = PontoEspessura(**ponto.dict(), laudo_id=laudo_id)
        session.add(novo)
        await session.commit()
        await session.refresh(novo)
        return novo


@router.get("/laudos/{laudo_id}/espessuras", response_model=List[PontoEspessuraOut])
async def listar_pontos(laudo_id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(
            select(PontoEspessura).where(PontoEspessura.laudo_id == laudo_id)
        )
        return result.scalars().all()


@router.put("/espessuras/{id}", response_model=PontoEspessuraOut)
async def atualizar_ponto(
    id: UUID,
    dados: PontoEspessuraCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        result = await session.execute(
            select(PontoEspessura).where(PontoEspessura.id == id)
        )
        ponto = result.scalar_one_or_none()
        if not ponto:
            raise HTTPException(status_code=404, detail="Ponto não encontrado")

        for key, value in dados.dict().items():
            setattr(ponto, key, value)

        await session.commit()
        await session.refresh(ponto)
        return ponto


@router.delete("/espessuras/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_ponto(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(
            select(PontoEspessura).where(PontoEspessura.id == id)
        )
        ponto = result.scalar_one_or_none()
        if not ponto:
            raise HTTPException(status_code=404, detail="Ponto não encontrado")

        await session.delete(ponto)
        await session.commit()
