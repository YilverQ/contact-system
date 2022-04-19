#App.py ------- Importando Modulos Necesarios
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request
from flask import session
from forms_contact import Login, Signup, Contact
import model
import json



# Configuración de la Aplicación #
app = Flask(__name__)
app.secret_key = "Llave Secreta Para Nuestro Proyecto"



# Objetos del Modelo #
obj_user = model.User()
obj_contact = model.Contact()
check_user = model.Check("Users")
check_contact = model.Check("Contacts")



###########################
###### Login System #######
###########################
@app.route("/")
def index():
	data_HTML = {"title" : f"Home 'Index HTML' "}
	return render_template("index.html", data = data_HTML)


@app.route("/home/admin")
def homeAdmin():
	if "admin_username" in session:
		data_HTML = {"title" : f"Home admin {session['admin_username']}"}
		return render_template("index.html", data = data_HTML)
	return redirect(url_for("login_manager"))


@app.route("/home")
def home():
	if "username" in session:
		return f"{session['username']} and {session['id']}"
	return redirect(url_for("login"))


@app.route("/login/admin", methods = ["GET", "POST"])
def login_manager():
	data_HTML = {"title" : "Ingresar Credenciales", "redirect" : "/login/admin"}
	form = Login()
	if form.validate_on_submit():
		manager = {	"id" : None,
					"username" : form.username.data,
					"password" : form.password.data}
		if model.check_manager(manager):
			session["admin_username"] = manager["username"]
			session["password"] = manager["password"]

			return redirect(url_for("homeAdmin"))
		return "User has not Credentials admited!"
	return render_template("login.html", data = data_HTML, form = form)



@app.route("/login", methods = ["GET", "POST"])
def login():
	data_HTML = {"title" : "Ingresar Credenciales", "redirect" : "/login"}
	form = Login()
	if form.validate_on_submit():
		user_credentials = {"id" : None,
							"username" : form.username.data,
							"password" : form.password.data}
		dataJSON = check_user.data_piece()
		if check_user.login(user_credentials, dataJSON):
			session["username"] = user_credentials["username"]
			session["id"] = check_user.get_id(user_credentials, dataJSON)
			print(session["id"])
			return redirect(url_for("home"))
		return "The Credentials to user has Invalidated!"
	return render_template("login.html", data = data_HTML, form = form)


@app.route("/logout")
def logout():
	if "admin_username" in session:
		session.pop("admin_username")
		return redirect(url_for("login_manager"))
	elif "username" in session:
		session.pop("username")
		session.pop("id")
		return redirect(url_for("login"))




######################
# Rutas USERS SYSTEM #
######################
@app.route("/signup", methods = ["GET", "POST"])
def create_user():
	data_HTML = {"title" : "Create New User"}
	form = Signup()
	if form.validate_on_submit():

		new_user = {"id" : None,
				 	"username" 	: form.username.data,
				 	"email" 	: form.email.data,
				 	"password" 	: form.password.data}
		dataJSON = check_user.data_piece()
		if not check_user.search_item(new_user, dataJSON):
			new_user["password"] = generate_password_hash(new_user["password"], "sha256")
			create_user = obj_user.add(new_user)
			create_user_contact = obj_contact.add_new_user_contact(new_user["username"])
			if "admin_username" in session:
				return "User has Created Successfully!"

			return redirect(url_for("index"))
		return "User has Exist!"
	return render_template("signup.html", data = data_HTML, form = form)


@app.route("/read_users")
def read_users():
	if "admin_username" in session:
		data_HTML = {"title" : "Read Users In Database"}
		users = obj_user.get_all_items()
		return {"Usuarios": users}
	
	return redirect(url_for("login_manager"))


@app.route("/read_user/<string:user>")
def search_user(user):
	if "admin_username" in session:
		data_HTML = {"title" : f"{user}'s Data User"}
		user_data = obj_user.get_item(user)
		return user_data

	return redirect(url_for("login_manager"))


