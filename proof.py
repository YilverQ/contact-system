def input_manager(username, password):
	data = get_data()
	data["Managers"] = [{"username" : username, "password" : password}]
	with open("data.json", "w") as json_file:
		json.dump(data, json_file, indent = 4)
	return data["Managers"]



@app.route("/admin/admin", methods = ["GET", "POST"])
def admin():
	data = {"title" : "Login"}
	form = Login()
	if form.validate_on_submit():
		print("Hola Mudno Si llegamos hasta aqui")
		return redirect(url_for("index"))

	return render_template("login.html", data = data, form = form)






########################################

estruct_json_user = {"id" : None,
						 "username" : "",
						 "email" : "",
						 "password" : ""}

	estruct_json_contact = {"id" : None,
							"fullname" : "",
							"email" : "",
							"phone" : ""}

	user = Contact("Users", estruct_json_user)
	contact = Contact("Contacts", estruct_json_contact)

	password = "Bloyhu"
	new_user = { "id" : None,
				 "username" : "Quevedo Molinares",
				 "email" : "yilver0906@protonmail.com",
				 "password" : generate_password_hash(password, method = "sha256")}


	new_contact = { "id" : None,
					"fullname" : "Yilver Antonio",
					"email" : "yilver0906@protonmail.com",
					"phone" : "04160140472"}


	#print(user.get_all_items())
	print(user.delete_item("Yilver Quevedo"))

	#print(contact.get_all_items())
	print(contact.delete_item("Yilver Antonio"))





#####################################################
#####################################################
#####################################################




### Obtener Datos del Archivo JSON ###
def get_data():
	#abrir el archivo JSON
	#Retorna el archivo como un Diccionario
	with open("data.json", "r") as json_file:
		return json.load(json_file)


### Escribir Datos en Data.JSON ###
def write_data(data):
	#Reescribimos el diccionario "data" en el archivo
	with open("data.json", "w") as json_file:
		json.dump(data, json_file, indent = 4)
		return "File has Modified!"



### Comprobamos que el usuario (Manager) tenga las credenciales correctas ###
def check_manager(username, password):
	data = data["Managers"]
	for i in data:
		username_bool = check_password_hash(i["username"], username)
		password_bool = check_password_hash(i["password"], password)
		#True, Si las crendenciales son correctas
		if username_bool and password_bool:
			return True

	return False


### Ordenamos los IDs ###
def order_IDs(data):
	for i in range(len(data)):
		data[i]["id"] = i + 1 
	return data


########################################################################################
########################################################################################
########################################################################################

#################
##### Users #####
#################

### Comprobamos que las credenciales sean correctas ###
def check_user_login(username, password):
	data = get_data()
	for i in data["Users"]:
		username_bool = i["username"] == username
		password_bool = check_password_hash(i["password"], password)
		#True la clave y el username son validas
		if username_bool and password_bool:
			return True

	return False


### Comprobamos que el usuario exista en la base de datos ###
def check_user(username):
	# True, el usuario existe. False, el usuario no existe
	data = get_data()
	for i in data["Users"]:
		if i["username"] == username:
			return True		 

	return False


### Comprobamos que el email este en la base de datos ###
def check_email(email):
	# True, el email existe. False, el email no existe
	data = get_data()
	for i in data["Users"]:
		if i["email"] == email:
			return True

	return False



### Agregar Nuevo Usuario ###
def add_user(username, password, email):
	if not check_user(username) and not check_email(email):
		data = get_data()
		ID_from_new_user = len(data["Users"]) + 1
		new_user = {"id" : ID_from_new_user,
					"username" : username.title(),
					"email" : email,
					"password" : generate_password_hash(password, method = "sha256")}

		data["Users"].append(new_user)
		add_from_json = write_data(data)
		return "New User has Created Successfully!"
	return "User already exist!"


### Obtener lista de usuarios ###
def get_users():
	data = get_data()
	return data["Users"]


### Obtener datos de un Usuario ###
def get_user(username):
	if check_user(username):
		data = get_data()
		data = data["Users"]
		for i in data:
			if i["username"] == username:
				return i

	return "User not exist!"


### Actualizar datos de un Usuario ###
def update_user(username, update_user):
	if check_user(username):
		data = get_data()
		iterador = 0
		for i in data["Users"]: 
			if i["username"] == username:
				update_user["id"] = i["id"]
				update_user["password"] = generate_password_hash(update_user["password"], method = "sha256")
				data["Users"][iterador] = update_user
				write = write_data(data)
				return "User Has Updated Successfully!"
			iterador += 1
	return "User not exist!"


### Eliminar Un Usuario ###
def delete_user(username):
	if check_user(username):
		data = get_data()
		for i in data["Users"]:
			if i["username"] == username:
				data["Users"].remove(i)
				data["Users"] = order_IDs(data["Users"])
				write = write_data(data)
				return "User has deleted!"
	return "User to Delete not exist!"






########################################################################################
########################################################################################
########################################################################################

####################
##### Contacts #####
####################
#CRUD /// Create/Read/Update/Delete


