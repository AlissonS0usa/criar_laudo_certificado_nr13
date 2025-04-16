from pydantic import BaseModel
from uuid import UUID

class DocumentoAnexoBase(BaseModel):
    nome: str
    caminho_arquivo: str
    referencia_tipo: str
    referencia_id: UUID

class DocumentoAnexoCreate(DocumentoAnexoBase):
    pass

class DocumentoAnexoOut(DocumentoAnexoBase):
    id: UUID

    class Config:
        orm_mode = True
