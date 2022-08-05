#We attend the POST or PUT request to return a dictionary.
def data_request(jsonData):
	new_contact = {
		"num_phone" : jsonData["num_phone"],
		"name_contact" : jsonData["name_contact"],
		"id_user" : jsonData["id_user"]
	}
	return new_contact


def data_request_POST(request, id_user):
	new_contact = {
		"num_phone" : request.get("num_phone"),
		"name_contact" : request.get("name_contact"),
		"id_user" : id_user
	}
	return new_contact