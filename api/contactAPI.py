"""Importaciones"""
from flask import Blueprint
from flask import jsonify, request
from models.modelContact import Model_Contact
from models.requestContact import data_request


"""Aplicación contact Blueprint"""
contactAPI = Blueprint("contactAPI", __name__, url_prefix = "/api")


#Objeto Global.
obj_contact = Model_Contact()


"""Rutas"""
#----------------------------------------------

#Crear contacto nuevo.
@contactAPI.route("/contact/<int:id_user>", methods = ["POST"]) #El id_user debe ser una cookie.
def create_contact(id_user):
	new_contact = data_request(request.json) #Datos de la petición request.
	message = {"Message" : "Creando contacto..."}
	message["Contacto nuevo:"] = obj_contact.create(new_contact, id_user)
	return jsonify(message)


#Leer todos los contactos de la base de datos.
@contactAPI.route("/contact/allContacts")
def read_all_contact():
	return jsonify({"Message":"Petición no disponible."})


#Leer todos los contactos del usuario.
@contactAPI.route("/contact/<int:id_user>", methods = ["GET"]) #El id_user debe ser una cookie.
def read_contact(id_user):
	message = {"Message" : "Lista de contactos."}
	message["Lista de contactos:"] = obj_contact.read(id_user)
	return jsonify(message)


#Actualizar un contacto.
@contactAPI.route("/contact/<int:id_contact>", methods = ["PUT"])
def update_contact(id_contact):
	data = data_request(request.json) #Datos de la petición request.
	message = {"Message" : f"Actualizando datos del contacto {id_contact}"}
	message["Datos Nuevos:"] = obj_contact.update(id_contact, data)
	return jsonify(message)


#Eliminar un contacto.
@contactAPI.route("/contact/<int:id_contact>", methods = ["Delete"])
def delete_contact(id_contact):
	message = {"Message" : f"Eliminando datos del contacto {id_contact}"}
	message["Message 2:"] = obj_contact.delete(id_contact)
	return jsonify(message)