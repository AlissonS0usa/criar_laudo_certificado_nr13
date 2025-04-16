from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class PontoEspessura(Base):
    __tablename__ = "pontos_espessura"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    laudo_id = Column(UUID(as_uuid=True), ForeignKey("laudos_nr13.id"))
    posicao = Column(String)
    espessura = Column(Float)
