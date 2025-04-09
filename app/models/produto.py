from app.database import conectar_bd_mysql

class Produto:
    def __init__(self, id_produto=None, nome=None, preco=None, estoque=None, categoria=None):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria

    def inserir(self):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, preco, estoque, categoria)
                VALUES (%s, %s, %s, %s)
            """, (self.nome, self.preco, self.estoque, self.categoria))
            conn.commit()
            return cursor.lastrowid  # Retorna o ID do produto inserido
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def getProdutos():
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM produtos")
            rows = cursor.fetchall()
            produtos = [Produto(*row).__dict__ for row in rows]  # Retorna como dicionários
            return produtos
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def pegar_por_id(id_produto):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM produtos WHERE id_produto = %s", (id_produto,))
            row = cursor.fetchone()
            if row:
                return Produto(*row)  # Retorna apenas os dados do produto
            else:
                return None  # Produto não encontrado
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    def atualizar(self):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE produtos
                SET nome = %s, preco = %s, estoque = %s, categoria = %s
                WHERE id_produto = %s
            """, (self.nome, self.preco, self.estoque, self.categoria, self.id_produto))
            conn.commit()
            if cursor.rowcount > 0:
                return self.id_produto  # Retorna o ID do produto atualizado
            else:
                return None  # Produto não encontrado para atualizar
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def deletar(id_produto):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM produtos WHERE id_produto = %s", (id_produto,))
            conn.commit()
            if cursor.rowcount > 0:
                return id_produto  # Retorna o ID do produto deletado
            else:
                return None  # Produto não encontrado para deletar
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()