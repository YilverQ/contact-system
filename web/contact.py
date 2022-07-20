from flask import Blueprint

contactSite = Blueprint("contactSite", __name__)

@contactSite.route("/contact")
def index():
	return "<h1>Hola Desde una página web.</h1>"