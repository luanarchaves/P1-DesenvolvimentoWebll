import sqlite3


# fazer código para só conectar ao bd se ele existir
# ou retornar erro se não existir
def conectar_bd(nome_bd) -> sqlite3.Connection | None:
    try:
        conn = sqlite3.connect(nome_bd)
        print(f"SQLite aberto com sucesso, versão: {sqlite3.sqlite_version}.")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
