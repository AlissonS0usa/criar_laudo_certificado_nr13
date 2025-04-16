from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Compara a senha digitada (senha) com a senha criptografada armazenada no banco (senha_hash)
def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)

#Recebe a senha e retorna ela criptografada com bcrypt
def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

# Cria um token JWT com os dados informados e tempo de expiração
def criar_token_dados(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy() #copia os dados  pra não modificar o original
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)) #se o tempo de expiração não for passado, usa o padrão das configurações
    to_encode.update({"exp": expire})    # adiciona o tempo de expiração ao token
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

#verifica se um token é válido e retorna os dados contidos nele 
def verificar_token(token: str):
    try:
        #tenta decodificar o token com a chave e algoritmo configurados
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
