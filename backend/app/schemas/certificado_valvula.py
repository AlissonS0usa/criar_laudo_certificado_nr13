from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional

class CertificadoValvulaBase(BaseModel):
    data_inicio_calibracao: date
    data_validade: date
    tag_equipamento: str
    fabricante: Optional[str]
    modelo_valvula: Optional[str]
    diametro_valvula: Optional[str]
    pressao_abertura: Optional[float]
    pressao_fechamento: Optional[float]
    fluido_teste: Optional[str]
    unidade_pressao: Optional[str]
    foto_valvula: Optional[str]
    cliente_id: UUID

class CertificadoValvulaCreate(CertificadoValvulaBase):
    pass

class CertificadoValvulaOut(CertificadoValvulaBase):
    id: UUID
    criado_por_id: UUID

    class Config:
        orm_mode = True
