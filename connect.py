import sqlite3
from app.database import criar_tabelas

try:
    with sqlite3.connect("my.db") as conn:
        print(f"SQLite aberto com sucesso, versão: {sqlite3.sqlite_version}.")

        criar_tabelas.criar_tabela(conn)

except sqlite3.OperationalError as erro:
    print("Falha ao abrir database:", erro)



