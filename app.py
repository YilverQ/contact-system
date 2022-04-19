#Modulos y librerias.
from flask import Flask
from flask import jsonify, request
from model import *

#Aplicación.
app = Flask(__name__)
obj_usuario = Model_Usuario()
obj_contacto = Model_Contacto()

#FUNCIONES GLOBALES.
#Atendemos la petición POST o PUT para devolver un diccionario u objeto.
def request_usuario_nuevo():
	usuario_nuevo = {
		"nombre" : request.json["nombre"],
		"apellido" : request.json["apellido"],
		"correoElectronico" : request.json["correoElectronico"],
		"clave" : request.json["clave"]
	}
	return usuario_nuevo

#Atendemos la petición POST o PUT para devolver un diccionario u objeto.
def request_contacto_nuevo():
	contacto_nuevo = {
		"numTelefono" : request.json["numTelefono"],
		"nombreContacto" : request.json["nombreContacto"],
		"idUsuario" : request.json["idUsuario"]
	}
	return contacto_nuevo



#Rutas GLOBALES.
@app.route("/")
def index():
	index = {"Mensaje":"Hola Mundo Desde Flask",}
	return jsonify(index)


#Rutas Para Usuario.
@app.route("/usuarios/<int:id>")
def leer_usuario(id):
	datos = obj_usuario.read_only(id)
	mensaje = {"Mensaje":f"Leer Usuario con id: {id}", "Datos": datos}
	return jsonify(mensaje)


@app.route("/usuarios")
def leer_usuarios():
	lista_usuarios = obj_usuario.read()
	mensaje = {"Mensaje": "Esta es la lista de Usuarios", "Usuarios": lista_usuarios}
	return jsonify(mensaje)


@app.route("/usuarios", methods = ["POST"])
def crear_usuario():
	usuario_nuevo = request_usuario_nuevo()
	mensaje = {"Mensaje": obj_usuario.create(usuario_nuevo)}
	return jsonify(mensaje)


@app.route("/usuarios/<int:id>", methods = ["PUT"])
def actualizar_usuario(id):
	usuario_nuevo = request_usuario_nuevo()
	mensaje = {"Mensaje": obj_usuario.update(id, usuario_nuevo)}
	return jsonify(mensaje)


@app.route("/usuarios/<int:id>", methods = ["Delete"])
def eliminar_usuario(id):
	mensaje = {"Mensaje": obj_usuario.delete(id)}
	return jsonify(mensaje)



#Rutas Para Contacto.
@app.route("/all-contactos")
def leer_all_contactos():
	lista_contactos = obj_contacto.read_all()
	mensaje = {"Mensaje": "Lista completa de Contactos", "Contactos": lista_contactos}
	return jsonify(mensaje)


@app.route("/contactos/<int:idUsuario>")
def leer_contactos(idUsuario):
	lista_contactos = obj_contacto.read(idUsuario)
	mensaje = {"Mensaje": "Lista de contactos", "Contactos": lista_contactos}
	return jsonify(mensaje)


@app.route("/contactos", methods = ["POST"])
def crear_contacto():
	contacto_nuevo = request_contacto_nuevo()
	idUsuario = contacto_nuevo["idUsuario"]
	mensaje = {"Mensaje": obj_contacto.create(contacto_nuevo, idUsuario)}
	return jsonify(mensaje)


@app.route("/contactos/<int:idContacto>", methods = ["PUT"])
def actualizar_contacto(idContacto):
	contacto_nuevo = request_contacto_nuevo()
	mensaje = {"Mensaje": obj_contacto.update(idContacto, contacto_nuevo)}
	return jsonify(mensaje)


@app.route("/contactos/<int:idContacto>", methods = ["Delete"])
def eliminar_contacto(idContacto):
	mensaje = {"Mensaje": obj_contacto.delete(idContacto)}
	return jsonify(mensaje)



#Ejecución Del Programa.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)