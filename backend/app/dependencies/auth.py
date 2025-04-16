from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verificar_token
from app.models.usuario import Usuario
from app.core.database import SessionLocal
from sqlalchemy.future import select

#define o esquema de autenticação: o token será extraído do header "Authorization: Bearer <token>"
# a URL 'tokenUrl="login"' indica onde o usuário deve enviar as credenciais para obter esse token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#essa função será usada como dependência em rotas protegidas
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    
    async with SessionLocal() as session:
        result = await session.execute(select(Usuario).where(Usuario.email == payload["sub"]))
        usuario = result.scalar_one_or_none()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return usuario
