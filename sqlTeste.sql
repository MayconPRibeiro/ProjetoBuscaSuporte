CREATE DATABASE testeBusca;
USE testeBusca;

CREATE TABLE usuarios(
	id int not null auto_increment primary key,
    nome varchar(150) not null,
    tipo ENUM('gestor', 'suporte', 'cliente'),
    email varchar(150) not null,
    senha varchar(50) not null
);

INSERT INTO usuarios(nome, tipo, email, senha) VALUES ('Maycon Teste', 'gestor', 'gestor@teste.com', 'teste');

select * from usuarios;

CREATE USER 'teste@BD123'@'localhost' IDENTIFIED BY 'teste@BD123';
GRANT ALL PRIVILEGES ON *.* TO 'teste@BD123'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
