from fastapi import APIRouter
from app.controllers import ProdutoController
from app.models import Produto
from app.models import ProdutoSchema

produtoRouter = APIRouter()

@produtoRouter.get("/")
async def listar_produtos():
    produtos = await ProdutoController.listar_produtos()
    return produtos

@produtoRouter.get("/{id_produto}")
async def buscar_produto_por_id(id_produto: int):
    produto = await ProdutoController.buscar_produto_por_id(id_produto)
    return produto

@produtoRouter.post("/")
async def criar_produto(produto: ProdutoSchema):
    produto_id = await ProdutoController.criar_produto(produto.nome, produto.preco, produto.estoque, produto.categoria)
    if isinstance(produto_id, dict) and "error" in produto_id:
        return {"error": produto_id["error"]}
    return {"message": "Produto criado com sucesso.", "id_produto": produto_id}

@produtoRouter.put("/{id}")
async def atualizar_produto(produto: ProdutoSchema, id: int):
    produto_novo = Produto(id_produto=id, nome=produto.nome, preco=produto.preco, estoque=produto.estoque, categoria=produto.categoria)
    resposta = await ProdutoController.atualizar_produto(produto_novo)
    return resposta

@produtoRouter.delete("/{id}")
async def deletar_produto(id: int):
    produto_id = await ProdutoController.deletar_produto(id)
    return produto_id

