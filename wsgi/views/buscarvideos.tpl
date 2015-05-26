% include('header.tpl')
	<ul>
	% for Videos,tit in valor:
		<li><a href="{{Videos}}"> {{tit}}</a></li>
	% end
	</ul>
% include('footer.tpl')
