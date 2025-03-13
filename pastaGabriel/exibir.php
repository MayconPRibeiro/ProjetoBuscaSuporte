<?php
// Incluir aquivo de conexão
include("conn.php");
 
// Recebe a id enviada no método GET
$id = $_GET['id'];
 
// Seleciona a noticia que tem essa ID
$sql = mysql_query("SELECT * FROM chamados WHERE id = '".$id."'");
$row = mysql_query("SELECT data FROM chamados WHERE id = '".$id."'");
// Pega os dados e armazena em uma variável
$noticia = mysql_fetch_object($sql);

$date = date_create($row[0]);

// Exibe o conteúdo da notica
echo $noticia -> conteudo;
echo wordwrap("<br />\n");
echo "Postado por: ";
echo $noticia -> funcionario;
echo wordwrap("<br>");
echo $noticia -> data;
 
// Acentuação
//header("Content-Type: multipart/form-data",true);
header("Content-Type: text/html",true);
?>
