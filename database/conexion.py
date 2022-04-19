import mysql.connector
from mysql.connector import Error


"""DAO = Data Access Object"""
class DAO:
	"""Conexión con la base de datos"""
	def __init__(self):
		try: #Hace un intento de conexión
			self.conexion = mysql.connector.connect(
							host = "localhost",
							port = 3306,
							user = "root",
							password = "root",
							db = "contacto") #Datos para la conexión a la BD.
			self.cursor = self.conexion.cursor() #Cursos es fundamental para ejecurar sentencias SQL
		except Error as ex:
			print("Lo siento, ha ocurrido un error")
			print(f"Error: {ex}")