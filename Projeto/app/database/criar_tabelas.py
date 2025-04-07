import sqlite3

def criar_tabela(conn):

    sql_statements = [ 
        """CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL, 
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            );""",

        """CREATE TABLE IF NOT EXISTS produtos (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT UNIQUE NOT NULL CHECK(LENGTH(nome) >= 3),
                preco REAL NOT NULL CHECK(preco > 0),
                estoque INTEGER NOT NULL CHECK(estoque >= 0),
                categoria TEXT
            );"""
    ]

    cursor = conn.cursor()
    try:
        for statement in sql_statements:
            cursor.execute(statement)
        conn.commit()
        print("Tabelas criadas com sucesso.")
    except Exception as erro:
        print("Erro ao criar tabelas:", erro)
    finally:
        cursor.close()
