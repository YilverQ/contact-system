from flask import Blueprint

userSite = Blueprint("userSite", __name__)

@userSite.route("/user")
def index():
	return "<h1>Hola Desde una página web.</h1>"