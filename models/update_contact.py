from database.contactDB import ContactDB
"""
	data = { "num_phone" : "", "name_contact": "", "id_user" : ""}
"""
def check_update_contact(id_contact, exist_contact, new_data):
	#Global Data.
	objUpdate = ContactDB()
	id_user = new_data["id_user"]
	name = new_data["name_contact"]
	number = new_data["num_phone"]

	#Variables to know if the data exists.
	exist_name = objUpdate.read_name_contact(name, id_user)
	exist_number = objUpdate.read_num_phone(number, id_user)

	#In case the new data does not exist.
	if exist_name == None and exist_number == None: #The name and number do not exist.
		return True

	#If the data exists.
	if exist_name and exist_number:
		#In case the new data exists but is mine.
		if exist_number[1] == exist_contact[1] and exist_name[2] == exist_contact[2]: 
			return True
		return "The data is not available."

	#In case that the name already exist and the number not. 
	if exist_name:
		if exist_name[2] == exist_contact[2]: 
			return True
		return "The name is not available."

	#In case that the number already exist and the name not.
	if exist_number:
		if exist_number[1] == exist_contact[1]: 
			return True
		return "The number is not available."

	#In case that the data already exist but are not mine.
	else:
		return "The data is not available."