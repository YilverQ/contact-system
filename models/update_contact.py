from database.contactDB import ContactDB
"""
	data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
"""
def check_update_contact(id_contact, exist_contact, new_data):
	#Datos Globales.
	objUpdate = ContactDB()
	id_user = new_data["id_user"]
	name = new_data["name_contact"]
	number = new_data["num_phone"]

	#Variables para conocer si existe el dato.
	exist_name = objUpdate.read_name_contact(name, id_user)
	exist_number = objUpdate.read_num_phone(number, id_user)

	#En caso de que los nuevos datos no existan.
	if exist_name == None and exist_number == None: #El nombre ni numero existen.
		return True

	#En caso de que los datos existan.
	if exist_name and exist_number:
		#En caso de que los nuevos datos existan pero sean mios.
		if exist_number[1] == exist_contact[1] and exist_name[2] == exist_contact[2]: 
			return True
		return "Los datos no están disponibles"

	#En caso de que exista el nombre y no el número.
	if exist_name:
		if exist_name[2] == exist_contact[2]: 
			return True
		return "2 El nombre no está disponible"

	#En caso de que exista el número y no el nombre.
	if exist_number:
		if exist_number[1] == exist_contact[1]: 
			return True
		return "El número no está disponible"

	#En caso de que los datos existan pero no sean mios.
	else:
		return "2 Los datos no están disponibles"