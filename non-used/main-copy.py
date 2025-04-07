from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session

import uvicorn

from app.database import get_db, SessionLocal, engine, Base
from app import Usuario
from app.models import UsuarioSchema, UsuarioRepository, UsuarioListResponseSchema, UsuarioRequestSchema
Base.metadata.create_all(bind=engine)  # Cria as tabelas no banco de dados

router = APIRouter()
app = FastAPI()

@router.get("/usuarios", response_model=UsuarioListResponseSchema)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = UsuarioRepository.find_all(db)
    return usuarios

@router.get("/usuarios/{id_usuario}", response_model=UsuarioSchema)
def listar_usuario_por_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = UsuarioRepository.find_by_id(id_usuario, db)
    if usuario:
        return usuario
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")


@router.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=UsuarioSchema)
def criar_usuario(usuario: UsuarioRequestSchema,
                        db: Session = Depends(get_db)):
    novo_usuario = Usuario(**usuario.dict())
    UsuarioRepository.save(novo_usuario, db)
    return novo_usuario

@router.put("/usuarios/{id_usuario}", response_model=UsuarioSchema)
def atualizar_usuario(id_usuario: int, usuario: UsuarioRequestSchema,
                             db: Session = Depends(get_db)):
    usuario_existente = UsuarioRepository.find_by_id(id_usuario, db)
    if not usuario_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    usuario_atualizado = Usuario(**usuario.dict(), id=id_usuario)
    UsuarioRepository.update(usuario_atualizado, db)
    return usuario_atualizado

@router.delete("/usuarios/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario_existente = UsuarioRepository.find_by_id(id_usuario, db)
    if not usuario_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    UsuarioRepository.delete(usuario_existente, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


app.include_router(router)    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
