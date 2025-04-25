from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ClienteBase(BaseModel):
    nome: str
    razao_social: Optional[str]
    nome_fantasia: Optional[str]
    cnpj: str
    cep: Optional[str]
    logradouro: Optional[str]
    numero: int
    cidade: Optional[str]
    estado: Optional[str]
    contatos: Optional[str]

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: UUID
    criado_por_id: UUID

    class Config:
        #Permite que o Pydantic leia dados diretamente de objetos ORM (como SQLAlchemy) em vez de apenas dicionários.
        orm_mode = True
