import bcrypt
from db.conexion_db import conectar
from mysql.connector import Error
from tkinter import messagebox

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
            return True, usuario_autenticado
        else:
            print("Contraseña incorrecta.")
            #messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos.")
            cursor.close()
            conexion.close()
            return False, usuario_autenticado
    else:
        print("Usuario no encontrado.")
        cursor.close()
        conexion.close()  # Mueve esto aquí
        return False, usuario_autenticado

def cerrar_sesion():
    global usuario_autenticado
    usuario_autenticado = None
    print("Sesión cerrada exitosamente.")
    return usuario_autenticado

def obtener_nombres_admin():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM administrador") 
    nombres = [fila[0] for fila in cursor.fetchall()]
    conexion.close()
    return nombres

def verificar_usuario_autenticado():
    global usuario_autenticado
    nombres_admin = obtener_nombres_admin()
    if usuario_autenticado in nombres_admin:
        return True
    else:
        print("Acceso denegado. Por favor, inicia sesión como administrador.")
        usuario_autenticado = None
        return False
    
# def acceso_requerido(parent):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if verificar_usuario_autenticado is False:
#                 messagebox.showerror("Acceso denegado", "Debe estar autenticado como administrador.", parent=parent)
#                 return
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# Funciones auxiliares

def preparar_datos_para_sql(diccionario):
    # Extraemos los valores en el mismo orden que en la consulta SQL
    return tuple(diccionario.values())

def dni_existe_en_db(dni):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT COUNT(*) FROM Aspirante WHERE dni = %s"
    cursor.execute(query, (dni,))
    result = cursor.fetchone()[0]
    return result > 0

def correo_existe_en_db(correo):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT COUNT(*) FROM Aspirante WHERE mail = %s"
    cursor.execute(query, (correo,))
    result = cursor.fetchone()[0]
    return result > 0

# Funciones CRUD

def crear_aspirante(datos): # ANDA
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = """INSERT INTO Aspirante (Nombre, Apellido, DNI, Genero, CUIL, Domicilio, Barrio, 
               Localidad, Codigo_Postal, Telefono, Mail, Fecha_Nacimiento, Pais_Nacimiento,
               Provincia_Nacimiento, Localidad_Nacimiento, Completo_Nivel_Medio, Completo_Nivel_Superior, 
               Trabajo, Personas_Cargo, Año_Ingreso_Medio, Año_Egreso_Medio, Provincia_Medio, 
               Titulo_Medio, Carrera_Superior, Institucion_Superior, Provincia_Superior, 
               Año_Ingreso_Superior, Año_Egreso_Superior, Horas_Trabajo, Descripcion_Trabajo, Estado,
               Fecha_Envio, ID_Carrera) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)"""
    cursor.execute(query, datos)
    conexion.commit()
    aspirante_id = cursor.lastrowid  # Obtiene el ID del último registro insertado
    print("Aspirante creado exitosamente con ID:", aspirante_id)
    cursor.close()
    conexion.close()
    return aspirante_id

def leer_aspirante(id_aspirante):
    # if not verificar_usuario_autenticado():
    #     print("Acceso denegado.")
    #     return None  # O lanza una excepción según tu lógica

    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return None

    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM Aspirante WHERE ID_Aspirante = %s"
        cursor.execute(query, (id_aspirante,))
        resultado = cursor.fetchone()

        if resultado is None:
            print(f"No se encontró un aspirante con ID: {id_aspirante}")
            return None  # O lanza una excepción según tu lógica

        # # Convertir el resultado a un diccionario, si es necesario
        # columnas = [column[0] for column in cursor.description]  # Obtener nombres de las columnas
        # aspirante_info = dict(zip(columnas, resultado))  # Crear un diccionario con los datos

    except Error as e:
        print(f"Error al leer el aspirante: {e}")
        resultado = None
    finally:
        cursor.close()
        conexion.close()

    return resultado

def leer_todos_los_aspirantes():
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Aspirante")  # Ajusta la consulta según tu tabla
        resultados = cursor.fetchall()  # Obtiene todos los registros
        return resultados
    except Error as e:
        print(f"Error al leer los aspirantes: {e}")
        return []
    finally:
        cursor.close()
        conexion.close()

def actualizar_aspirante(id_aspirante, datos_actualizados): # ANDA

    # if not verificar_acceso():
    #     return
        
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

def preparar_datos_para_sql(diccionario):
    # Extraemos los valores en el mismo orden que en la consulta SQL
    return tuple(diccionario.values())

def eliminar_aspirante(id_aspirante): # ANDA

    if not verificar_usuario_autenticado():
        return
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "DELETE FROM Aspirante WHERE ID_Aspirante = %s"
    cursor.execute(query, (id_aspirante,))
    conexion.commit()
    print("Aspirante eliminado.")
    cursor.close()
    conexion.close()
    
