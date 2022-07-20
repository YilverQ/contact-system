"""Importaciones"""
from flask import Blueprint
from flask import jsonify, request
from models.modelUser import Model_User
from models.requestUser import data_request

#Aplicación userAPI con Blueprint.
userAPI = Blueprint("userAPI", __name__, url_prefix = "/api")


#Objeto Global.
obj_user = Model_User()

"""Rutas"""
#----------------------------------------------

#Mostrar todos los usuarios de la base de datos.
@userAPI.route("/user", methods = ["GET"])
def read_user():
	message = {"Message" : "Lista de usuarios."}
	message["Lista de Usuarios:"] = obj_user.read()
	return jsonify(message)


#Crear un usuario nuevo.
@userAPI.route("/user", methods = ["POST"])
def create_user():
	new_user = data_request(request.json) #Datos de la petición request.
	message = {"Message" : "Creando Usuario..."}
	message["Nuevo Usuario:"] = obj_user.create(new_user)
	return jsonify(message)


#Actualizar los datos de un usuario.
@userAPI.route("/user/<int:id_user>", methods = ["PUT"])
def update_user(id_user):
	new_user = data_request(request.json) #Datos de la petición request.
	message = {"Message" : f"Actualizando datos del usuario {id_user}..."}
	message["Message 2: "] = obj_user.update(id_user, new_user)
	return jsonify(message)


#Eliminar un usuario de la base de datos.
@userAPI.route("/user/<int:id_user>", methods = ["Delete"])
def delete_user(id_user):
	message = {"Message" : f"Eliminando datos del usuario {id_user}..."}
	message["Message 2: "] = obj_user.delete(id_user)
	return jsonify(message)


#Mostrar los datos de un único usuario.
@userAPI.route("/user/<int:id_user>", methods = ["GET"])
def read_only_user(id_user):
	message = {"Message" : f"Usuario con id: {id_user}"}
	message["Datos: "] = obj_user.read_only_id(id_user)
	return jsonify(message)