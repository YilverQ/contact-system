#We attend the POST or PUT request to return a dictionary
def data_request(jsonData):
	new_user = {
		"name" : jsonData["name"],
		"last_name" : jsonData["last_name"],
		"email" : jsonData["email"],
		"password" : jsonData["password"]
	}
	return new_user

def data_request_POST(request):
	new_user = {
		"name" : request.get("name"),
		"last_name" : request.get("last_name"),
		"email" : request.get("email"),
		"password" : request.get("password")
	}
	return new_user
