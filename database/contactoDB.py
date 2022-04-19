from database.conexion import DAO


class ContactoDB(DAO):
	"""CRUD Contacto"""
	##########################################
	#Obtiene una lista completa de los contactos.
	def read_contacto(self):
		self.cursor.execute("Select * from Contacto;")
		return self.cursor.fetchall()


	#Crea un contacto con los datos pasados.
	def create_contacto(self, datos):
		"""
			datos = {
				"numTelefono" : 	"",
				"nombreContacto": 	"", 
				"idUsuario" : 		""}
		"""
		usuario = """Insert INTO Contacto (numTelefono, nombreContacto, idUsuario)"""
		values 	= f"""VALUES ('{datos["numTelefono"]}', '{datos["nombreContacto"]}', '{datos["idUsuario"]}');"""
		texto 	= usuario + " " + values
		self.cursor.execute(texto)
		self.conexion.commit()
		return "Contacto Registrado Sastifactoriamente"


	#Actualiza los datos de un contacto.
	def update_contacto(self, idContacto, datos):
		"""
			datos = {
				"numTelefono" : 	"",
				"nombreContacto": 	"", 
				"idUsuario" : 		""}
		"""
		datosUpdate = f"""numTelefono = '{datos["numTelefono"]}', nombreContacto = '{datos["nombreContacto"]}', idUsuario = '{datos["idUsuario"]}'"""
		texto 	= f"Update Contacto set {datosUpdate} WHERE id = {idContacto};";
		print(texto)
		self.cursor.execute(texto)
		self.conexion.commit()
		return "Contacto Actualizado Sastifactoriamente"


	#Elimina una fila de la tabla contacto.
	def delete_contacto(self, idContacto):
		texto = f"""Delete FROM Contacto WHERE id = {idContacto};"""
		self.cursor.execute(texto)
		self.conexion.commit()
		return f"Contacto {idContacto} Ha Sido Eliminado Sastifactoriamente"


	#Retorna todos los usuarios con el idContacto.
	def read_contactos_by(self, idUsuario):
		texto = f"Select * FROM Contacto WHERE idUsuario = '{idUsuario}';"
		self.cursor.execute(texto)
		return self.cursor.fetchall()


	#Comprueba que el número de teléfono exista.
	def read_telefono(self, telefono, idUsuario):
		texto = f"Select * FROM Contacto WHERE numTelefono = '{telefono}' and idUsuario = {idUsuario};"
		self.cursor.execute(texto)
		return self.cursor.fetchall()


	#Comprueba que el nombre del contacto exista.
	def read_nombre(self, nombre, idUsuario):
		texto = f"Select * FROM Contacto WHERE nombreContacto = '{nombre}' and idUsuario = {idUsuario};"
		self.cursor.execute(texto)
		return self.cursor.fetchall()


	#Comprueba que el idContacto de contacto exista.
	def read_idContacto(self, idContacto):
		texto = f"Select * FROM Contacto WHERE id = '{idContacto}';"
		self.cursor.execute(texto)
		return self.cursor.fetchone()