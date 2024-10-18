import bcrypt
from .conexion_db import conectar

# Funciones de inicio de sesión y gestión de usuarios

# Variable global para almacenar el estado de autenticación
usuario_autenticado = None

def verificar_login(usuario, contrasena_plana):
    
    global usuario_autenticado
    # Conectar a la base de datos
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Obtener el hash de la contraseña del usuario
    query = "SELECT Password FROM Administrador WHERE Usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        contrasena_hash = resultado[0]
        # Verificar la contraseña
        if bcrypt.checkpw(contrasena_plana.encode('utf-8'), contrasena_hash.encode('utf-8')):
            print("Login exitoso.")
            usuario_autenticado = usuario
            cursor.close()
            conexion.close()  
            return True
        else:
            print("Contraseña incorrecta.")
            cursor.close()
            conexion.close()
            return False
    else:
        print("Usuario no encontrado.")
        cursor.close()
        conexion.close()  # Mueve esto aquí
        return False

def verificar_acceso():
    global usuario_autenticado
    if usuario_autenticado is None:
        print("Acceso denegado. Por favor, inicia sesión como administrador.")
        return False
    return True

def cerrar_sesion():
    global usuario_autenticado
    # Confirmación de cierre de sesión
    confirmar = input("¿Está seguro de que desea cerrar sesión? (s/n): ")
    if confirmar.lower() == 's':
        usuario_autenticado = None
        print("Sesión cerrada exitosamente.")
        # Aquí podrías agregar código para manejar el estado de la interfaz, si es necesario.
    else:
        print("Cierre de sesión cancelado.")

# Funciones CRUD

def crear_aspirante(datos): # ANDA
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """INSERT INTO Aspirante (Nombre, Apellido, DNI, Genero, CUIL, Domicilio, Barrio, 
               Localidad, Codigo_Postal, Telefono, Mail, Fecha_Nacimiento, Lugar_Nacimiento, 
               Completo_Nivel_Medio, Año_Ingreso_Medio, Año_Egreso_Medio, Provincia_Medio, 
               Titulo_Medio, Completo_Nivel_Superior, Carrera_Superior, Institucion_Superior, 
               Provincia_Superior, Año_Ingreso_Superior, Año_Egreso_Superior, Trabajo, 
               Descripcion_Trabajo, Personas_Cargo) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
               %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, datos)
    conexion.commit()
    print("Aspirante creado exitosamente.")
    cursor.close()
    conexion.close()

def leer_aspirante(id_aspirante): # ANDA

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Aspirante WHERE ID_Aspirante = %s"
    cursor.execute(query, (id_aspirante,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado

def actualizar_aspirante(id_aspirante, datos_actualizados): # ANDA

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()

    # Construir la consulta SQL dinámicamente
    campos = ', '.join(f"{campo} = %s" for campo in datos_actualizados.keys())
    valores = list(datos_actualizados.values()) + [id_aspirante]  # Agregar el ID_Aspirante al final

    query = f"UPDATE Aspirante SET {campos} WHERE ID_Aspirante = %s"
    cursor.execute(query, valores)
    conexion.commit()
    print("Aspirante actualizado.")
    cursor.close()
    conexion.close()

def eliminar_aspirante(id_aspirante): # ANDA

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Aspirante WHERE ID_Aspirante = %s"
    cursor.execute(query, (id_aspirante,))
    conexion.commit()
    print("Aspirante eliminado.")
    cursor.close()
    conexion.close()

def leer_carrera(id_carrera):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Carrera WHERE ID_Carrera = %s"
    cursor.execute(query, (id_carrera,))
    carrera = cursor.fetchone()
    cursor.close()
    conexion.close()
    return carrera

def actualizar_carrera(id_carrera, datos_actualizados):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """UPDATE Carrera SET Nombre_Carrera = %s, Duracion = %s, Facultad = %s, 
               Cupos_Disponibles = %s WHERE ID_Carrera = %s"""
    cursor.execute(query, (*datos_actualizados, id_carrera))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Carrera actualizada exitosamente.")

def actualizar_cupo(id_carrera, nuevo_cupo):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    
    query = "UPDATE Carrera SET Cupos_Disponibles = %s WHERE ID_Carrera = %s"
    cursor.execute(query, (nuevo_cupo, id_carrera))
    
    conexion.commit()
    cursor.close()
    conexion.close()
    
    print(f"Cupo de la carrera con ID {id_carrera} actualizado a {nuevo_cupo}.")

def crear_formulario(datos):
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """INSERT INTO Formulario (Fecha_Envio, Estado, Constancia_URL, ID_Aspirante, ID_Carrera) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, datos)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Formulario creado exitosamente.")


def eliminar_formulario(id_formulario):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Formulario WHERE ID_Formulario = %s"
    cursor.execute(query, (id_formulario,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Formulario eliminado exitosamente.")

def crear_constancia(datos):
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """INSERT INTO Constancia (Fecha_Generacion, URL_Constancia, Mensaje_Personalizado, ID_Formulario) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, datos)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Constancia creada exitosamente.")

def leer_constancia(id_constancia):

    if not verificar_acceso():
        return

    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Constancia WHERE ID_Constancia = %s"
    cursor.execute(query, (id_constancia,))
    constancia = cursor.fetchone()
    cursor.close()
    conexion.close()
    return constancia

def eliminar_constancia(id_constancia):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Constancia WHERE ID_Constancia = %s"
    cursor.execute(query, (id_constancia,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Constancia eliminada exitosamente.")

def crear_reporte(datos):
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """INSERT INTO Reporte (Fecha_Creacion, Descripcion, URL_Reporte, ID_Administrador) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, datos)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Reporte creado exitosamente.")

def leer_reporte(id_reporte):

    if not verificar_acceso():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Reporte WHERE ID_Reporte = %s"
    cursor.execute(query, (id_reporte,))
    reporte = cursor.fetchone()
    cursor.close()
    conexion.close()
    return reporte

def eliminar_reporte(id_reporte):

    if not verificar_acceso():
        return
   
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Reporte WHERE ID_Reporte = %s"
    cursor.execute(query, (id_reporte,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Reporte eliminado exitosamente.")

# Funciones Formulario

def obtener_carreras_disponibles():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT ID_Carrera, Nombre_Carrera, Cupos_Disponibles FROM Carrera WHERE Cupos_Disponibles > 0"
    cursor.execute(query)
    carreras = cursor.fetchall()
    cursor.close()
    conexion.close()
    return carreras
