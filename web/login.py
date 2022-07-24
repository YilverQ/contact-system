from flask import Blueprint
from flask import render_template

login = Blueprint("login", __name__)

#Login
@userSite.route("/login")
def login():
	data = {"title":"Login"}
	return render_template('login.html', data=data)


#SingUp
@userSite.route("/SingUp")
def singUp():
	data = {"title":"Sing Up"}
	return render_template('singUp.html', data=data)