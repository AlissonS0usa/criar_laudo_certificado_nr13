from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional

class LaudoNR13Base(BaseModel):
    cliente_id: UUID
    tag_equipamento: Optional[str]
    foto_equipamento: Optional[str]
    data_inicio_inspecao: Optional[date]
    tipo_inspecao: Optional[str]
    numero_serie: Optional[str]
    modelo: Optional[str]
    fabricante: Optional[str]
    ano_fabricacao: Optional[int]
    temperatura_max_projeto: Optional[float]
    codigo_construcao: Optional[str]
    pmta_fabricante: Optional[float]
    pth_fabricante: Optional[float]
    fluido_servico: Optional[str]
    volume: Optional[float]
    setor: Optional[str]
    tipo_vaso: Optional[str]
    classe_fluido: Optional[str]
    foto_pintura_revestimento: Optional[str]
    foto_placa_identificacao: Optional[str]
    foto_adesivo_categoria: Optional[str]
    foto_valvula_seguranca: Optional[str]
    foto_manometro: Optional[str]
    foto_medicao_espessura: Optional[str]
    observacoes: Optional[str]
    comprimento: Optional[float]
    diametro_vaso: Optional[float]
    data_proxima_inspecao: Optional[date]

class LaudoNR13Create(LaudoNR13Base):
    pass

class LaudoNR13Out(LaudoNR13Base):
    id: UUID
    criado_por_id: UUID

    class Config:
        orm_mode = True
