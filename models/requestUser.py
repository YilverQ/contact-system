#Atendemos la petición POST o PUT para devolver un diccionario.
def data_request(jsonData):
	new_user = {
		"name" : jsonData["name"],
		"last_name" : jsonData["last_name"],
		"email" : jsonData["email"],
		"password" : jsonData["password"]
	}
	return new_user