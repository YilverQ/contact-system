-- Tablas SQL

-- 1. Crear base de datos;
CREATE DATABASE contacto;
use contacto;

-- 2. Crear Tablas.
-- 2.1 Usuario.
CREATE TABLE Usuario(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nombre varchar(30) NOT NULL,
	apellido varchar(30) NOT NULL,
	correoElectronico varchar(50) NOT NULL,
	clave varchar(30) NOT NULL
)ENGINE=InnoDB;

-- 2.2 Contacto.
CREATE TABLE Contacto(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	numTelefono varchar(30) NOT NULL,
	nombreContacto varchar(30) NOT NULL,
	idUsuario int(3),
	FOREIGN KEY (idUsuario) REFERENCES Usuario(id)
)ENGINE = InnoDB;