#Import Flask module.
from flask import Flask
from flask import redirect, render_template, request, url_for, make_response, flash


#Imports all Blueprints
from api.userAPI import userAPI
from api.contactAPI import contactAPI
from web.user import userSite
from web.contact import contactSite
from web.login import register


#Import Model by aplication
from models.modelUser import Model_User
from models.requestUser import data_request
obj_user = Model_User()


#Flask Aplitacion.
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#Register Blueprint in Flask aplication.
app.register_blueprint(userAPI)
app.register_blueprint(contactAPI)
app.register_blueprint(userSite)
app.register_blueprint(contactSite)
app.register_blueprint(register)



"""Rutas"""
#----------------------------------------------

""" Working """
#Home
@app.route("/")
def index():
	#Comprobar usuario en coockie. 
	name = request.cookies.get('userID')
	if name == None:
		return redirect(url_for('register.login'))
	return redirect(url_for('contactSite.read_contact'))


#delete Coockie.
@app.route("/exit")
def exit():
	resp = make_response(redirect(url_for('register.login')))
	resp.delete_cookie('userID')
	flash(f'successful exit')
	return resp

#Play the aplication in localhost.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)