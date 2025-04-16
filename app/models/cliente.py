from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome = Column(String, nullable=False)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    cnpj = Column(String)
    cep = Column(String)
    logradouro = Column(String)
    numero = Column(Integer, nullable=False)
    cidade = Column(String)
    estado = Column(String)
    contatos = Column(String)
    criado_por_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))
