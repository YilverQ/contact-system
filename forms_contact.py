from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

#form wtforms import Form, StringField, TextField
#from wtforms.fields.html5 import EmailField

def check_just_numbers(form, field):
	if field.data.isdigit() == False:
		raise validators.ValidationError("El Campo solo debe tener numeros")


class Login(FlaskForm):
	username = StringField(	"Username", [DataRequired(message = "Debe Ingresar un Dato"),
										Length(min = 4, max = 15, message = "Debe Ingresar un usuario de 6 a 15 caracteres.")])
	password = PasswordField("Password", [DataRequired(message = "Debe Ingresar Un Dato"),
										Length(min = 6, max = 15, message = "Debe Ingresar una Clave de 6 a 15 caracteres.")])
	submit = SubmitField("Submit")


class Signup(Login):
	email = StringField("Email", [DataRequired(message = "Debe Ingresar un Dato."),
								Email(message = "Debe Ingresar Un Correo Valido.")])

"""
class Google(Form):
	busqueda = StringField("Busqueda")
"""


class Contact(FlaskForm):
	fullname = StringField(	"Username", [DataRequired(message = "Debe Ingresar un Dato"),
										Length(min = 6, max = 15, message = "Debe Ingresar un usuario de 6 a 15 caracteres.")])
	email = StringField("Email", [Email(message = "Debe Ingresar Un Correo Valido.")])
	phone = StringField("Phone", [Length(min = 11, max = 11, message = "El Número de Télefono Debe Tener 11 Dígitos"), check_just_numbers])
	submit = SubmitField("Submit")
