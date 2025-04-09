// Script para criar o banco de dados e as tabelas do projeto
CREATE database p1;

use p1;

CREATE TABLE IF NOT EXISTS usuarios 
(
	id_usuario INT AUTO_INCREMENT PRIMARY KEY, 
	nome VARCHAR(255) NOT NULL, 
	email VARCHAR(255) UNIQUE NOT NULL,
	senha VARCHAR(255) NOT NULL
);
                
CREATE TABLE IF NOT EXISTS produtos 
(
	id_produtos INT AUTO_INCREMENT PRIMARY KEY, 
	nome VARCHAR(255) UNIQUE NOT NULL CHECK(CHAR_LENGTH(nome) >= 3),
	preco_unitario DECIMAL(10, 2) NOT NULL CHECK(preco_unitario > 0),
	qtd_estoque INT NOT NULL CHECK(qtd_estoque >= 0),
	categoria VARCHAR(255)
);
