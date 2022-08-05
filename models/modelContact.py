from database.contactDB import ContactDB
#from database.contactAdminDB import ContactAdminDB //This is in case you want to read all the contacts.
from models.update_contact import check_update_contact


class Model_Contact:
	def __init__(self):
		self.object = ContactDB()


	#Create a user in the database.
	def create(self, data, id_user):
		"""
			data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
		"""
		name = data["name_contact"]
		num_phone = data["num_phone"]
		exist_name = self.object.read_name_contact(name, id_user) #check the name exist.
		exist_number = self.object.read_num_phone(num_phone, id_user) #check the number exist.
		if exist_name or exist_number: 
			return f"Sorry, contact with the number and name {num_phone}, {name} already registered."
		else:
			return self.object.create_contact(data)


	#Find all contact from users with "id_user".
	def read(self, id_user):
		exist = self.object.read_id_user(id_user) #Find user. 
		if exist: #In case the user exist, return data.
			data = self.object.read_contact(id_user) #Find all contacts. 
			return data
		else:
			return f"User with id {id_user} not exist."


	#Find and return contact with id "id_contact"
	def read_only_id(self, id_contact):
		data = self.object.read_id_contact(id_contact) #Search user. 
		if data: #return values.
			return data
		else:
			return f"User with id {id_user} does not exist."


	#Update contact with the data passed by parameters.
	def update(self, id_contact, new_data):
		"""
			data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
		"""
		exist_contact = self.object.read_id_contact(id_contact) #Check the user exist.
		if exist_contact:
			text = check_update_contact(id_contact, exist_contact, new_data)
			if text == True:
				return self.object.update_contact(id_contact, new_data) #Update new data.
			return text
		else:
			return f"Sorry, contact with id {id_contact} not exist."


	#Delete user with the id passed by parameters.
	def delete(self, id_contact):
		exist = self.object.read_id_contact(id_contact) #find the contac.
		if exist: #en caso de que exista el contacto
			return self.object.delete_contact(id_contact) #delete the contact.
		else:
			return f"The contact with id {id_contact} not exist"