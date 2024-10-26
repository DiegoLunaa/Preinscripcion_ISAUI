import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
from PIL import Image, ImageTk
from interfaz_grafica.form1 import abrir_ventana_form1
from interfaz_grafica.config import path_isaui
from interfaz_grafica.login import abrir_ventana_login
from db.funciones_db import obtener_carreras_disponibles

# Funciones para poner la pantalla completa
def activar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", True)

def desactivar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", False)

# Diccionario para mapear nombres de carreras con sus IDs
carreras_id_mapeo = {}

# Función para cargar las carreras en el ComboBox
def cargar_carreras():
    carreras_db = obtener_carreras_disponibles()
    lista_carreras = []
    for id_carrera, nombre, cupos_disponibles, cupos_maximos in carreras_db:
        lista_carreras.append(f"{nombre}")
        carreras_id_mapeo[nombre] = id_carrera  # Guarda el ID de cada carrera

    combobox_carreras['values'] = lista_carreras

# Obtener el ID de la carrera seleccionada
def obtener_id_carrera_seleccionada():
    nombre_seleccionado = combobox_carreras.get().split(" (")[0]  # Extrae el nombre sin los cupos
    return carreras_id_mapeo.get(nombre_seleccionado)

# Nueva función para avanzar a form1
def avanzar_form1():
    # Verifica que se haya seleccionado una carrera
    id_carrera = obtener_id_carrera_seleccionada()
    
    if id_carrera is None:
        # Si no hay selección, muestra un mensaje de error
        messagebox.showerror("Error", "Por favor, selecciona una carrera antes de avanzar.")
        return

    # Mostrar el ID de la carrera seleccionada (para debugging)
    print(f"ID de carrera seleccionada: {id_carrera}")

    # Abre el formulario y pasa el ID de la carrera seleccionada
    abrir_ventana_form1(id_carrera)

ventana = tk.Tk()
ventana.title("PREINSCRIPCIÓN ISAUI")
ventana.geometry(f"1366x768")  # Tamaño inicial para pruebas
ventana.configure(bg="#1F6680")
# ventana.attributes("-fullscreen", True)  # Inicia en modo pantalla completa
ventana.bind("<Escape>", desactivar_pantalla_completa)
ventana.bind("<F11>", activar_pantalla_completa)
ventana.attributes("-fullscreen", True)  # Iniciar en pantalla completa

# Frames
frame1 = tk.Frame(ventana, bg="#274357", width=75, height=768)
frame1.place(x=20, y=0)  # Frame izquierdo
frame2 = tk.Frame(ventana, bg="#274357", width=75, height=768)
frame2.place(x=1271, y=0)  # Frame derecho (ajuste para que sea igual)

# Logo Isaui
imagen = Image.open(path_isaui)
imagen_redimensionada = imagen.resize((450, 300))  # Tamaño ajustado
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen = tk.Label(ventana, image=imagen_logo, bg="#1F6680")
label_imagen.place(x=459, y=20)  # Ajuste de posición

# Frame cuadrado con carreras
frame_cuadrado = tk.Frame(ventana, bg="#274357", width=700, height=350)  # Tamaño del frame cuadrado
frame_cuadrado.place(relx=0.5, rely=0.5, anchor='center')  # Centrado en la ventana

# Texto de bienvenida
label_texto = tk.Label(frame_cuadrado, text=" Bienvenido a la preinscripción 2025 ",
                       fg="White", font=("Arial", 28))  # Tamaño de fuente ajustado
label_texto.configure(bg="#274357")
label_texto.pack(pady=20)

# ComboBox de carreras
# Inicializa el ComboBox
combobox_carreras = ttk.Combobox(frame_cuadrado, font=("Arial", 16), state='readonly')
combobox_carreras.set("Seleccione una carrera...")
combobox_carreras.pack(pady=10, padx=20, fill='x')

# Llama a la función para cargar las carreras al iniciar la app
cargar_carreras()

# Botones
boton_admin = tk.Button(ventana, text="Ingreso Admin", width=12, fg="White", font=("Arial", 12), bg="#274357", command= abrir_ventana_login)
boton_admin.place(x=1150, y=20)  # Ajuste de posición

# Cambiar el comando del botón "Avanzar" para usar la nueva función
boton_avanzar = tk.Button(ventana, text="Avanzar", bg="White", fg="Black", font=("Arial", 16), command=avanzar_form1)
boton_avanzar.place(relx=0.5, y=580, anchor='center', width=200, height=50)  # Centrado horizontalmente

boton_salir = tk.Button(ventana, text="Salir", bg="White", fg="Black", font=("Arial", 16), command=sys.exit)
boton_salir.place(relx=0.5, y=670, anchor='center', width=200, height=50)

ventana.mainloop()
