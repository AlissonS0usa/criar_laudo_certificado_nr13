from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.future import select
from uuid import UUID
from typing import List

from app.core.database import SessionLocal
from app.models.certificado_valvula import CertificadoValvula
from app.schemas.certificado_valvula import CertificadoValvulaCreate, CertificadoValvulaOut
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

router = APIRouter(prefix="/certificados", tags=["Certificados de Válvula"])


@router.post("/", response_model=CertificadoValvulaOut)
async def criar_certificado(
    certificado: CertificadoValvulaCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        novo = CertificadoValvula(**certificado.dict(), criado_por_id=usuario.id)
        session.add(novo)
        await session.commit()
        await session.refresh(novo)
        return novo


@router.get("/", response_model=List[CertificadoValvulaOut])
async def listar_certificados(usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(CertificadoValvula))
        certificados = result.scalars().all()
        return certificados


@router.get("/{id}", response_model=CertificadoValvulaOut)
async def obter_certificado(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(CertificadoValvula).where(CertificadoValvula.id == id))
        cert = result.scalar_one_or_none()
        if not cert:
            raise HTTPException(status_code=404, detail="Certificado não encontrado")
        return cert


@router.put("/{id}", response_model=CertificadoValvulaOut)
async def atualizar_certificado(
    id: UUID,
    dados: CertificadoValvulaCreate,
    usuario: Usuario = Depends(get_current_user)
):
    async with SessionLocal() as session:
        result = await session.execute(select(CertificadoValvula).where(CertificadoValvula.id == id))
        cert = result.scalar_one_or_none()
        if not cert:
            raise HTTPException(status_code=404, detail="Certificado não encontrado")
        
        for key, value in dados.dict().items():
            setattr(cert, key, value)

        await session.commit()
        await session.refresh(cert)
        return cert


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_certificado(id: UUID, usuario: Usuario = Depends(get_current_user)):
    async with SessionLocal() as session:
        result = await session.execute(select(CertificadoValvula).where(CertificadoValvula.id == id))
        cert = result.scalar_one_or_none()
        if not cert:
            raise HTTPException(status_code=404, detail="Certificado não encontrado")
        
        await session.delete(cert)
        await session.commit()
