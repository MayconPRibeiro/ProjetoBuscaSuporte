<?php
   include("conn.php");

  //Abaixo atribuímos os valores provenientes do formulário pelo método POST
  $titulo = $_POST['titulo']; 
  $categoria = $_POST['categoria'];
  $atendente = $_POST['atendente'];
  $datetime = date('y-m-d H:i:s');
  $conteudo = $_POST['conteudo'];

   $titulo = mysql_escape_string($titulo);
   $categoria = mysql_escape_string($categoria);
  $conteudo = mysql_escape_string($conteudo);
// Montamos a consulta SQL
$query = "INSERT INTO chamados (titulo, categoria, conteudo, funcionario, data) VALUES ('$titulo', '$categoria', '$conteudo', '$atendente', '$datetime')";
// Executa a query
$inserir = mysql_query($query);

if ($titulo==null || $titulo==""){
echo "Não foi possível inserir a cadastro, tente novamente.";
}
if ($categoria==null || $categoria==""){
echo "Não foi possível inserir a cadastro, tente novamente.";
}
if ($conteudo==null || $conteudo==""){
echo "Não foi possível inserir a cadastro, tente novamente.";
}
if ($inserir) {
    ?>
        <div class="sucesso">Cadastro enviado com sucesso!</div>
	<form>
<input type="button" value="Voltar" onClick="JavaScript: window.history.back();">
</form>
    <?php
    
} else {
echo "Não foi possível inserir a cadastro, tente novamente.";
echo "Dados sobre o erro:" . mysql_error();

    ?>
	<form>
<input type="button" value="Voltar" onClick="JavaScript: window.history.back();">
</form>
    <?php


}
