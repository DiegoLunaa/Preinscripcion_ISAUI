import tkinter as tk
from tkinter import messagebox
from mod1 import abrir_mod1
from mod2 import abrir_mod2

def modificar_datos_personales():
    abrir_mod1()

def modificar_estudios():
    abrir_mod2()

def seleccionar_opcion(opcion):
    if opcion == "datos_personales":
        modificar_datos_personales()
    elif opcion == "estudios":
        modificar_estudios()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Modificar Información")
ventana.geometry("200x200")

# Crear un marco para las opciones
marco = tk.Frame(ventana)
marco.pack(expand=True)  # Permite que el marco se expanda en el espacio disponible

# Crear botones para seleccionar la opción con el mismo ancho
boton_datos_personales = tk.Button(marco, text="Modificar Datos Personales", command=modificar_datos_personales, width=20)
boton_datos_personales.pack(pady=5)

boton_estudios = tk.Button(marco, text="Modificar Estudios", command=modificar_estudios, width=20)
boton_estudios.pack(pady=5)

# Iniciar la interfaz
ventana.mainloop()
