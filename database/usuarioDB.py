from database.conexion import DAO


class UsuarioDB(DAO):
	"""CRUD-Usuario"""
	###########################################
	#Obtiene una lista completa de los usuarios.
	def read_usuarios(self):
		self.cursor.execute("Select * from Usuario;")
		return self.cursor.fetchall() #Obtiene todos las filas de la tabla. 


	#Crea un usuario con los datos pasados.
	def create_usuario(self, datos):
		"""
			datos = {
				"nombre" : "", "apellido" : "",
				"correoElectronico": "", "clave" : ""}
		"""
		insert = """Insert INTO Usuario (nombre, apellido, correoElectronico, clave)"""
		values 	= f"""VALUES ('{datos["nombre"]}', '{datos["apellido"]}', '{datos["correoElectronico"]}', '{datos["clave"]}');"""
		texto 	= insert + " " + values #Texto es la sentencia SQL a ejecutar.
		self.cursor.execute(texto)
		self.conexion.commit()
		return "Usuario Registrado Sastifactoriamente"


	#Actualiza los datos de un usuario.
	def update_usuario(self, idUsuario, datos):
		"""
			datos = {
				"nombre" : "", "apellido" : "",
				"correoElectronico": "", "clave" : ""}
		"""
		datosUpdate = f"""nombre = '{datos["nombre"]}', apellido = '{datos["apellido"]}', correoElectronico = '{datos["correoElectronico"]}', clave = '{datos["clave"]}'"""
		texto 	= f"Update Usuario set {datosUpdate} WHERE id = {idUsuario}"; 
		self.cursor.execute(texto) #Se actualiza toda la fila.
		self.conexion.commit()
		return "Usuario Actualizado Sastifactoriamente"


	#Elimina una fila de la tabla usuario.
	def delete_usuario(self, idUsuario):
		texto = f"""Delete FROM Usuario WHERE id = {idUsuario};"""
		self.cursor.execute(texto) #Elimina toda la fila.
		self.conexion.commit()
		return f"Usuario {idUsuario} Ha Sido Eliminado Sastifactoriamente"


	#Obtiene solo la fila donde se encuentra el correoElectronico.
	def read_mail_usuario(self, correoElectronico):
		texto = f"Select * FROM Usuario WHERE correoElectronico = '{correoElectronico}';"
		self.cursor.execute(texto)
		return self.cursor.fetchone() #retorna una sola fila


	#Obtiene la fila del usuario con el id pasado como parametro.
	def obtener_id_usuario(self, idContacto):
		texto = f"Select * FROM Usuario WHERE id = '{idContacto}';"
		self.cursor.execute(texto)
		return self.cursor.fetchall() #retorna muchas filas.