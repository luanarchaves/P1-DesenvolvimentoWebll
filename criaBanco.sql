create database p1;

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
	id_produto INT AUTO_INCREMENT PRIMARY KEY, 
	nome VARCHAR(255) UNIQUE NOT NULL CHECK(CHAR_LENGTH(nome) >= 3),
	preco DECIMAL(10, 2) NOT NULL CHECK(preco > 0),
	estoque INT NOT NULL CHECK(estoque >= 0),
	categoria VARCHAR(255)
);