### Comprobamos que el usuario exista en la base de datos ###
def check_contact(fullname):
	# True, el usuario existe. False, el usuario no existe
	data = get_data()
	for i in data["Contacts"]:
		if i["fullname"] == fullname:
			return True		 

	return False



### Comprobamos que el email este en la base de datos ###
def check_email(email):
	# True, el email existe. False, el email no existe
	data = get_data()
	for i in data["Contacts"]:
		if i["email"] == email:
			return True

	return False



def add_contact(fullname, email, phone):
	if not check_contact(fullname) and not check_email(email): #Modificar estas funciones########################
		data = get_data()
		ID_from_new_user = len(data["Contacts"]) + 1
		new_user = {"id" : ID_from_new_user,
					"fullname": fullname,
					"email" : email,
					"phone" : phone}

		data["Contacts"].append(new_user)
		add_from_json = write_data(data)
		return "New Contacts Has Created Successfully!"
	return "Contacts Already Exist!"


def get_contacts():
	data = get_data()
	return data["Contacts"]


def get_contact(fullname):
	if check_contact(fullname): #Comprobar está funcion##########################################
		data = get_data()
		data = data["Contacts"]
		for i in data:
			if i["fullname"] == fullname:
				return i
	return "Contact not exist!"


def update_contact(fullname, update_contact):
	if check_contact(fullname):
		data = get_data()
		iterador = 0
		for i in data["Contacts"]:
			update_contact["id"] = i["id"]
			data["Contacts"][iterador] = update_contact
			write = write_data(data)
			return "Contact has Updated Successfully!"

	return "Contact not exist!"


def delete_contact(fullname):
	if check_contact(fullname):
		data = get_data()
		for i in data["Contacts"]:
			if i["fullname"] == fullname:
				data["Contacts"].remove(i)
				data["Contacts"] = order_IDs(data["Contacts"])
				write = write_data(data)
				return "Contact has Deleted!"

	return "Contact to Delete not exist!"



#CRUD
if __name__ == '__main__':
	#username = generate_password_hash("yilver", method = "sha256")
	#password = generate_password_hash("BloyhuVfisbo", method = "sha256")
	#print(check_manager("yilver", "BloyhuVfisbo"))
	
	"""
	print(add_user("JuanCastillo", "JuanChan", "Juan0906@gmail.com"))
	print(add_user("YilverQ", "YilverChan", "Yilver0906@gmail.com"))
	print(add_user("WinderM", "WinderChan", "Winder0906@gmail.com"))
	update = {	"id" : None,
				"username" : "YilverQ",
				"email" : "yilver@protonmail.com",
				"password" : "nueva"}
	"""
	#print(update_user("Yilver", update))
	#print(delete_user("Yilver"))

	pass
	update = {	"id" : None,
						"username" : "Yilver Antonio",
						"email" : "yilver@protonmail.com",
						"phone" : "02123772170"}
	print(delete_contact("Jhon Pacheco"))










#####################################



	def update_data(self):
		self.data = get_data()
		return self.data


	def where_id_user(self, id_user):
		self.id_user = id_user
		return self.id_user


	def data_piece(self):
		if self.block == "Users":
			data = get_data()
			return data["Users"]
		else:
			data = get_data()
			return data["Contacts"][self.id_user][self.search]


	def add_data_piece(self, data):
		if self.block == "Users":
			self.data["Users"] = data
			return self.data
		else:
			self.data["Contacts"][self.id_user][self.search] = data
			return self.data


	def add(self, username):
		data = get_data()
		username = {"username" : username,
					"contact_list" : []}

		data[self.block].append(username)
		add_from_json =  write_data(data)
		return True


	def add_contact(self, new_contact, id_user):
		data = get_data()
		ID_from_new_contact = len(data[self.block][id_user]["contact_list"]) + 1
		new_contact["id"] = ID_from_new_contact
		data[self.block][id_user]["contact_list"].append(new_contact)
		add_from_json =  write_data(data)
		return True


	def get_all_items(self, id_user):
		data = get_data()
		return data[self.block][id_user]["contact_list"]


	def get_item(self, search_item, id_user):
		data = get_data()
		data = data[self.block][id_user]["contact_list"]
		for i in data:
			if i[self.key_search] == search_item:
				return i


	def update(self, search_item, data_update, id_user):
		data = get_data()
		for i in data[self.block][id_user]["contact_list"]:
			if i[self.key_search] == search_item:
				data_update["id"] = i["id"]
				data[self.block][id_user]["contact_list"][i["id"]-1] = data_update #(i["id"]-1) es la posicion del dato.
				add_from_json = write_data(data)
				return True


	def delete_item(self, search_item, id_user):
		data = get_data()
		for i in data[self.block][id_user]["contact_list"]:
			if i[self.key_search] == search_item:
				data[self.block][id_user]["contact_list"].remove(i)
				data[self.block][id_user]["contact_list"] = order_IDs(data[self.block][id_user]["contact_list"])
				write =  write_data(data)
				return True
