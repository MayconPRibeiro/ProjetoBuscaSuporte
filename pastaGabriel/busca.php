<?php
// Incluir aquivo de conexão
include("conn.php");
 
// Recebe o valor enviado
$valor = $_GET['valor'];
$valornovo = preg_replace('/[ -]+/' , '%' , $valor);
 
// Procura titulos no banco relacionados ao valor
$sql = mysql_query("SELECT * FROM chamados WHERE titulo LIKE '%".$valornovo."%' or categoria LIKE '%".$valornovo."%'");
 
// Exibe todos os valores encontrados
while ($noticias = mysql_fetch_object($sql)) {
echo "<a href=\"javascript:func()\" onclick=\"exibirConteudo('".$noticias->id."')\">".$noticias->titulo."</a><br />";
}
 
// Acentuação
header("Content-Type: text/html",true);
?>
