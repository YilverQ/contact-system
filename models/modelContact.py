from database.contactDB import ContactDB
#from database.contactAdminDB import ContactAdminDB //Esto es por si se quiere leer todos los contactos.
from models.update_contact import check_update_contact


class Model_Contact:
	def __init__(self):
		self.object = ContactDB()


	#Crear usuario en la base de datos.
	def create(self, data, id_user):
		"""
			data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
		"""
		name = data["name_contact"]
		num_phone = data["num_phone"]
		exist_name = self.object.read_name_contact(name, id_user) #comprueba que el nombre existe.
		exist_number = self.object.read_num_phone(num_phone, id_user) #comprueba que el numero existe.
		if exist_name or exist_number: 
			return f"Lo siento, contacto con el numero o nombre {num_phone}, {name} ya se encuentra registrado"
		else:
			return self.object.create_contact(data)


	#Busca todos los contacto del usuario con idUsuario.
	def read(self, id_user):
		exist = self.object.read_id_user(id_user) #Busca todos los contactos. 
		if exist: #en caso de que exista el usuario, devolver valores.
			data = self.object.read_contact(id_user) #Busca todos los contactos. 
			return data
		else:
			return f"Usuario con el id {id_user} no existe"


	#Devuelve la lista de contactos desde la BD.
	def read_all(self):
		#Hay que devolver toda la lista. 
		return "Todavía no sirve... Sorry"


	#Actualiza el usuario del id con los datos pasados por parametros.
	def update(self, id_contact, new_data):
		"""
			data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
		"""
		exist_contact = self.object.read_id_contact(id_contact) #comprueba que el usuario exista.
		if exist_contact:
			text = check_update_contact(id_contact, exist_contact, new_data)
			if text == True:
				return self.object.update_contact(id_contact, new_data) #Se actualizan los nuevos datos.
			return text
		else:
			return f"Lo siento, el contacto con el ID {id_contact} no existe"


	#Elimina usuario con el id pasado por parametro.
	def delete(self, id_contact):
		exist = self.object.read_id_contact(id_contact) #busca el contacto.
		if exist: #en caso de que exista el contacto
			return self.object.delete_contact(id_contact) #elimina el contacto.
		else:
			return f"El Contacto con el id {id_contact} no existe"