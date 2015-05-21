% include('header.tpl')
<h3>Busca Videos</h3>
 
<form action="/buscarvideos" method="post">
  Artista:
  <input type="text" name="nombre" value="" />
 
  <br/>
 
  <input type="submit" value="Enviar" />
</form>
% include('footer.tpl')
