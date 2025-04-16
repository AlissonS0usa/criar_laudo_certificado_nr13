from sqlalchemy import Column, String, Float, Integer, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.models.base import Base

class LaudoNR13(Base):
    __tablename__ = "laudos_nr13"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    cliente_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"))
    criado_por_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))

    tag_equipamento = Column(String)
    foto_equipamento = Column(String)

    data_inicio_inspecao = Column(Date)
    tipo_inspecao = Column(String)
    numero_serie = Column(String)
    modelo = Column(String)
    fabricante = Column(String)
    ano_fabricacao = Column(Integer)

    temperatura_max_projeto = Column(Float)
    codigo_construcao = Column(String)
    pmta_fabricante = Column(Float)
    pth_fabricante = Column(Float)

    fluido_servico = Column(String)
    volume = Column(Float)
    setor = Column(String)
    tipo_vaso = Column(String)
    classe_fluido = Column(String)

    foto_pintura_revestimento = Column(String)
    foto_placa_identificacao = Column(String)
    foto_adesivo_categoria = Column(String)
    foto_valvula_seguranca = Column(String)
    foto_manometro = Column(String)
    foto_medicao_espessura = Column(String)

    observacoes = Column(String)
    comprimento = Column(Float)
    diametro_vaso = Column(Float)
    data_proxima_inspecao = Column(Date)
