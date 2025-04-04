import sqlite3

def criar_tabela(conn):

    sql_statements = [ 
        """CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL, 
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                cep TEXT NOT NULL CHECK(LENGTH(cep) = 8),
                rua TEXT NOT NULL,
                numero_residencia INTEGER NOT NULL,
                complemento TEXT,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL CHECK(LENGTH(estado) = 2)
            );""",

        """CREATE TABLE IF NOT EXISTS produtos (
                id_produtos INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT UNIQUE NOT NULL CHECK(LENGTH(nome) >= 3),
                preco_unitario REAL NOT NULL CHECK(preco_unitario > 0),
                qtd_estoque INTEGER NOT NULL CHECK(qtd_estoque >= 0),
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
