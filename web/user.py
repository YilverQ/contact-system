#import requests
from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect
from models.modelUser import Model_User
from models.requestUser import data_request_POST


#blueprints
userSite = Blueprint("userSite", __name__)


#Objeto Global.
obj_user = Model_User()


"""Rutas"""
#----------------------------------------------

#SingUp
#Create a new user
@userSite.route("/SingUp", methods = ["GET", "POST"])
def singUp():
	if request.method == 'POST':
		new_user = data_request_POST(request.form) #data from request (POST).
		message = obj_user.create(new_user)
		flash(f'{message}')
		return redirect(url_for('login'))

	data = {"title":"Sing Up"}
	return render_template('singUp.html', data=data)


#Read all users
@userSite.route("/users", methods = ["GET"])
def users():
	#Mensaje flash. Admin
	users = obj_user.read()
	data = {"title":"User (Admin)", "users" : users}
	return render_template('users.html', data=data)


#Update one user when "id" is equal to id_user
@userSite.route("/upd-user/<int:id_user>", methods = ["GET", "POST"])
def update_user(id_user):
	if request.method == 'POST':
		new_user = data_request_POST(request.form) #data from request (POST).
		message = obj_user.update(id_user, new_user)
		flash(f'{message}')
		return redirect(url_for('userSite.users'))

	user = obj_user.read_only_id(id_user)
	data = {"title":f"Update User by ID {id_user}", "user" : user}
	return render_template('user/user_edit.html', data=data)

	
#Delete user where "id" is equal to id_user
@userSite.route("/del-user/<int:id_user>")
def delete_user(id_user):
	message = obj_user.delete(id_user)
	flash(f'{message}')
	return redirect(url_for('userSite.users'))


""" Working """
#Read only user.
@userSite.route("/read-user/<int:id_user>")
def read_only_user(id_user):
	data = {"title":f"User by id {id_user}"}
	return render_template('user.html', data=data)