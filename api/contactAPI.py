"""Imports"""
from flask import Blueprint
from flask import jsonify, request
from models.modelContact import Model_Contact
from models.requestContact import data_request


"""Blueprint Aplication contact"""
contactAPI = Blueprint("contactAPI", __name__, url_prefix = "/api")


#Global object.
obj_contact = Model_Contact()


"""Routes"""
#----------------------------------------------

#Create a new contact.
@contactAPI.route("/contact/<int:id_user>", methods = ["POST"]) #El id_user debe ser una cookie.
def create_contact(id_user):
	new_contact = data_request(request.json) #Request data.
	message = {"Message" : "Create a new contact..."}
	message["New contact:"] = obj_contact.create(new_contact, id_user)
	return jsonify(message)


#Get a complete list of contact from "id_user".
@contactAPI.route("/contact/<int:id_user>", methods = ["GET"]) #El id_user debe ser una cookie.
def read_contact(id_user):
	message = {"Message" : "Contact List."}
	message["Contacts from list:"] = obj_contact.read(id_user)
	return jsonify(message)


#Update contact with id "id_contact".
@contactAPI.route("/contact/<int:id_contact>", methods = ["PUT"])
def update_contact(id_contact):
	data = data_request(request.json) #Request data.
	message = {"Message" : f"Updating contact data with id {id_contact}"}
	message["New data:"] = obj_contact.update(id_contact, data)
	return jsonify(message)


#Delete the contact with id "id_contact".
@contactAPI.route("/contact/<int:id_contact>", methods = ["Delete"])
def delete_contact(id_contact):
	message = {"Message" : f"Deleting contact data with id {id_contact}"}
	message["Message 2:"] = obj_contact.delete(id_contact)
	return jsonify(message)