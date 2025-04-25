from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class ItemConformidade(Base):
    __tablename__ = "itens_conformidade"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    laudo_id = Column(UUID(as_uuid=True), ForeignKey("laudos_nr13.id"))
    descricao = Column(String)
    conforme = Column(Boolean)
    observacao = Column(String)
