from database.connectionDB import DAO


class ContactAdminDB(DAO):
	"""CRUD Para el administrador en Contacto"""
	##########################################
	#Obtiene una lista completa de los contactos.
	def __read_contact(self): #Método privado.
		self.cursor.execute("Select * from Contact;")
		return self.cursor.fetchall()


	#Crea un contacto con los datos pasados.
	def create_contact(self, data):
		"""
			data = {
				"num_phone" : 	"",
				"name_contact": 	"", 
				"id_user" : 		""}
		"""
		usuario  = """Insert INTO Contact (num_phone, name_contact, id_user)"""
		values 	 = f"""VALUES ('{data["num_phone"]}', '{data["name_contact"]}', '{data["id_user"]}');"""
		sentence = usuario + " " + values
		self.cursor.execute(sentence)
		self.conexion.commit()
		return "Contacto Registrado Sastifactoriamente"


	#Actualiza los datos de un contacto.
	def update_contact(self, id_contact, data):
		"""
			data = {
				"num_phone" : 	"",
				"name_contact": 	"", 
				"id_user" : 		""}
		"""
		dataUpdate = f"""num_phone = '{data["num_phone"]}', name_contact = '{data["name_contact"]}', id_user = '{data["id_user"]}'"""
		sentence 	= f"Update Contact set {dataUpdate} WHERE id = {id_contact};";
		self.cursor.execute(sentence)
		self.conexion.commit()
		return "Contacto Actualizado Sastifactoriamente"


	#Elimina una fila de la tabla contacto.
	def delete_contact(self, id_contact):
		sentence = f"""Delete FROM Contact WHERE id = {id_contact};"""
		self.cursor.execute(sentence)
		self.conexion.commit()
		return f"Contacto {id_contact} Ha Sido Eliminado Sastifactoriamente"