@app.route("/update_user/<string:user>", methods = ["GET", "POST"])
def update_user(user):
	if "admin_username" in session:
		data_HTML = {"title" : f"Update Data User From {user}"}
		form = Signup()
		if form.validate_on_submit():
			new_user = {"id" : None,
						"username" 	: form.username.data,
						"email" 	: form.email.data,
						"password" 	: form.password.data}

			new_user["password"] = generate_password_hash(new_user["password"], "sha256")
			update = obj_user.update(user, new_user)
			return "User has Updated Successfully!"

		dataJSON = check_user.data_piece()
		new_user = {"username" 	: user,
					"email" 	: ""}

		if check_user.search_item(new_user, dataJSON):
			return render_template("signup.html", data = data_HTML, form = form)
		return f"User Not Exist! .--. {user}"

	return redirect(url_for("login_manager"))


##################################################################################################33Debemos revisar
##################################################################################################33Debemos revisar
@app.route("/delete_user/<string:user>")
def delete_user(user):
	if "admin_username" in session:
		data_HTML = {"title" : f"Delete user {user}"}
		delete_user = obj_user.delete_item(user)
		return "User has deleted successfully!"

	return redirect(url_for("login_manager"))



########################
# Rutas Contact System #
########################
@app.route("/create_contact", methods = ["GET", "POST"])
def create_contact():
	if "username" in session:
		data_HTML = {"title" : "Create New Contact"}
		form = Contact()
		if form.validate_on_submit():

			new_contact = {	"id" : None,
					 		"fullname" 	: form.fullname.data,
					 		"email" 	: form.email.data,
					 		"phone" 	: form.phone.data}
			

			new_id = obj_contact.where_id_user(session["id"] - 1)
			check_contact.id_user = new_id
			print(check_contact.id_user)
			dataJSON = check_contact.data_piece()
			if not check_contact.search_item(new_contact, dataJSON):
				create_contact = obj_contact.add(new_contact)
				return redirect(url_for("home"))
			
			return "Contact has Exist!"
		return render_template("create_contact.html", data = data_HTML, form = form)

	return redirect(url_for("login"))


@app.route("/read_contacts")
def read_contacts():
	if "username" in session:
		data_HTML = {"title" : "Read Users In Database"}
		users = obj_user.get_all_items()
		return {"Usuarios": users}
		#return users

	return redirect(url_for("login"))


@app.route("/read_contacts/<string:contact>")
def search_contact(contact):
	if "username" in session:
		data_HTML = {"title" : f"{contact}'s Data User"}
		contact_data = obj_contact.get_item(contact)
		return contact_data

	return redirect(url_for("login"))


@app.route("/update_contact/<string:contact>", methods = ["GET", "POST"])
def update_contact(contact):
	if "username" in session:
		data_HTML = {"title" : f"Update Data contact From {contact}"}
		form = Contact()
		if form.validate_on_submit():
			new_contact = {"id" : None,
						"username" 	: form.fullname.data,
						"email" 	: form.email.data,
						"password" 	: form.phone.data}

			new_contact["password"] = generate_password_hash(new_contact["password"], "sha256")
			update = obj_contact.update(contact, new_contact)
			return "Contact has Updated Successfully!"

		contactJSON = model.struct_contact
		contactJSON["fullname"] = contact
		if model.check_contact(contactJSON):
			return render_template("create_contact.html", data = data_HTML, form = form)
		return f"User Not Exist! .--. {contact}"

	return redirect(url_for("login"))


@app.route("/delete_contact/<string:contact>")
def delete_contact(contact):
	if "username" in session:
		data_HTML = {"title" : f"Delete contact {contact}"}
		delete_contact = obj_contact.delete_item(contact)
		return "Contact has deleted successfully!"

	return redirect(url_for("login"))


if __name__ == '__main__':
	app.run(debug = True, port = 5000)

#192.168.43.7


