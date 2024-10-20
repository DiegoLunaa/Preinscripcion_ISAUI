CREATE DATABASE isaui_prematricula;

USE isaui_prematricula;

CREATE TABLE Aspirante (
    ID_Aspirante INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    DNI VARCHAR(20) UNIQUE,
    Genero VARCHAR(10),
    CUIL VARCHAR(20),
    Domicilio VARCHAR(255),
    Barrio VARCHAR(100),
    Localidad VARCHAR(100),
    Codigo_Postal VARCHAR(10),
    Telefono VARCHAR(15),
    Mail VARCHAR(100) UNIQUE,
    Fecha_Nacimiento DATE,
    Lugar_Nacimiento VARCHAR(100),
    Completo_Nivel_Medio BOOLEAN,
    Año_Ingreso_Medio INT,
    Año_Egreso_Medio INT,
    Provincia_Medio VARCHAR(100),
    Titulo_Medio VARCHAR(100),
    Completo_Nivel_Superior VARCHAR(100),
    Carrera_Superior VARCHAR(100),
    Institucion_Superior VARCHAR(100),
    Provincia_Superior VARCHAR(100),
    Año_Ingreso_Superior INT,
    Año_Egreso_Superior INT,
    Trabajo BOOLEAN,
    Descripcion_Trabajo TEXT,
    Personas_Cargo BOOLEAN
);

CREATE TABLE Carrera (
    ID_Carrera INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Carrera VARCHAR(255),
    Duracion INT,
    Facultad VARCHAR(100),
    Cupos_Disponibles INT
);

CREATE TABLE Formulario (
    ID_Formulario INT PRIMARY KEY AUTO_INCREMENT,
    Fecha_Envio DATE,
    Estado VARCHAR(20),
    Constancia_URL TEXT,
    ID_Aspirante INT,
    ID_Carrera INT,
    FOREIGN KEY (ID_Aspirante) REFERENCES Aspirante(ID_Aspirante),
    FOREIGN KEY (ID_Carrera) REFERENCES Carrera(ID_Carrera)
);

CREATE TABLE Administrador (
    ID_Administrador INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    Cargo VARCHAR(100),
    Usuario VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Reporte (
    ID_Reporte INT PRIMARY KEY AUTO_INCREMENT,
    Fecha_Creacion DATE,
    Descripcion TEXT,
    URL_Reporte TEXT,
    ID_Administrador INT,
    FOREIGN KEY (ID_Administrador) REFERENCES Administrador(ID_Administrador)
);

CREATE TABLE Constancia (
    ID_Constancia INT PRIMARY KEY AUTO_INCREMENT,
    Fecha_Generacion DATE,
    URL_Constancia TEXT,
    Mensaje_Personalizado TEXT,
    ID_Formulario INT,
    FOREIGN KEY (ID_Formulario) REFERENCES Formulario(ID_Formulario)
);

-- Insertar carreras
INSERT INTO Carrera (Nombre_Carrera, Duracion, Facultad, Cupos_Disponibles) VALUES
('Tecnicatura Superior en Desarrollo de Software', 3, 'ISAUI', 50),
('Tecnicatura Superior en Diseño de Espacios', 3, 'ISAUI', 50),
('Tecnicatura Superior en Enfermería', 3, 'ISAUI', 50),
('Tecnicatura Superior en Turismo y Hotelería', 3, 'ISAUI', 50),
('Tecnicatura Superior en Guía de Turismo', 3, 'ISAUI', 50),
('Tecnicatura Superior en Guía de Trekking y Guía de Turismo', 3, 'ISAUI', 50);

-- Insertar administrador
INSERT INTO Administrador (Nombre, Apellido, Cargo, Usuario, Password) VALUES
('Jorge', 'Aperlo', 'Administrador', 'admin', '$2b$12$UzRFtiVFgRqynR9PLlOw9ONxli4T0YW/s.hq7RwuXg6BLGZjt06lm');
VALUES ('admin', 'admin', 'Administrador', 'adm', '$2b$12$g65hJdyYvneSALBS.3bQNeAwaZkxkeyLp9Hj2rxV3v1f2SP36zply');

ALTER TABLE Aspirante
MODIFY Completo_Nivel_Medio TINYINT DEFAULT 0,
MODIFY Año_Ingreso_Medio INT DEFAULT NULL,
MODIFY Año_Egreso_Medio INT DEFAULT NULL,
MODIFY Provincia_Medio VARCHAR(100) DEFAULT NULL,
MODIFY Titulo_Medio VARCHAR(100) DEFAULT NULL,
MODIFY Completo_Nivel_Superior TINYINT DEFAULT 0,
MODIFY Carrera_Superior VARCHAR(100) DEFAULT NULL,
MODIFY Institucion_Superior VARCHAR(100) DEFAULT NULL,
MODIFY Provincia_Superior VARCHAR(100) DEFAULT NULL,
MODIFY Año_Ingreso_Superior INT DEFAULT NULL,
MODIFY Año_Egreso_Superior INT DEFAULT NULL,
MODIFY Trabajo TINYINT DEFAULT 0,
MODIFY Descripcion_Trabajo TEXT DEFAULT NULL,
MODIFY Personas_Cargo TINYINT DEFAULT 0;

ALTER TABLE Aspirante 
CHANGE COLUMN Lugar_Nacimiento Pais_Nacimiento VARCHAR(100);

ALTER TABLE Aspirante 
ADD COLUMN Provincia_Nacimiento VARCHAR(100) AFTER Pais_Nacimiento,
ADD COLUMN Localidad_Nacimiento VARCHAR(100) AFTER Ciudad_Nacimiento,
ADD COLUMN Horas_Trabajo INT DEFAULT NULL AFTER Trabajo;

ALTER TABLE Carrera ADD COLUMN Cupos_Maximos INT;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 1;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 2;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 3;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 4;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 5;
UPDATE Carrera SET Cupos_Maximos = 60 WHERE ID_Carrera = 6;