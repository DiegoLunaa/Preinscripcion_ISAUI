import re
from tkinter import messagebox
from datetime import datetime
import tkinter as tk
from db.funciones_db import dni_existe_en_db, correo_existe_en_db

def validar_entrada(texto):
    # Expresión regular que permite letras (incluyendo tildes) y espacios.
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
    return bool(re.match(patron, texto))

def validar_alfanumerico_espacios(texto):
# Expresión regular que permite letras, números y espacios.
    patron = r'^[a-zA-Z0-9\s]+$'
    return bool(re.match(patron, texto))

def validar_alfanumerico_pyc(texto):
# Se le añade punto y coma.
    patron = r'^[a-zA-Z0-9\s.,]+$'
    return bool(re.match(patron, texto))

# VALIDACIONES FORMULARIO 1

def mostrar_errores(errores, padre):
    if errores:
        messagebox.showerror("ATENCIÓN", "\n".join(errores), parent=padre)

def validar_nombre_apellido(nombre, apellido, errores):
    if not validar_entrada(nombre):
        errores.append("El nombre debe ser escrito solo con letras.")
    elif len(nombre) < 2 or len(nombre) > 20:
        errores.append("El nombre debe tener entre 2 y 20 caracteres.")
    
    if not validar_entrada(apellido):
        errores.append("El apellido debe ser escrito solo con letras.")
    elif len(apellido) < 2 or len(apellido) > 20:
        errores.append("El apellido debe tener entre 2 y 20 caracteres.")

def validar_dni(dni, errores):
    if not dni.isdigit():
        errores.append("El DNI solo debe contener dígitos.")
    elif len(dni) < 7 or len(dni) > 8:
        errores.append("El número de DNI debe tener 7 u 8 dígitos.")
    else:
        # Validar si el DNI ya existe en la base de datos
        if dni_existe_en_db(dni):
            errores.append("El DNI ya está registrado en el sistema.")    

def validar_cuil(cuil, errores):
    if not cuil.isdigit():
        errores.append("El CUIL solo debe contener dígitos.")
    elif len(cuil) != 11:
        errores.append("El número de CUIL debe tener 11 dígitos.")

def validar_domicilio(domicilio, errores):
    if not validar_alfanumerico_espacios(domicilio):
        errores.append("No se aceptan signos y/o caracteres no alfanuméricos en el domicilio.")
    if len(domicilio) < 5 or len(domicilio) > 50:
        errores.append("El domicilio debe tener entre 5 y 50 caracteres.")

def validar_localidad(localidad, errores):
    if localidad == "": 
        errores.append("Debes seleccionar una provincia.")

def validar_barrio(barrio, errores):
    if not validar_entrada(barrio):
        errores.append("El barrio debe ser escrito solo con letras.")
    elif len(barrio) < 2 or len(barrio) > 30:
        errores.append("El barrio debe tener entre 2 y 30 caracteres.")

def validar_codigo_postal(codigo_postal, errores):
    if not codigo_postal.isdigit():
        errores.append("El código postal solo debe contener dígitos.")
    elif len(codigo_postal) != 4:
        errores.append("El código postal debe tener 4 dígitos")

def validar_telefono(telefono, errores):
    if not telefono.isdigit():
        errores.append("El teléfono solo debe contener dígitos.")
    elif len(telefono) < 6 or len(telefono) > 10:
        errores.append("El número de teléfono debe tener entre 6 y 10 dígitos.")

def verificar_correo(correo, errores):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, correo):
        errores.append("El correo ingresado no tiene un formato válido.")
    else:
        # Validar si el correo ya existe en la base de datos
        if correo_existe_en_db(correo):
            errores.append("El correo ya está registrado en el sistema.")

def validar_fecha(fecha_nacimiento, errores):

    fecha_actual = datetime.now().date()

    if fecha_nacimiento >= fecha_actual:
        errores.append("La fecha de nacimiento no puede ser posterior o igual a la fecha actual.")
    if fecha_nacimiento == "":
        errores.append("Debes seleccionar una fecha de nacimiento.")


