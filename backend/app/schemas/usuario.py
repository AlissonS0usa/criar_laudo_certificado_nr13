from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum
from typing import Optional

class TipoUsuario(str, Enum):
    administrador = "administrador"
    tecnico = "tecnico"

class UsuarioBase(BaseModel):
    nome_completo: str
    email: EmailStr
    tipo: TipoUsuario

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioOut(UsuarioBase):
    id: UUID

    class Config:
        orm_mode = True
