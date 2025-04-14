from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.models.usuario import Usuario
from app.core.database import SessionLocal
from app.core.security import gerar_hash_senha, verificar_senha, criar_token_dados
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UsuarioOut)
async def register(usuario: UsuarioCreate):
    async with SessionLocal() as session:
        result = await session.execute(select(Usuario).where(Usuario.email == usuario.email))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        
        novo_usuario = Usuario(
            nome_completo=usuario.nome_completo,
            email=usuario.email,
            senha=gerar_hash_senha(usuario.senha),
            tipo=usuario.tipo
        )
        session.add(novo_usuario)
        await session.commit()
        await session.refresh(novo_usuario)
        return novo_usuario

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    async with SessionLocal() as session:
        result = await session.execute(select(Usuario).where(Usuario.email == form.username))
        usuario = result.scalar_one_or_none()

        if not usuario or not verificar_senha(form.password, usuario.senha):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token = criar_token_dados({"sub": usuario.email})
        return {"access_token": token, "token_type": "bearer"}