def validar_sexo(sexo, errores):
    if sexo == "...": 
        errores.append("Debes seleccionar un sexo.")

def validar_pais_nacimiento(pais_nacimiento, errores):
    if not validar_entrada(pais_nacimiento):
        errores.append("El país de nacimiento debe ser escrito con letras")
    if pais_nacimiento == "": 
        errores.append("Debes seleccionar un país de nacimiento.")

def validar_provincia_nacimiento(provincia_nacimiento, errores):
    if not validar_entrada(provincia_nacimiento):
        errores.append("La provincia de nacimiento debe ser escrita con letras")
    elif provincia_nacimiento == "": 
        errores.append("Debes seleccionar una provincia de nacimiento.")

def validar_ciudad_nacimiento(ciudad_nacimiento, errores):
    if not validar_entrada(ciudad_nacimiento):
        errores.append("La ciudad de nacimiento debe ser escrita con letras")
    elif ciudad_nacimiento == "": 
        errores.append("Debes seleccionar una ciudad de nacimiento.")

def validar_campos_obligatorios(entries, errores):
    if any(
        (entry.get("1.0", "end").strip() if isinstance(entry, tk.Text) else entry.get().strip()) == ""
        for entry in entries
    ):
        errores.append("Todos los campos del formulario son obligatorios.")
  
# VALIDACIONES FORMULARIO 2

def validar_nivel_medio(nivel_medio, provincia_medio, año_ingreso_medio, año_egreso_medio, titulo_medio, errores):
    if nivel_medio == 1: # Valida si tiene estudios medios.

        if provincia_medio == "...":
            errores.append("Debes seleccionar una provincia en el nivel medio.")

        if año_ingreso_medio == "": 
            errores.append("Debes seleccionar un año de ingreso medio")
        if año_egreso_medio == "": 
            errores.append("Debes seleccionar un año de egreso medio")

        if not validar_entrada(titulo_medio):
            errores.append("El título debe ser escrito solo con letras.")
        elif len(titulo_medio) < 1 or len(titulo_medio) > 100:
            errores.append("El título debe tener entre 1 y 1000 caracteres.")
            

def validar_nivel_superior(nivel_superior, carrera_superior, institucion, provincia_superior, año_ingreso_superior, año_egreso_superior, errores):
    if nivel_superior in [1,2]:

        if not validar_entrada(carrera_superior):
            errores.append("La carrera debe ser escrita solo con letras.")
        elif len(carrera_superior) < 1 or len(carrera_superior) > 100:
            errores.append("El nombre de la carrera debe tener entre 1 y 100 caracteres.")

        if not validar_entrada(institucion):
            errores.append("La institución debe ser escrita solo con letras.")
        elif len(institucion) < 1 or len(institucion) > 100:
            errores.append("El nombre de la institución debe tener entre 1 y 100 caracteres.")
        
        if provincia_superior == "":
            errores.append("Debes seleccionar una provincia en el nivel superior.")
        
        if año_ingreso_superior == "": 
            errores.append("Debes seleccionar un año de ingreso superior")
        if nivel_superior == 1:
            if año_egreso_superior == "": 
                errores.append("Debes seleccionar un año de egreso superior")
        
def validar_situacion_laboral(check_trabaja_si, horas_lab, descripcion_laboral, errores):
    if check_trabaja_si == 1:
        # Validación de las horas laborales
        try:
            horas = int(horas_lab)
            if horas < 1 or horas > 24:
                errores.append("Las horas diarias trabajadas no pueden ser superiores a 24.")
        except ValueError:
            errores.append("Las horas deben ser escritas solo con dígitos.")

        if descripcion_laboral == "":
            errores.append("Se debe ingresar una breve descripción sobre el trabajo.")
        elif not validar_alfanumerico_pyc(descripcion_laboral):
            errores.append("No se aceptan signos y/o caracteres no alfanuméricos en la descripción laboral.")
        elif len(descripcion_laboral) < 5 or len(descripcion_laboral) > 300:
            errores.append("La descripción debe tener entre 5 y 300 caracteres.")