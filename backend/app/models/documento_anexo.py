from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class DocumentoAnexo(Base):
    __tablename__ = "documentos_anexos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome = Column(String)
    caminho_arquivo = Column(String)
    referencia_tipo = Column(String)  # 'laudo', 'certificado'
    referencia_id = Column(UUID(as_uuid=True))
