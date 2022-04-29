#Atendemos la petición POST o PUT para devolver un diccionario.
def data_request(jsonData):
	new_contact = {
		"num_phone" : jsonData["num_phone"],
		"name_contact" : jsonData["name_contact"],
		"id_user" : jsonData["id_user"],
	}
	return new_contact