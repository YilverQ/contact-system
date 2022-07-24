import mysql.connector
from mysql.connector import Error


"""DAO = Data Access Object"""
class DAO:
	"""Connection with the database"""
	def __init__(self):
		try: #Try a connection.
			self.conexion = mysql.connector.connect(
							host = "localhost",
							port = 3306,
							user = "root",
							password = "root",
							db = "contact") #Data for to connection.
			self.cursor = self.conexion.cursor() #cursor is essential to execute SQL statements
		except Error as ex: #In case of connection failure
			print("Lo siento, ha ocurrido un error")
			print(f"Error: {ex}")