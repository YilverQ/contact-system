from database.connectionDB import DAO
from database.contactAdminDB import ContactAdminDB


class ContactDB(ContactAdminDB):
	"""CRUD Contact"""
	##########################################
	#Get a complete list of Contacts from "id_user".
	def read_contact(self, id_user):
		sentence = f"Select * FROM Contact WHERE id_user = '{id_user}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchall()


	#Check that the phone number exists.
	def read_num_phone(self, num_phone, id_user):
		sentence = f"Select * FROM Contact WHERE num_phone = '{num_phone}' and id_user = {id_user};"
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#Check that the contact name exists.
	def read_name_contact(self, name_contact, id_user):
		sentence = f"Select * FROM Contact WHERE name_contact = '{name_contact}' and id_user = {id_user};"
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#Checks that the contactID of the contact exists.
	def read_id_contact(self, id_contact):
		sentence = f"Select * FROM Contact WHERE id = '{id_contact}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone()


	#Checks that the contactID of the user exists.
	def read_id_user(self, id_user):
		sentence = f"Select * FROM User WHERE id = '{id_user}';"
		self.cursor.execute(sentence)
		return self.cursor.fetchone()