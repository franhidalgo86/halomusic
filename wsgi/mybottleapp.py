from bottle import route, default_app,Bottle,request,template,static_file
import requests
from lxml import etree

#PAGINA PRINCIPAL
@route('/')
def index():
	return template("index.tpl")
@route('/index')
def index():
	return template("index.tpl")

@route('/letras')
def letras():
	return template('letras.tpl')
#BUSCA LAS LETRAS DE LAS CANCIONES
@route('/buscarletras' ,method='POST')
def buscarletras():
	artista=request.forms.get('nombre')
	if len(artista) >1: 
		URL_base= ("http://api.muzu.tv/api/artist/details/")
		parametros= {"muzuid":"pixnImQXRE","aname":artista}

@route('/videos')
def videos():
	return template('videos.tpl')
#BUSCA LAS URL DE LOS VIDEOS
@route('/buscarvideos' ,method='POST')


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
