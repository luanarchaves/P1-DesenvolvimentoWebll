from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

db_config = {
    'host': os.getenv("BD_HOST"),
    'user': os.getenv("BD_USER"),
    'password': os.getenv("BD_PASSWORD"),
    'database': os.getenv("BD_NAME"),
    'port': int(os.getenv("BD_PORT"))
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("\n Tabelas encontradas no banco:")
    for table in tables:
        print(f" - {table[0]}")

    cursor.close()
    conn.close()

except mysql.connector.Error as erro:
    print("\n Erro ao conectar com o banco de dados:")
    print(erro)
