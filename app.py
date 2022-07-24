#Import Flask module.
from flask import Flask, render_template


#Imports all Blueprints
from api.userAPI import userAPI
from api.contactAPI import contactAPI
from web.user import userSite
from web.contact import contactSite


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



"""Rutas"""
#----------------------------------------------

""" Working """
#Home
@app.route("/")
def index():
	data = {"title":"Home"}
	return render_template('index.html', data=data)

#Login
@app.route("/login")
def login():
	data = {"title":"Login"}
	return render_template('login.html', data=data)


#Play the aplication in localhost.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)