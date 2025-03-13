<?php
$host = "localhost"; 
$usuario = "root";
$senha = "gabriel@12";
$banco = "chamados";
 
$conn = mysql_connect($host, $usuario, $senha);
$db = mysql_select_db($banco, $conn);
?>
