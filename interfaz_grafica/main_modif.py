from tkinter import *
from tkinter import messagebox
from interfaz_grafica.mod1 import abrir_mod1
from interfaz_grafica.mod2 import abrir_mod2

def abrir_ventana_modificar(aspirante_id, actualizar_lista_aspirantes):
    def modificar_datos_personales():
        abrir_mod1(aspirante_id, actualizar_lista_aspirantes)

    def modificar_estudios():
        abrir_mod2(aspirante_id, actualizar_lista_aspirantes)

    # Crear la ventana principal
    ventana = Toplevel()
    ventana.title("Modificar Información")
    ventana.configure(bg="#1F6680")
    window_width = 300
    window_height = 300
    ventana.geometry(f"{window_width}x{window_height}")
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

    # Frame
    frame_titulo = Frame(ventana,bg="#274357", width=217, height=75)
    frame_titulo.place(x=41,y=17)

    #label
    label_titulo = Label(frame_titulo, text="MODIFICAR\nINFORMACIÓN", fg="White", font=("Arial", 14))
    label_titulo.configure(bg="#274357")
    label_titulo.place(relx=0.5, rely=0.5, anchor='center')
    # Botones
    boton_datos_personales = Button(ventana, text="Datos Personales", command=modificar_datos_personales,bg="#274357", width=25,fg="White", font=("Arial", 10))
    boton_datos_personales.place(relx=0.5, y = 125, anchor='center')

    boton_estudios = Button(ventana, text="Estudios", command=modificar_estudios,bg="#274357", width=25,fg="White", font=("Arial", 10))
    boton_estudios.place(relx=0.5, y = 185, anchor='center')

    boton_salir = Button(ventana,text="Salir",command=ventana.destroy,bg="#274357", width=25,fg="White", font=("Arial", 10))
    boton_salir.place(relx=0.5, y = 245, anchor='center')

    # Iniciar la interfaz
    ventana.mainloop()
