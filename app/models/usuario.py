from app.database import conectar_bd_mysql

class Usuario:
    def __init__(self, id_usuario=None, nome=None, email=None, senha=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha

    def inserir(self):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nome, email, senha)
                VALUES (%s, %s, %s)
            """, (self.nome, self.email, self.senha))
            conn.commit()
            return cursor.lastrowid  # Retorna o ID do usuário inserido
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def getUsuarios():
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios")
            rows = cursor.fetchall()
            usuarios = [Usuario(*row).__dict__ for row in rows]  # Retorna como dicionários
            return usuarios  # Apenas os dados
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def pegar_por_id(id_usuario):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(*row)  # Retorna apenas os dados do usuário
            else:
                return None  # Usuário não encontrado
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
                UPDATE usuarios
                SET nome = %s, email = %s, senha = %s
                WHERE id_usuario = %s
            """, (self.nome, self.email, self.senha, self.id_usuario))
            conn.commit()
            if cursor.rowcount > 0:
                return self.id_usuario  # Retorna o ID do usuário atualizado
            else:
                return None  # Usuário não encontrado para atualizar
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def deletar(id_usuario):
        conn = conectar_bd_mysql()
        if conn is None:
            return {"error": "Erro de servidor"}
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            if cursor.rowcount > 0:
                return id_usuario  # Retorna o ID do usuário deletado
            else:
                return None  # Usuário não encontrado para deletar
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

# from sqlalchemy import Column, Integer, String

# from database import Base

# class Usuario(Base):
#     __tablename__ = "usuarios"
#     id = Column(Integer, primary_key=True, index=True)
#     nome = Column(String(255), index=True)
#     email = Column(String(100), unique=True, index=True)
#     senha = Column(String)