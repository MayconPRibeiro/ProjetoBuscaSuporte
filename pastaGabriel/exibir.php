<?php
// Incluir aquivo de conex�o
include("conn.php");
 
// Recebe a id enviada no m�todo GET
$id = $_GET['id'];
 
// Seleciona a noticia que tem essa ID
$sql = mysql_query("SELECT * FROM chamados WHERE id = '".$id."'");
$row = mysql_query("SELECT data FROM chamados WHERE id = '".$id."'");
// Pega os dados e armazena em uma vari�vel
$noticia = mysql_fetch_object($sql);

$date = date_create($row[0]);

// Exibe o conte�do da notica
echo $noticia -> conteudo;
echo wordwrap("<br />\n");
echo "Postado por: ";
echo $noticia -> funcionario;
echo wordwrap("<br>");
echo $noticia -> data;
 
// Acentua��o
//header("Content-Type: multipart/form-data",true);
header("Content-Type: text/html",true);
?>
