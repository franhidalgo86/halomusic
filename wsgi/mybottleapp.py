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


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
