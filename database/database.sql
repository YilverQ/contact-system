-- Tables SQL

-- 1. Create a database;
CREATE DATABASE contact;
use contact;

-- 2. Create Tables.
-- 2.1 User.
CREATE TABLE User(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	email varchar(50) NOT NULL,
	password varchar(30) NOT NULL
)ENGINE=InnoDB;

-- 2.2 Contact.
CREATE TABLE Contact(
	id int(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	num_phone varchar(30) NOT NULL,
	name_contact varchar(30) NOT NULL,
	id_user int(3),
	FOREIGN KEY (id_user) REFERENCES User(id)
)ENGINE = InnoDB;