def confirmar_aspirante(id_aspirante):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT Estado, ID_Carrera FROM Aspirante WHERE ID_Aspirante = %s"
    cursor.execute(query, (id_aspirante,))
    resultado = cursor.fetchone()
    
    estado = resultado[0]
    id_carrera = resultado[1]

    if estado == 'Confirmado':
        cursor.close()
        conexion.close()
        return False, "El aspirante ya se encuentra confirmado."
    
    cupos = cupos_disponibles(id_carrera)
    if cupos == 0:
        return False, "No hay cupos disponibles para esta carrera."   
    
    query = "UPDATE Aspirante SET Estado = 'Confirmado' WHERE ID_Aspirante = %s"
    cursor.execute(query, (id_aspirante,))
    descontar_cupo(id_carrera)
    conexion.commit()
    cursor.close()
    conexion.close()
    return True, "Aspirante confirmado exitosamente."

def obtener_aspirantes_confirmados():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Aspirante WHERE Estado = 'Confirmado'"
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def leer_carrera(id_carrera):

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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

    if not verificar_usuario_autenticado():
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
    query = "SELECT ID_Carrera, Nombre_Carrera, Cupos_Disponibles, Cupos_Maximos FROM Carrera"
    cursor.execute(query)
    carreras = cursor.fetchall()
    cursor.close()
    conexion.close()
    return carreras

def obtener_nombre_carrera(id_carrera):
    conexion = conectar()  # Asegúrate de que la función 'conectar' esté definida
    cursor = conexion.cursor()
    query = "SELECT Nombre_Carrera FROM Carrera WHERE ID_Carrera = %s"
    cursor.execute(query, (id_carrera,))
    carrera = cursor.fetchone()
    cursor.close()
    conexion.close()
    return carrera[0] if carrera else "Carrera no encontrada"

def cupos_disponibles(id_carrera):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT Cupos_Disponibles FROM Carrera WHERE ID_Carrera = %s"
    cursor.execute(query, (id_carrera,))
    cupos = cursor.fetchone()[0]
    print(f"Cupos disponibles actuales: {cupos}")
    cursor.close()
    conexion.close()
    return cupos

def descontar_cupo(id_carrera):
    conexion = conectar()
    cursor = conexion.cursor()
    cupos_actuales = cupos_disponibles(id_carrera)

    if cupos_actuales > 0:
        query = "UPDATE Carrera SET Cupos_Disponibles = Cupos_Disponibles - 1 WHERE ID_Carrera = %s"
        cursor.execute(query, (id_carrera,))
        conexion.commit()
        print(f"Cupos actualizados. Cupos restantes: {cupos_actuales - 1}")
    else:
        print("No hay cupos disponibles para esta carrera.")
    cursor.close()
    conexion.close()

def cupos_max(id_carrera):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT Cupos_Maximos FROM Carrera WHERE ID_Carrera = %s"
    cursor.execute(query, (id_carrera,))
    cupos_max = cursor.fetchone()[0]
    cursor.close()
    conexion.close
    return cupos_max

def modificar_cantidad_cupos(id_carrera, cupos_max_nuevo):

    if not verificar_usuario_autenticado():
        return
    
    cupos_max_nuevo = int(cupos_max_nuevo)
    conexion = conectar()
    cursor = conexion.cursor()
    query_max_cupos = "SELECT Cupos_Maximos FROM Carrera WHERE ID_Carrera = %s"
    cursor.execute(query_max_cupos, (id_carrera,))
    cupos_max = cursor.fetchone()[0]

    if cupos_max_nuevo > cupos_max:
        diferencia_cupos = int(cupos_max_nuevo) - cupos_max
        query_actualizar_cupos_disponibles = "UPDATE Carrera SET Cupos_Disponibles = Cupos_Disponibles + %s WHERE ID_Carrera = %s"
        cursor.execute(query_actualizar_cupos_disponibles, (diferencia_cupos, id_carrera))
    else:
        query_cupos_disponibles = "SELECT Cupos_Disponibles FROM Carrera WHERE ID_Carrera = %s"
        cursor.execute(query_cupos_disponibles, (id_carrera,))
        cupos_disponibles = cursor.fetchone()[0]
        
        if cupos_max - cupos_max_nuevo > cupos_disponibles:
            query_actualizar_cupos_disponibles = "UPDATE Carrera SET Cupos_Disponibles = 0 WHERE ID_Carrera = %s"
            cursor.execute(query_actualizar_cupos_disponibles, (id_carrera,))
        else:
            diferencia_cupos = cupos_max - cupos_max_nuevo
            query_actualizar_cupos_disponibles = "UPDATE Carrera SET Cupos_Disponibles = Cupos_Disponibles - %s WHERE ID_Carrera = %s"
            cursor.execute(query_actualizar_cupos_disponibles, (diferencia_cupos, id_carrera))

    query_actualizar_cupos_max = "UPDATE Carrera SET Cupos_Maximos = %s WHERE ID_Carrera = %s"
    cursor.execute(query_actualizar_cupos_max, (cupos_max_nuevo, id_carrera))
    conexion.commit()
    cursor.close()
    conexion.close()