from app.models.produto import Produto

class ProdutoController:

    @staticmethod
    async def listar_produtos():
        produtos = Produto.getProdutos()
        if produtos:
            return {"produtos": produtos}
        else:
            return {"message": "Nenhum produto encontrado."}

    @staticmethod
    async def buscar_produto_por_id(id_produto):
        produto = Produto.pegar_por_id(id_produto)
        if produto:
            if isinstance(produto, dict):
                return {"produto": produto}
            return {"produto": produto.__dict__}
        else:
            return {"message": "Produto não encontrado."}

    @staticmethod
    async def criar_produto(nome, preco, estoque, categoria):
        produto = Produto(nome=nome, preco=preco, estoque=estoque, categoria=categoria)
        produto_id = produto.inserir()
        if isinstance(produto_id, dict) and "error" in produto_id:
            return {"error": produto_id["error"]}
        return produto_id

    @staticmethod
    async def atualizar_produto(produto: Produto):
        produto_existente = Produto.pegar_por_id(produto.id_produto)
        if not produto_existente:
            return {"message": "Produto não encontrado."}
        produto_existente = produto
        produto_id = produto_existente.atualizar()
        if produto_id:
            return {"message": "Produto atualizado com sucesso.", "id_produto": produto_id}
        else:
            return {"message": "Erro ao atualizar produto."}

    @staticmethod
    async def deletar_produto(id_produto):
        produto_id = Produto.deletar(id_produto)
        if produto_id:
            return {"message": "Produto deletado com sucesso.", "id_produto": produto_id}
        else:
            return {"message": "Erro ao deletar produto."}