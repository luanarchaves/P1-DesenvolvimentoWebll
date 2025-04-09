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
        if not nome or not preco or not estoque or not categoria:
            return {"error": "Todos os campos são obrigatórios."}
        if not isinstance(nome, str) or len(nome) < 3:
            return {"error": "Nome deve ser uma string com pelo menos 3 caracteres."}
        if not isinstance(preco, (int, float)) or preco <= 0:
            return {"error": "Preço deve ser um número positivo."}
        if not isinstance(estoque, int) or estoque < 0:
            return {"error": "Estoque deve ser um número inteiro não negativo."}
        if not isinstance(categoria, str) or len(categoria) < 3:
            return {"error": "Categoria deve ser uma string com pelo menos 3 caracteres."}
        produto = Produto(nome=nome, preco=preco, estoque=estoque, categoria=categoria)
        produto_id = produto.inserir()
        if isinstance(produto_id, dict) and "error" in produto_id:
            return {"error": produto_id["error"]}
        return produto_id

    @staticmethod
    async def atualizar_produto(produto: Produto):
        if not produto.nome or not produto.preco or not produto.estoque or not produto.categoria:
            return {"error": "Todos os campos são obrigatórios."}
        if not isinstance(produto.preco, (int, float)) or produto.preco <= 0:
            return {"error": "Preço deve ser um número positivo."}
        if not isinstance(produto.estoque, int) or produto.estoque < 0:
            return {"error": "Estoque deve ser um número inteiro não negativo."}
        if not isinstance(produto.categoria, str) or len(produto.categoria) < 3:
            return {"error": "Categoria deve ser uma string com pelo menos 3 caracteres."}
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
        if not isinstance(id_produto, int) or id_produto <= 0:
            return {"error": "ID do produto deve ser um número inteiro positivo."}
        produto_id = Produto.deletar(id_produto)
        if produto_id:
            return {"message": "Produto deletado com sucesso.", "id_produto": produto_id}
        else:
            return {"message": "Erro ao deletar produto."}