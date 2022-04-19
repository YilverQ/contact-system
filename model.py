from database.usuarioDB import UsuarioDB
from database.contactoDB import ContactoDB

class Model_Usuario:
	def __init__(self):
		self.objeto = UsuarioDB()


	#Crear usuario en la base de datos.
	def create(self, datos):
		"""
			datos = {
				"nombre" : "", "apellido" : "",
				"correoElectronico": "", "clave" : ""}
		"""
		correo = datos["correoElectronico"]
		existe = self.objeto.read_mail_usuario(correo) #comprueba que el correo existe.
		if existe: 
			return f"Lo siento, usuario con el correo {correo} ya se encuentra registrado"
		else:
			return self.objeto.create_usuario(datos)


	#Busca usuario con el id pasado por parametro
	def read_only(self, id):
		datos = self.objeto.obtener_id_usuario(id) #Busca usuario. 
		if datos: #en caso de que exista, devolver valores.
			return datos
		else:
			return f"Usuario con el id {id} no existe"


	#Devuelve la lista de usuarios en la BD.
	def read(self):
		return self.objeto.read_usuarios()


	#Actualiza el usuario del id con los datos pasados por parametros.
	def update(self, id, datos):
		"""
			datos = {
				"nombre" : "", "apellido" : "",
				"correoElectronico": "", "clave" : ""}
		"""
		correo = datos["correoElectronico"]
		existe = self.objeto.obtener_id_usuario(id) #existe usuario
		if existe:

			datos_usuario = self.objeto.read_mail_usuario(correo)
			if datos_usuario == None: #En caso de que el correo nuevo no exista.
				return self.objeto.update_usuario(id, datos)
			
			if datos_usuario[0] == id: #En caso de que el correo nuevo exista pero sea igual al correo del id.
				return self.objeto.update_usuario(id, datos)
			
			else: #Si el correo existe pero no es igual al del id del usuario a actualizar.
				return f"El correo no está disponible."
		else:
			return f"Lo siento, usuario con el ID {id} no existe"


	#Elimina usuario con el id pasado por parametro.
	def delete(self, id):
		existe = self.objeto.obtener_id_usuario(id) #busca usuario.
		if existe: #en caso de que exista usuario
			return self.objeto.delete_usuario(id) #elimina el usuario.
		else:
			return f"Usuario con el id {id} no existe"



class Model_Contacto:
	def __init__(self):
		self.objeto = ContactoDB()


	#Crear usuario en la base de datos.
	def create(self, datos, idUsuario):
		"""
			datos = {
				"numTelefono" : 	"",
				"nombreContacto": 	"", 
				"idUsuario" : 		""}
		"""
		nombre = datos["nombreContacto"]
		numero = datos["numTelefono"]
		existe_nombre = self.objeto.read_nombre(nombre, idUsuario) #comprueba que el nombre existe.
		existe_numero = self.objeto.read_telefono(numero, idUsuario) #comprueba que el numero existe.
		if existe_numero or existe_nombre: 
			return f"Lo siento, contacto con el numero o nombre {nombre}, {numero} ya se encuentra registrado"
		else:
			return self.objeto.create_contacto(datos)


	#Busca todos los contacto del usuario con idUsuario.
	def read(self, idUsuario):
		datos = self.objeto.read_contactos_by(idUsuario) #Busca todos los contactos. 
		if datos: #en caso de que exista el usuario, devolver valores.
			return datos
		else:
			return f"Usuario con el id {idUsuario} no existe"


	#Devuelve la lista de contactos en la BD.
	def read_all(self):
		return self.objeto.read_contacto()


	#Actualiza el usuario del id con los datos pasados por parametros.
	def update(self, idContacto, datos):
		"""
			datos = {
				"numTelefono" : 	"",
				"nombreContacto": 	"", 
				"idUsuario" : 		""}
		"""
		existe_contacto = self.objeto.read_idContacto(idContacto) #comprueba que el usuario exista.
		if existe_contacto:
			idUsuario = datos["idUsuario"]
			nombre = datos["nombreContacto"]
			numero = datos["numTelefono"]
			existe_nombre = self.objeto.read_nombre(nombre, idUsuario) #comprueba que el nombre existe.
			existe_numero = self.objeto.read_telefono(numero, idUsuario) #comprueba que el numero existe.

			if existe_nombre or existe_numero: #Si los datos existen devolver un mensaje.
				return f"Lo siento, contacto con el numero o nombre {nombre}, {numero} ya se encuentra registrado"
			else: #Si no existen es porque los datos están disponibles.
				return self.objeto.update_contacto(idContacto, datos) #Se actualizan los nuevos datos.
		else:
			return f"Lo siento, el contacto con el ID {idContacto} no existe"


	#Elimina usuario con el id pasado por parametro.
	def delete(self, idContacto):
		existe = self.objeto.read_idContacto(idContacto) #busca el contacto.
		if existe: #en caso de que exista el contacto
			return self.objeto.delete_contacto(idContacto) #elimina el contacto.
		else:
			return f"El Contacto con el id {idContacto} no existe"