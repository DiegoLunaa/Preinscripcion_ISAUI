import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='isaui_prematricula',
            user='root',
            password='PreIns2024!@'
        )
        if conexion.is_connected():
            # print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Prueba la conexión
conexion = conectar()
if conexion:
    conexion.close()
