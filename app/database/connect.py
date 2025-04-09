import sqlite3
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

def conectar_bd_mysql():
    """
    Conecta ao banco de dados MySQL.
    Retorna a conexão se bem-sucedida ou None em caso de erro.
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("BD_HOST"),
            user=os.getenv("BD_USER"),
            password=os.getenv("BD_PASSWORD"),
            database=os.getenv("BD_MYSQL")
        )
        if conn.is_connected():
            print(f"MySQL conectado com sucesso! Versão: {conn.get_server_info()}")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados MySQL: {e}")
        return None