import re
from tkinter import messagebox
from datetime import datetime

# VALIDACIONES FORMULARIO 1

def mostrar_errores(errores):
    if errores:
        messagebox.showerror("ATENCIÓN", "\n".join(errores))

def validar_nombre_apellido(nombre, apellido, errores):
    if not nombre.isalpha():
        errores.append("El nombre debe ser escrito solo con letras.")
    elif len(nombre) < 2 or len(nombre) > 20:
        errores.append("El nombre debe tener entre 2 y 20 caracteres.")
    
    if not apellido.isalpha():
        errores.append("El apellido debe ser escrito solo con letras.")
    elif len(apellido) < 2 or len(apellido) > 20:
        errores.append("El apellido debe tener entre 2 y 20 caracteres.")

def validar_dni(dni, errores):
    if not dni.isdigit():
        errores.append("El DNI solo debe contener dígitos.")
    elif len(dni) < 7 or len(dni) > 8:
        errores.append("El número de DNI debe tener 7 u 8 dígitos.")

def validar_cuil(cuil, errores):
    if not cuil.isdigit():
        errores.append("El CUIL solo debe contener dígitos.")
    elif len(cuil) != 11:
        errores.append("El número de CUIL debe tener 11.")

def validar_domicilio(domicilio, errores):
    if len(domicilio) < 5 or len(domicilio) > 50:
        errores.append("El nombre debe tener entre 5 y 50 caracteres.")

def validar_provincia(provincia, errores):
    if provincia.get() == "" or provincia.get() == "Seleccione una provincia": 
        errores.append("Debes seleccionar una provincia.")

def validar_barrio(barrio, errores):
    if barrio.get() == "" or barrio.get() == "Seleccione un barrio": 
        errores.append("Debes seleccionar un barrio.")

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
        errores.append("El correo no es válido o no existe.")

def validar_fecha(fecha_entry, errores):
    fecha_seleccionada = fecha_entry.get_date()

    fecha_actual = datetime.now().date()

    if fecha_seleccionada < fecha_actual:
        errores.append("La fecha seleccionada no puede ser anterior a la fecha actual.")
    if fecha_seleccionada == "" or fecha_seleccionada == "Fecha de nacimiento":
        errores.append("La selección de una fecha es obligatoria.")


def validar_sexo(sexo, errores):
    if sexo.get() == "" or sexo.get() == "Seleccione su sexo": 
        errores.append("Debes seleccionar un sexo.")

def validar_pais_nacimiento(pais_nacimiento, errores):
    if pais_nacimiento.get() == "" or pais_nacimiento.get() == "Seleccione país de nacimiento": 
        errores.append("Debes seleccionar un país de nacimiento.")

def validar_provincia_nacimiento(provincia_nacimiento, errores):
    if provincia_nacimiento.get() == "" or provincia_nacimiento.get() == "Seleccione provincia de nacimiento": 
        errores.append("Debes seleccionar una provincia de nacimiento.")

def validar_ciudad_nacimiento(ciudad_nacimiento, errores):
    if ciudad_nacimiento.get() == "" or ciudad_nacimiento.get() == "Seleccione ciudad de nacimiento": 
        errores.append("Debes seleccionar una ciudad de nacimiento.")

def validar_campos_obligatorios(entries, errores):
    if any(entry.get().strip() == "" for entry in entries):
        errores.append("Todos los campos del formulario son obligatorios.")
    
# VALIDACIONES FORMULARIO 2

# Valida que solamente seleccione un checkbutton.
def validar_seleccion(check_medio_si, check_medio_no, check_superior_si, check_superior_no, check_trabaja_si, check_trabaja_no, errores):
    if (check_medio_si.get() == 1 and check_medio_no.get() == 1) or (check_medio_si.get() == 0 and check_medio_no.get() == 0):
        errores.append("Debes elegir solamente una opción para estudios medios.")

    if (check_superior_si.get() == 1 and check_superior_no.get() == 1) or (check_superior_si.get() == 0 and check_superior_no.get() == 0):
        errores.append("Debes elegir solamente una opción para estudios superiores.")
    
    if (check_trabaja_si.get() == 1 and check_trabaja_no.get() == 1) or (check_trabaja_si.get() == 0 and check_trabaja_no.get() == 0):
        errores.append("Debes elegir solamente una opción para situación laboral.")

# def validar_provincia_2(check_medio_si, check_superior_si, provincia_medio, provincia_superior, errores):
#     if check_medio_si.get() == 1: # Valida si tiene estudios medios.
#         if provincia_medio.get() == "" or provincia_medio.get() == "Seleccione una provincia":
#             errores.append("Debes seleccionar una provincia.")
#     if check_superior_si.get() == 1: # Valida si tiene estudios superiores.
#         if provincia_superior.get() == "" or provincia_superior.get() == "Seleccione una provincia": 
#             errores.append("Debes seleccionar una provincia.")

def nivel_medio(check_medio_si, provincia_medio, año_ingreso_medio, año_egreso_medio, titulo_medio, errores):
    if check_medio_si.get() == 1: # Valida si tiene estudios medios.
        

        if provincia_medio.get() == "" or provincia_medio.get() == "Seleccione una provincia":
            errores.append("Debes seleccionar una provincia.")

        if año_ingreso_medio.get() == "" or año_ingreso_medio.get() == "Seleccione año ingreso": 
            errores.append("Debes seleccionar un año de ingreso")
        if año_egreso_medio.get() == "" or año_egreso_medio.get() == "Seleccione año egreso": 
            errores.append("Debes seleccionar un año de egreso")

        if not titulo_medio.isalpha():
            errores.append("El título debe ser escrito solo con letras.")
        elif len(titulo_medio) < 5 or len(titulo_medio) > 30:
            errores.append("El nombre debe tener entre 5 y 30 caracteres.")

def nivel_superior(check_superior_si, check_superior_curso, carrera_superior, errores):
    if check_superior_si.get() == 1 or check_superior_curso == 1: # Valida si tiene estudios medios.

        if not carrera_superior.isalpha():
            errores.append("La carrera debe ser escrita solo con letras.")
        elif len(carrera_superior) < 5 or len(carrera_superior) > 30:
            errores.append("El nombre de la carreradebe tener entre 5 y 30 caracteres.")

