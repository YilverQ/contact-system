from database.connectionDB import DAO


class ContactAdminDB(DAO):
	"""CRUD For the administrator in Contact"""
	##########################################
	#Get a complete list of contacts.
	def __read_contact(self): #Private method.
		self.cursor.execute("Select * from Contact;")
		return self.cursor.fetchall()


	#Create a new contact.
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
		return "Contact has created successfully."


	#Update a contact with id is equal "id_contact".
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
		return "Contact has  successfully."


	#Delete contact with id is equal "id_contact".
	def delete_contact(self, id_contact):
		sentence = f"""Delete FROM Contact WHERE id = {id_contact};"""
		self.cursor.execute(sentence)
		self.conexion.commit()
		return f"Contact {id_contact} has deleted successfully."