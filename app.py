#Importar módulos.
from flask import Flask

#importar Blueprint
from api.userAPI import userAPI
from api.contactAPI import contactAPI
from web.user import userSite
from web.contact import contactSite

#Aplicación Flask.
app = Flask(__name__)

#Registar rutas externar con Blueprint
app.register_blueprint(userAPI)
app.register_blueprint(contactAPI)
app.register_blueprint(userSite)
app.register_blueprint(contactSite)


#Ejecución Del Programa.
if __name__ == "__main__":
	app.run(debug = True, host = "127.0.0.1", port = 5000)