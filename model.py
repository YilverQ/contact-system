from werkzeug.security import generate_password_hash, check_password_hash
import json

### Obtener Datos del Archivo JSON ###
def get_data():
	with open("data.json", "r") as json_file:
		return json.load(json_file)


### Escribir Datos en Data.JSON ###
def write_data(data):
	with open("data.json", "w") as json_file:
		json.dump(data, json_file, indent = 4)
		return "File has Modified!"


### Ordenamos los IDs ###
def order_IDs(data):
	for i in range(len(data)):
		data[i]["id"] = i + 1 
	return data


### Clase Usuario ###
class User():
	def __init__(self):
		self.block = "Users"
		self.struct_user = { "id" : None,
							 "username" : "",
							 "email" : "",
							 "password" : ""}

		self.key_search = "username"
		self.data = get_data()


	### Actualizar Data ###
	def update_data(self):
		self.data = get_data()
		return True


	### Obtener un pedazo de la base de datos ###
	def data_piece(self):
		data = get_data()
		return data["Users"]


	### Escribimos un pedazo modificado en la base de datos ###
	def add_data_piece(self, data):
		self.data["Users"] = data
		add_from_json = write_data(self.data)
		return True


	#####################################
	#############__CRUD__################
	#####################################

	### Añadimos un nuevo usuario en la base de datos ###
	def add(self, new_user):
		actualizar_data = self.update_data()
		data = self.data_piece()
		ID_from_new_user = len(data) + 1
		new_user["id"] = ID_from_new_user
		data.append(new_user)
		add_from_json =  self.add_data_piece(data)
		return True


	### Obtenemos todos los item de un bloque // User/Contacts/Contact ###
	def get_all_items(self):
		data = self.data_piece()
		return data


	### Obtenemos un item de un bloque // User/Contacts/Contact ###
	def get_item(self, search_item):
		data = self.data_piece()
		for i in data:
			if i[self.key_search] == search_item:
				return i


	### Actualizamos un item en la base de datos // User/Contacts/Contact ###
	def update(self, search_item, data_update):
		actualizar_data = self.update_data()
		data = self.data_piece()
		for i in data:
			if i[self.key_search] == search_item:
				data_update["id"] = i["id"]
				data[i["id"]-1] = data_update #(i["id"]-1) es la posicion del dato.
				add_from_json = self.add_data_piece(data)
				return True


	### Eliminamos un item en la base de datos // User/Contacts/Contact ###
	def delete_item(self, search_item):
		actualizar_data = self.update_data()
		data = self.data_piece()
		for i in data:
			if i[self.key_search] == search_item:
				data.remove(i)
				data = order_IDs(data)
				write =  self.add_data_piece(data)
				return True


class Contact(User):
	def __init__(self):
		self.block = "Contacts"
		self.struct_user = { "id" : None,
							 "fullname" : "",
							 "email" : "",
							 "phone" : ""}

		self.key_search = "fullname"
		###########################
		self.id_user = None
		self.data = None
		self.search = "contact_list"


	### igualamos el "id_user" con el id del dato a trabajar ###
	def where_id_user(self, id_user):
		self.id_user = id_user
		return self.id_user


	### Obtenemos un pedazo de la base de datos // "Contacts" ###
	def data_piece(self, id_user = True):
		data = get_data()
		if id_user == True:
			return data["Contacts"][self.id_user][self.search]
		else:
			data = get_data()
			return data["Contacts"]


	### Añadimos un pedazo JSON a la base de datos // "Contacts" ###
	def add_data_piece(self, data, id_user = True):
		if id_user == True:
			self.data["Contacts"][self.id_user][self.search] = data
		else:
			self.data["Contacts"] = data

		add_from_json = write_data(self.data)
		return True

	######################
	####### _CRUD_ #######
	######################

	### Añadimos un nuevo contacto en la base de datos ###
	def add_new_user_contact(self, username):
		actualizar_data = self.update_data()
		data = self.data_piece(id_user = False)
		new_user = {"username" : username,
					"contact_list" : []}
		data.append(new_user)
		add_from_json = self.add_data_piece(data, id_user = False)
		return True


	### Elminamos un contacto de la base de datos ###
	def delete_contact(self, username):
		actualizar_data = self.update_data()
		data = self.data_piece(id_user = False)
		for i in data:
			if i["username"] == username:
				data.remove(i)
				write =  self.add_data_piece(data, id_user = False)
				return True


class Check():
	def __init__(self, block):
		self.block = block
		self.key_search = ""
		self.search = "contact_list"
		self.id_user = None


	def data_piece(self, id_user = True):
		if self.block == "Users":
			self.key_search = ("username", "email")
			data = get_data()
			return data["Users"]
		
		elif id_user == True:
			self.key_search = ("fullname", "email", "phone")
			data = get_data()
			return data["Contacts"][self.id_user][self.search]
		else:
			self.key_search = ("username") 
			data = get_data()
			return data["Contacts"]


	def search_item(self, check_dict, data):
		for i in self.key_search:
			for j in data:
				if check_dict[i] == j[i]:
					return True

		return False



	def login(self, check_dict, data):
		for i in data:
			boolean_password = check_password_hash(i["password"], check_dict["password"])
			boolean_username = i["username"] == check_dict["username"]
			if boolean_username and boolean_password:
				return True
		return False


	def get_id(self, check_dict, data):
		for i in data:
			if check_dict["username"] == i["username"]:
				return i["id"]

		return False







### Agregamos credenciales de Manager en la posicion 0 de la base de datos ###
def input_manager(username, password):
	data = get_data()
	data["Managers"] = [{"username" : username, "password" : password}]
	with open("data.json", "w") as json_file:
		json.dump(data, json_file, indent = 4)
	return data["Managers"]

### Comprobamos que el usuario (Manager) tenga las credenciales correctas ###
def check_manager(dict_manager):
	data = get_data()
	data = data["Managers"]
	for i in data: 
		username_bool = check_password_hash(i["username"], dict_manager["username"])
		password_bool = check_password_hash(i["password"], dict_manager["password"])
		#True, Si las crendenciales son correctas
		if username_bool and password_bool:
			return True

	return False


if __name__ == '__main__':
	from werkzeug.security import generate_password_hash, check_password_hash
	username = generate_password_hash("Yilver", "sha256")
	password = generate_password_hash("Bloyhu", "sha256")
	#print(input_manager(username, password))