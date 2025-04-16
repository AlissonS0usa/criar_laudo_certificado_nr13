from sqlalchemy import Column, String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class CertificadoValvula(Base):
    __tablename__ = "certificados_valvula"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    data_inicio_calibracao = Column(Date, nullable=False)
    data_validade = Column(Date, nullable=False)
    tag_equipamento = Column(String, nullable=False)
    fabricante = Column(String)
    modelo_valvula = Column(String)
    diametro_valvula = Column(String)
    pressao_abertura = Column(Float)
    pressao_fechamento = Column(Float)
    fluido_teste = Column(String)
    unidade_pressao = Column(String)
    foto_valvula = Column(String)
    
    cliente_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"))
    criado_por_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))
