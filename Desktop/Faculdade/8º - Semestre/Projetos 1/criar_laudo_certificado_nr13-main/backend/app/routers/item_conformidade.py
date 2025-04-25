from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from app.core.database import SessionLocal
from app.models.item_conformidade import ItemConformidade
from app.schemas.item_conformidade import ItemConformidadeCreate, ItemConformidadeOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

router = APIRouter(tags=["Itens de Conformidade"])


@router.post("/laudos/{laudo_id}/conformidades", response_model=ItemConformidadeOut)
async def criar_item_conformidade(
    laudo_id: UUID,
    item: ItemConformidadeCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        novo_item = ItemConformidade(**item.dict(), laudo_id=laudo_id)
        session.add(novo_item)
        await session.commit()
        await session.refresh(novo_item)
        return novo_item


@router.get("/laudos/{laudo_id}/conformidades", response_model=List[ItemConformidadeOut])
async def listar_itens_conformidade(laudo_id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ItemConformidade).where(ItemConformidade.laudo_id == laudo_id)
        )
        return result.scalars().all()


@router.put("/conformidades/{id}", response_model=ItemConformidadeOut)
async def atualizar_item_conformidade(
    id: UUID,
    dados: ItemConformidadeCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ItemConformidade).where(ItemConformidade.id == id)
        )
        item = result.scalar_one_or_none()
        if not item:
            raise HTTPException(status_code=404, detail="Item não encontrado")

        for key, value in dados.dict().items():
            setattr(item, key, value)

        await session.commit()
        await session.refresh(item)
        return item


@router.delete("/conformidades/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_item_conformidade(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(
            select(ItemConformidade).where(ItemConformidade.id == id)
        )
        item = result.scalar
