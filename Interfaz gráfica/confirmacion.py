from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

def mostrar_confirmacion():
    confirmacion = Toplevel()
    confirmacion.title("Formulario de preinscripción")
    confirmacion.geometry("600x400")
    confirmacion.configure(bg="#1F6680")

    imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Tkinter isaui/Preinscripcion-Isaui/isaui.png")
    imagen_redimensionada = imagen.resize((400, 250))  # Tamaño ajustado
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen = Label(confirmacion, image=imagen_logo, bg="#1F6680")
    label_imagen.image = imagen_logo #Guarda la referencia sino no aparece
    label_imagen.place(relx=0.5, y=-31, anchor='n')  # Ajuste de posición

    label_msj = Label(confirmacion, text="GRACIAS POR INSCRIBIRTE!\n \nTe llegará un mail con la\nconfirmación e información.", fg="White", font=("Arial", 20)) 
    label_msj.configure(bg="#1F6680")
    label_msj.place(relx=0.5, y=171, anchor='n')  # Centrar horizontalmente

    label_msj = Label(confirmacion, text="ÉXITOS!", fg="White", font=("Arial", 20)) 
    label_msj.configure(bg="#1F6680")
    label_msj.place(relx=0.5, y=320, anchor='n') 

    #salir

    def salir():
        confirmacion.destroy()

    boton_salir = Button(confirmacion, text="SALIR", bg="White", fg="Black", font=("Arial", 16), borderwidth=2, command=salir)
    boton_salir.place(x=480, y=340, width=100, height=40)

