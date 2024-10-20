from tkinter import *
from tkinter import messagebox
from mod1 import abrir_mod1
from mod2 import abrir_mod2

def abrir_ventana_modificar(aspirante_id):
    def modificar_datos_personales():
        abrir_mod1(aspirante_id)

    def modificar_estudios():
        abrir_mod2(aspirante_id)

    def seleccionar_opcion(opcion):
        if opcion == "datos_personales":
            modificar_datos_personales()
        elif opcion == "estudios":
            modificar_estudios()

    # Crear la ventana principal
    ventana = Toplevel()
    ventana.title("Modificar Información")
    ventana.geometry("200x200")

    # Crear un marco para las opciones
    marco = Frame(ventana)
    marco.pack(expand=True)  # Permite que el marco se expanda en el espacio disponible

    # Crear botones para seleccionar la opción con el mismo ancho
    boton_datos_personales = Button(marco, text="Modificar Datos Personales", command=modificar_datos_personales, width=20)
    boton_datos_personales.pack(pady=5)

    boton_estudios = Button(marco, text="Modificar Estudios", command=modificar_estudios, width=20)
    boton_estudios.pack(pady=5)

    # Iniciar la interfaz
    ventana.mainloop()
