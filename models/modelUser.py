from database.userDB import UserDB

class Model_User(UserDB):
	def __init__(self):
		self.object = UserDB()


	#Create a new user in the database.
	def create(self, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		email = data["email"]
		exist = self.object.read_mail_user(email) #comprueba que el correo existe.
		if exist: 
			return f"Sorry, user with the email {email} already registered."
		else:
			return self.object.create_user(data)


	#Find and return user with id "id_user"
	def read_only_id(self, id_user):
		data = self.object.read_id_user(id_user) #Search user. 
		if data: #return values.
			return data
		else:
			return f"User with id {id_user} does not exist."


	#Return all user in the database.
	def read(self):
		return self.object.read_users()


	#Update user with id "id_user"
	def update(self, id_user, data):
		"""
			data = {
				"name" : "", "last_name" : "",
				"email": "", "password" : ""}
		"""
		email = data["email"]
		exist = self.object.read_id_user(id_user) #User exist
		if exist:
			data_user = self.object.read_mail_user(email)
			if data_user == None: #In case the new mail does not exist.
				return self.object.update_user(id_user, data)
			
			if data_user[0] == id_user: #In case the new email exists but is equal to the email of the id.
				return self.object.update_user(id_user, data)
			
			else: #If the email exists but is not equal to the user id to update.
				return f"Email is not available."
		else:
			return f"Sorry, user with id {id_user} does not exist."


	#Delete user with id "id_user".
	def delete(self, id_user):
		exist = self.object.read_id_user(id_user) #Search user.
		if exist: #if there is a user
			return self.object.delete_user(id_user) #Delete user.
		else:
			return f"User with id {id_user} does not exist."