CREATE DATABASE testeBusca;
USE testeBusca;

CREATE TABLE usuarios(
	id int not null auto_increment primary key,
    nome varchar(150) not null,
    tipo varchar(150) not null,
    email varchar(150) not null unique,
    senha varchar(255) not null
);

INSERT INTO usuarios(nome, tipo, email, senha) VALUES ('Maycon Teste', 'gestor', 'gestor@teste.com', 'teste');

select * from usuarios;

CREATE TABLE chamados(
	id int not null auto_increment primary key,
    titulo varchar(150) not null,
    descricao varchar(700) not null,
    nome_tecnico varchar(150) not null,
    permissoes varchar(20) not null,
    data_hora datetime not null
);
