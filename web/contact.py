from flask import Blueprint

contactSite = Blueprint("contactSite", __name__)

#createContact
@contactSite.route("/contact")
def create_user():
	data = {"title":"Create User"}
	return render_template('singUp.html', data=data)


#readContact
#updateUser
#deleteUser
#readContact