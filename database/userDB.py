from database.connectionDB import DAO


class UserDB(DAO):
	"""CRUD-Usuario"""
	###########################################
	#Obtiene una lista completa de los usuarios.
	def read_users(self):
		self.cursor.execute("Select * from User;")
		return self.cursor.fetchall() #Obtiene todos las filas de la tabla. 


	#Crea un usuario con los datos pasados.
	def create_user(self, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		insert	 = """Insert INTO User (name, last_name, email, password)"""
		values	 = f"""VALUES ('{data["name"]}', '{data["last_name"]}', '{data["email"]}', '{data["password"]}');"""
		sentence = insert + " " + values #'sentence' es la sentencia SQL a ejecutar.
		self.cursor.execute(sentence)
		self.conexion.commit()
		return "Usuario Registrado Sastifactoriamente"


	#Actualiza los datos de un usuario.
	def update_user(self, idUser, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		dataUpdate = f"""name = '{data["name"]}', last_name = '{data["last_name"]}', email = '{data["email"]}', password = '{data["password"]}'"""
		sentence 	= f"Update User set {dataUpdate} WHERE id = {idUser}"; 
		self.cursor.execute(sentence) #Se actualiza toda la fila.
		self.conexion.commit()
		return "Usuario Actualizado Sastifactoriamente"


	#Elimina una fila de la tabla usuario.
	def delete_user(self, idUser):
		sentence = f"""Delete FROM User WHERE id = {idUser};"""
		self.cursor.execute(sentence) #Elimina toda la fila.
		self.conexion.commit()
		return f"Usuario {idUser} Ha Sido Eliminado Sastifactoriamente"


	#Obtiene solo la fila donde se encuentra el correoElectronico.
	def read_mail_user(self, email):
		sentence = f"Select * FROM User WHERE email = '{email}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone() #retorna una sola fila


	#Obtiene la fila del usuario con el id pasado como parametro.
	def read_id_user(self, idUser):
		sentence = f"Select * FROM User WHERE id = '{idUser}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone() #retorna muchas filas.