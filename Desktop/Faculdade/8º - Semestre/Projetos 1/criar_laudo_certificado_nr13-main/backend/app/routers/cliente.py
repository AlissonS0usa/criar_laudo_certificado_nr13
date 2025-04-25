from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from app.schemas.cliente import ClienteCreate, ClienteOut
from app.models.cliente import Cliente
from app.core.database import SessionLocal
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/", response_model=ClienteOut)
async def criar_cliente(
    cliente: ClienteCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        novo_cliente = Cliente(**cliente.dict(), criado_por_id=usuario.id)
        session.add(novo_cliente)
        await session.commit()
        await session.refresh(novo_cliente)
        return novo_cliente


#lista todos os clientes
@router.get("/", response_model=List[ClienteOut])
async def listar_clientes(usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(Cliente))
        #pega todos os objetos Cliente
        clientes = result.scalars().all()
        return clientes

#busca um cliente pelo id.
@router.get("/{id}", response_model=ClienteOut)
async def obter_cliente(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(Cliente).where(Cliente.id == id))
        cliente = result.scalar_one_or_none()
        if cliente is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return cliente


#atualiza cliente
@router.put("/{id}", response_model=ClienteOut)
async def atualizar_cliente(
    id: UUID,
    dados: ClienteCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        result = await session.execute(select(Cliente).where(Cliente.id == id))
        cliente = result.scalar_one_or_none()
        if cliente is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

        for key, value in dados.dict().items():
            #define dinamicamente o valor de um atributo de um objeto: cliente.nome = "am engenharia"
            setattr(cliente, key, value)

        await session.commit()
        await session.refresh(cliente)
        return cliente

#deleta cliente
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(Cliente).where(Cliente.id == id))
        cliente = result.scalar_one_or_none()
        if cliente is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        
        await session.delete(cliente)
        await session.commit()

