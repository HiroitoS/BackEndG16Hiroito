-- SQL > structured Query Lenguage
-- DDL
-- Data Definition Language(Lenaguaje de definicion de Datos)
-- Sirve para indicar como se almacenaran los datos, osea paradefinir las columnas, 
-- tablas entre otros
-- Los comandos en SQL tienen que finalizar con ;

-- IF NOT EXISTS sirve para comando de creacion (BD, TABLAS, COLUMNAS)
CREATE DATABASE IF NOT EXISTS pruebas;
-- seleccionamos en que base de datos vamos a trabajar
USE pruebas;
CREATE TABLE personas(
	id 					INT 	PRIMARY KEY AUTO_INCREMENT, 
    nombre  			TEXT	NULL,
    apellido			VARCHAR(50),
    fecha_nacimiento	DATE,
    nacionalidad		VARCHAR(100) DEFAULT 'PERUANO'
);

-- DML 
-- Data manipulation Language (Lenaguaje de manipulacion de Datos)

-- Agregar informacion a la tabla
INSERT INTO personas(id, nombre, apellido, fecha_nacimiento) VALUES
					(DEFAULT, 'Hiroito', 'Sanchez', '1987-09-15');
-- Si no declaro las columnas que voy a insertar me veo en la obligacion de colocar valores
-- a todas las columnas y siguiendo el mismo orden que usa el momento de crear la tabla
INSERT INTO personas VALUES (DEFAULT, 'Levi', 'Sanchez', '2004-07-03', 'URUGUAYO');

INSERT INTO personas VALUES (DEFAULT, 'Eduardo', 'de Rivero', '1992-08-01', 'PERUANO');

INSERT INTO personas(nombre, apellido, fecha_nacimiento, nacionalidad) VALUES
					('Bryan', 'Urquizo', '1995-02-14', 'PERUANO'),
                    ('Maria', 'Retamozo', '1989-06-14', 'SALVADOREÑA');

SELECT id, nombre FROM personas;

SELECT * FROM personas;

SELECT * -- columnas
FROM personas -- tabla
WHERE nombre = 'Hiroito'; -- Condicional

SELECT *
FROM personas 
WHERE nacionalidad = 'PERUANO' AND id = 6;

SELECT * FROM personas WHERE nombre LIKE '%a%'; -- %> no interesa donde se encuentre el caracater

SELECT * FROM persaonas WHERE nombre LIKE '__u%';



-- devolver todas las personas cuyo nombre tengan la letra 'r' o en su apellido tenga la letra 'a'

SELECT * FROM personas WHERE nombre LIKE '%r%' OR apellido LIKE '%a%';

SELECT * FROM personas WHERE id IN (1,2,3);
SELECT * FROM personas WHERE id=1 OR id=2 OR id=3;


SELECT * FROM personas
LIMIT 2 -- 2 ELEMENTOS POR PAGINA
OFFSET 4; -- oFFSET  sirve para indicar cuantos se tiene que saltar 

-- Actualizaciones 
UPDATE personas 
SET nombre = 'Yasiel', apellido = 'Escobar' 
WHERE id = 5;

SELECT * FROM personas;

DELETE FROM personas WHERE id = 4;


-- DIRECCIONES

