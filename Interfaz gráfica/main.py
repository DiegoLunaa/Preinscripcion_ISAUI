import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from form1 import abrir_ventana_form1


# Funciones para poner la pantalla completa
def activar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", True)

def desactivar_pantalla_completa(event=None):
    ventana.attributes("-fullscreen", False)

ventana = tk.Tk()
ventana.title("PREINSCRIPCIÓN ISAUI")
ventana.geometry("1366x768")  # Tamaño inicial para pruebas
ventana.configure(bg="#1F6680")
ventana.attributes("-fullscreen", True)  # Inicia en modo pantalla completa
ventana.bind("<Escape>", desactivar_pantalla_completa)
ventana.bind("<F11>", activar_pantalla_completa)

# Frames
frame1 = tk.Frame(ventana, bg="#274357", width=75, height=768)
frame1.place(x=20, y=0)  # Frame izquierdo
frame2 = tk.Frame(ventana, bg="#274357", width=75, height=768)
frame2.place(x=1271, y=0)  # Frame derecho (ajuste para que sea igual)

# Logo Isaui
imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Tkinter isaui/Preinscripcion-Isaui/isaui.png")
imagen_redimensionada = imagen.resize((450, 300))  # Tamaño ajustado
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen = tk.Label(ventana, image=imagen_logo, bg="#1F6680")
label_imagen.place(x=459, y=20)  # Ajuste de posición

# Frame cuadrado con carreras
frame_cuadrado = tk.Frame(ventana, bg="#274357", width=700, height=350)  # Tamaño del frame cuadrado
frame_cuadrado.place(relx=0.5, rely=0.5, anchor='center')  # Centrado en la ventana

# Texto de bienvenida
label_texto = tk.Label(frame_cuadrado, text="Bienvenido a la preinscripción 2025\nElija la carrera a la cual ingresar",
                       fg="White", font=("Arial", 28))  # Tamaño de fuente ajustado
label_texto.configure(bg="#274357")
label_texto.pack(pady=20)

# ComboBox de carreras
carreras = {
    1: "Software",
    2: "Enfermería",
    3: "Diseño de Espacios",
    4: "Guía de Trekking",
    5: "Guía de Turismo",
    6: "Turismo y Hotelería"
}
lista_carreras = list(carreras.values())
combobox_carreras = ttk.Combobox(frame_cuadrado, values=lista_carreras, font=("Arial", 16), state='readonly')
combobox_carreras.set("Seleccione una carrera...")
combobox_carreras.pack(pady=10, padx=20, fill='x')  # Ajustar el ComboBox para que llene horizontalmente

# Botones
boton_admin = tk.Button(ventana, text="Ingreso Admin", width=12, fg="White", font=("Arial", 12), bg="#274357")
boton_admin.place(x=1150, y=20)  # Ajuste de posición

boton_avanzar = tk.Button(ventana, text="Avanzar", bg="White", fg="Black", font=("Arial", 16), command=abrir_ventana_form1)
boton_avanzar.place(relx=0.5, y=650, anchor='center', width=200, height=50)  # Centrado horizontalmente

ventana.mainloop()
