create database teste;
use teste;


CREATE TABLE `chamados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `categoria` varchar(200) NOT NULL,
  `conteudo` text NOT NULL,
  `funcionario` varchar(20) DEFAULT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=809;


CREATE TABLE `usuarios` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `senha` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2;

insert into usuarios(id, nome, usuario, senha) values ('', 'Maycon', 'teste', 'teste');


use chamados;
select * from chamados;
select * from usuarios;


