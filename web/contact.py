from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect
#from models.modelUser import Model_User
from models.modelContact import Model_Contact
from models.requestContact import data_request_POST



#blueprints
contactSite = Blueprint("contactSite", __name__)


#Objeto Global.
#obj_user = Model_User()
obj_contact = Model_Contact()

"""Rutas"""
#----------------------------------------------
#createContact
@contactSite.route("/contact", methods = ["GET", "POST"])
def create_contact():
   if request.method == "POST":
      id_user = request.cookies.get('userID')
      new_contact = data_request_POST(request.form, id_user)      
      message = obj_contact.create(new_contact, id_user)
      flash(f'{message}')
      return redirect(url_for('contactSite.read_contact'))

   data = {"title":"Create a contact"}
   return render_template('contact/create_contact.html', data=data)


#readContacts
@contactSite.route("/contacts")
def read_contact():
   id_user = request.cookies.get('userID')
   contacts = obj_contact.read(id_user)
   data = {"title":"Home", "contacts":contacts}
   return render_template('home.html', data=data)


#updateUser
@contactSite.route("/upd-contact/<int:id_contact>", methods = ["GET", "POST"])
def update_contact(id_contact):
   if request.method == 'POST':
      id_user = request.cookies.get('userID')
      new_contact = data_request_POST(request.form, id_user) #data from request (POST).
      message = obj_contact.update(id_contact, new_contact)
      flash(f'{message}')
      return redirect(url_for('contactSite.read_contact'))

   contact = obj_contact.read_only_id(id_contact)
   data = {"title":f"Update Contact by ID {id_contact}", "contact" : contact}
   return render_template('contact/update_contact.html', data=data)


#deleteUser
@contactSite.route("/del-contact/<int:id_contact>")
def delete_contact(id_contact):
   message = obj_contact.delete(id_contact)
   flash(f'{message}')
   return redirect(url_for('contactSite.read_contact'))