from pydantic import BaseModel
from uuid import UUID

class PontoEspessuraBase(BaseModel):
    laudo_id: UUID
    posicao: str
    espessura: float

class PontoEspessuraCreate(PontoEspessuraBase):
    pass

class PontoEspessuraOut(PontoEspessuraBase):
    id: UUID

    class Config:
        orm_mode = True
