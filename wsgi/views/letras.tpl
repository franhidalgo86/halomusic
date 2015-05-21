% include('header.tpl')
<h3>Busca Letras</h3>
 
<form action="/buscarletras" method="post">
  Artista:
  <input type="text" name="nombre" value="" />
 
  <br/>
 
  <input type="submit" value="Enviar" />
</form>
% include('footer.tpl')
