from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect, make_response

from models.modelUser import Model_User
from models.requestUser import data_request_POST
from database.userDB import UserDB

#blueprints
register = Blueprint("register", __name__)


#Objeto Global.
obj_user = Model_User()



"""Rutas"""
#----------------------------------------------

#Login
@register.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == 'POST':
		response_model = obj_user.read_mail_user(request.form["email"])
		if type(response_model) == type(()):
			if request.form["password"] == response_model[4]:
				id_user = str(response_model[0])
				resp = make_response(redirect(url_for('index')))
				resp.set_cookie('userID', id_user)
				return resp

			flash(f'Entered password is not valid')
			return redirect(url_for('register.login'))
		
		flash(f'{response_model}')
		return redirect(url_for('register.login'))
	data = {"title":"Login"}
	return render_template('login.html', data=data)


#SingUp
#Create a new user
@register.route("/SingUp", methods = ["GET", "POST"])
def singUp():
	if request.method == 'POST':
		new_user = data_request_POST(request.form) #data from request (POST).
		message = obj_user.create(new_user)
		flash(f'{message}')
		return redirect(url_for('register.login'))

	data = {"title":"Sing Up"}
	return render_template('singUp.html', data=data)