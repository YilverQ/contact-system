"""Imports"""
from flask import Blueprint
from flask import jsonify, request
from models.modelUser import Model_User
from models.requestUser import data_request

#Blueprint aplication User.
userAPI = Blueprint("userAPI", __name__, url_prefix = "/api")


#Global object.
obj_user = Model_User()

"""Routes"""
#----------------------------------------------

#Return all user from database.
@userAPI.route("/user", methods = ["GET"])
def read_user():
	message = {"Message" : "User list."}
	message["Full user list:"] = obj_user.read()
	return jsonify(message)


#Create a new user.
@userAPI.route("/user", methods = ["POST"])
def create_user():
	new_user = data_request(request.json) #Request data.
	message = {"Message" : "Creating a new user..."}
	message["New user:"] = obj_user.create(new_user)
	return jsonify(message)


#Update data from user with id "id_user".
@userAPI.route("/user/<int:id_user>", methods = ["PUT"])
def update_user(id_user):
	new_user = data_request(request.json) #Data request.
	message = {"Message" : f"Updating user with id {id_user}..."}
	message["Message 2: "] = obj_user.update(id_user, new_user)
	return jsonify(message)


#Delete user with id "id_user" from database.
@userAPI.route("/user/<int:id_user>", methods = ["Delete"])
def delete_user(id_user):
	message = {"Message" : f"Deleting user with id {id_user}..."}
	message["Message 2: "] = obj_user.delete(id_user)
	return jsonify(message)


#Get data from a single user.
@userAPI.route("/user/<int:id_user>", methods = ["GET"])
def read_only_user(id_user):
	message = {"Message" : f"Usuario con id: {id_user}"}
	message["Datos: "] = obj_user.read_only_id(id_user)
	return jsonify(message)