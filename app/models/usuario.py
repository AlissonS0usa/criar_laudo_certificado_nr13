from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

#Módulo usado para definir valores fixos (enums).
import enum

#str, enum.Enum: Faz com que os valores do enum sejam tratados como strings
class TipoUsuario(str, enum.Enum):
    administrador = "administrador"
    tecnico = "tecnico"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome_completo = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    tipo = Column(Enum(TipoUsuario), nullable=False)
