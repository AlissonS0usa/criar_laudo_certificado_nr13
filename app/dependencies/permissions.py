from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.models.usuario import Usuario

def is_admin(usuario: Usuario = Depends(get_current_user)):
    if usuario.tipo != "administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso permitido apenas para administradores"
        )
    return usuario

def is_tecnico(usuario: Usuario = Depends(get_current_user)):
    if usuario.tipo != "tecnico":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso permitido apenas para técnicos"
        )
    return usuario
