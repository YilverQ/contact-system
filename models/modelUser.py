from database.userDB import UserDB

class Model_User(UserDB):
	def __init__(self):
		self.object = UserDB()


	#Crear usuario en la base de datos.
	def create(self, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		email = data["email"]
		exist = self.object.read_mail_user(email) #comprueba que el correo existe.
		if exist: 
			return f"Lo siento, usuario con el correo {email} ya se encuentra registrado"
		else:
			return self.object.create_user(data)


	#Busca usuario con el id pasado por parametro
	def read_only_id(self, id_user):
		data = self.object.read_id_user(id_user) #Busca usuario. 
		if data: #en caso de que exista, devolver valores.
			return data
		else:
			return f"Usuario con el id {id_user} no existe"


	#Devuelve la lista de usuarios en la BD.
	def read(self):
		return self.object.read_users()


	#Actualiza el usuario del id con los datos pasados por parametros.
	def update(self, id_user, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		email = data["email"]
		exist = self.object.read_id_user(id_user) #existe usuario
		if exist:
			data_user = self.object.read_mail_user(email)
			if data_user == None: #En caso de que el correo nuevo no exista.
				return self.object.update_user(id_user, data)
			
			if data_user[0] == id_user: #En caso de que el correo nuevo exista pero sea igual al correo del id.
				return self.object.update_user(id_user, data)
			
			else: #Si el correo existe pero no es igual al del id del usuario a actualizar.
				return f"El correo no está disponible."
		else:
			return f"Lo siento, usuario con el ID {id_user} no existe"


	#Elimina usuario con el id pasado por parametro.
	def delete(self, id_user):
		exist = self.object.read_id_user(id_user) #busca usuario.
		if exist: #en caso de que exista usuario
			return self.object.delete_user(id_user) #elimina el usuario.
		else:
			return f"Usuario con el id {id_user} no existe"