from fastapi import APIRouter
from app.controllers import UsuarioController
from app.models import Usuario, UsuarioSchema

usuarioRouter = APIRouter()

@usuarioRouter.get("/")
async def listar_usuarios():
    usuarios = await UsuarioController.listar_usuarios()
    return usuarios

@usuarioRouter.get("/{id_usuario}")
async def buscar_usuario_por_id(id_usuario: int):
    usuario = await UsuarioController.buscar_usuario_por_id(id_usuario)
    return usuario

@usuarioRouter.post("/")
async def criar_usuario(usuario: UsuarioSchema):
    usuario_id = await UsuarioController.criar_usuario(usuario.nome, usuario.email, usuario.senha)
    return usuario_id

@usuarioRouter.put("/{id}")
async def atualizar_usuario(id: int, usuarioReq: UsuarioSchema):
    usuario_novo = Usuario(id_usuario=id, nome=usuarioReq.nome, email=usuarioReq.email, senha=usuarioReq.senha)
    resposta = await UsuarioController.atualizar_usuario(usuario_novo)
    return resposta

@usuarioRouter.delete("/{id}")
async def deletar_usuario(id: int):
    usuario_id = await UsuarioController.deletar_usuario(id)
    return usuario_id

