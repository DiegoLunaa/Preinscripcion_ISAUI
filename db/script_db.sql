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
    Pais_Nacimiento VARCHAR(100),
    Provincia_Nacimiento VARCHAR(100),
    Localidad_Nacimiento VARCHAR(100),
    Completo_Nivel_Medio TINYINT DEFAULT 0,
    Año_Ingreso_Medio INT DEFAULT NULL,
    Año_Egreso_Medio INT DEFAULT NULL,
    Provincia_Medio VARCHAR(100) DEFAULT NULL,
    Titulo_Medio VARCHAR(100) DEFAULT NULL,
    Completo_Nivel_Superior TINYINT DEFAULT 0,
    Carrera_Superior VARCHAR(100) DEFAULT NULL,
    Institucion_Superior VARCHAR(100) DEFAULT NULL,
    Provincia_Superior VARCHAR(100) DEFAULT NULL,
    Año_Ingreso_Superior INT DEFAULT NULL,
    Año_Egreso_Superior INT DEFAULT NULL,
    Trabajo TINYINT DEFAULT 0,
    Horas_Trabajo INT DEFAULT NULL,
    Descripcion_Trabajo TEXT DEFAULT NULL,
    Personas_Cargo TINYINT DEFAULT 0,
    Estado VARCHAR(20) DEFAULT 'Pendiente',
    Fecha_Envio DATETIME DEFAULT NULL,
    ID_Carrera INT,
    Activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (ID_Carrera) REFERENCES Carrera(ID_Carrera)
);

CREATE TABLE Carrera (
    ID_Carrera INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_Carrera VARCHAR(255),
    Duracion INT,
    Facultad VARCHAR(100),
    Cupos_Disponibles INT,
    Cupos_Maximos INT
);

CREATE TABLE Administrador (
    ID_Administrador INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    Cargo VARCHAR(100),
    Usuario VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Insertar carreras
INSERT INTO Carrera (Nombre_Carrera, Duracion, Facultad, Cupos_Disponibles, Cupos_Maximos) VALUES
('Tecnicatura Superior en Desarrollo de Software', 3, 'ISAUI', 50, 60),
('Tecnicatura Superior en Diseño de Espacios', 3, 'ISAUI', 50, 60),
('Tecnicatura Superior en Enfermería', 3, 'ISAUI', 50, 60),
('Tecnicatura Superior en Turismo y Hotelería', 3, 'ISAUI', 50, 60),
('Tecnicatura Superior en Guía de Turismo', 3, 'ISAUI', 50, 60),
('Tecnicatura Superior en Guía de Trekking y Guía de Turismo', 3, 'ISAUI', 50, 60);

-- Insertar administrador
INSERT INTO Administrador (Nombre, Apellido, Cargo, Usuario, Password) VALUES
('Jorge', 'Aperlo', 'Administrador', 'admin', '$2b$12$UzRFtiVFgRqynR9PLlOw9ONxli4T0YW/s.hq7RwuXg6BLGZjt06lm'),
('admin', 'admin', 'Administrador', 'adm', '$2b$12$g65hJdyYvneSALBS.3bQNeAwaZkxkeyLp9Hj2rxV3v1f2SP36zply');