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
        errores.append("El domicilio debe tener entre 5 y 50 caracteres.")

def validar_provincia(provincia_personal, errores):
    if provincia_personal == "": 
        errores.append("Debes seleccionar una provincia.")

def validar_barrio(barrio, errores):
    if barrio == "": 
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
        errores.append("El correo ingresado no tiene un formato válido.")

def validar_fecha(fecha_nacimiento, errores):

    fecha_actual = datetime.now().date()

    if fecha_nacimiento >= fecha_actual:
        errores.append("La fecha de nacimiento no puede ser mayor o igual a la fecha actual.")
    if fecha_nacimiento == "":
        errores.append("La selección de una fecha es obligatoria.")


def validar_sexo(sexo, errores):
    if sexo == "": 
        errores.append("Debes seleccionar un sexo.")

def validar_pais_nacimiento(pais_nacimiento, errores):
    if pais_nacimiento == "": 
        errores.append("Debes seleccionar un país de nacimiento.")

def validar_provincia_nacimiento(provincia_nacimiento, errores):
    if provincia_nacimiento == "": 
        errores.append("Debes seleccionar una provincia de nacimiento.")

def validar_ciudad_nacimiento(ciudad_nacimiento, errores):
    if ciudad_nacimiento == "": 
        errores.append("Debes seleccionar una ciudad de nacimiento.")

def validar_campos_obligatorios(entries, errores):
    if any(entry.get().strip() == "" for entry in entries):
        errores.append("Todos los campos del formulario son obligatorios.")
    
# VALIDACIONES FORMULARIO 2

# Valida que solamente seleccione un checkbutton.
def validar_check_opcion(check_si, check_no, mensaje, errores):
    if (check_si == check_no):
        errores.append(mensaje)

def validar_seleccion(check_medio_si, check_medio_no, check_superior_si, check_superior_no, check_trabaja_si, check_trabaja_no, check_cargo_si, check_cargo_no, errores): # Habria que añadir check curso

    validar_check_opcion(check_medio_si, check_medio_no, "Debes elegir una opción para estudios medios.", errores)
    validar_check_opcion(check_superior_si, check_superior_no, "Debes elegir una opción para estudios medios.", errores) # falta en curso
    validar_check_opcion(check_trabaja_si, check_trabaja_no, "Debes elegir una opción para estudios medios.", errores)
    validar_check_opcion(check_cargo_si, check_cargo_no, "Debes elegir una opción para estudios medios.", errores)

def nivel_medio(check_medio_si, provincia_medio, año_ingreso_medio, año_egreso_medio, titulo_medio, errores):
    if check_medio_si == 1: # Valida si tiene estudios medios.
        
        # provincia_medio.config(state=tk.NORMAL)
        # año_ingreso.config(state=tk.NORMAL)
        # año_egreso.config(state=tk.NORMAL)
        # titulo_medio_entry.config(state=tk.NORMAL) # LA IDEA ES BLOQUEAR LOS ENTRYS.

        if provincia_medio == "":
            errores.append("Debes seleccionar una provincia en el nivel medio.")

        if año_ingreso_medio == "": 
            errores.append("Debes seleccionar un año de ingreso medio")
        if año_egreso_medio == "": 
            errores.append("Debes seleccionar un año de egreso medio")

        if not titulo_medio.isalpha():
            errores.append("El título debe ser escrito solo con letras.")
        elif len(titulo_medio) < 5 or len(titulo_medio) > 30:
            errores.append("El nombre debe tener entre 5 y 30 caracteres.")
            

def nivel_superior(check_superior_si, check_curso_si, carrera_superior, institucion, provincia_superior, año_ingreso_superior, año_egreso_superior, errores):
    if check_superior_si == 1: # or check_curso_si == 1 / Hay que poner el check en curso # Valida si tiene estudios superiores.

        if not carrera_superior.isalpha():
            errores.append("La carrera debe ser escrita solo con letras.")
        elif len(carrera_superior) < 5 or len(carrera_superior) > 30:
            errores.append("El nombre de la carrera debe tener entre 5 y 30 caracteres.")

        if not institucion.isalpha():
            errores.append("La institución debe ser escrita solo con letras.")
        elif len(institucion) < 5 or len(institucion) > 30:
            errores.append("El nombre de la institución debe tener entre 5 y 30 caracteres.")
        
        if institucion == "" or institucion == "Seleccione una provincia":
            errores.append("Debes seleccionar una provincia.")
        
        if provincia_superior == "":
            errores.append("Debes seleccionar una provincia en el nivel superior.")
        
        if año_ingreso_superior == "": 
            errores.append("Debes seleccionar un año de ingreso superior")
        if check_superior_si == 1:
            if año_egreso_superior == "": 
                errores.append("Debes seleccionar un año de egreso superior")
        
def situacion_laboral(check_trabaja_si, horas_lab, descripcion_laboral, errores):
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
        elif len(descripcion_laboral) < 5 or len(descripcion_laboral) > 300:
            errores.append("La descripción debe tener entre 5 y 300 caracteres.")