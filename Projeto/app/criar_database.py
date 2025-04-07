from app.database import criar_tabela
import sqlite3

def criar_db():

    try:
        conn = sqlite3.connect("p1.db")
        print(f"SQLite aberto com sucesso, versão: {sqlite3.sqlite_version}.")
        criar_tabela(conn)
    except sqlite3.Error as e:
        print(f"Banco de dados já existe")
    finally:
        if conn:
            conn.close()

