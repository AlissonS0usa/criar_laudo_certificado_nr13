from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ItemConformidadeBase(BaseModel):
    laudo_id: UUID
    descricao: str
    conforme: bool
    observacao: Optional[str]

class ItemConformidadeCreate(ItemConformidadeBase):
    pass

class ItemConformidadeOut(ItemConformidadeBase):
    id: UUID

    class Config:
        orm_mode = True
