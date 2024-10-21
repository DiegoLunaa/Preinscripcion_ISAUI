from tkinter import *
from tkinter import ttk
from interfaz_grafica.config import path_isaui
from PIL import Image, ImageTk
from db.funciones_db import leer_todos_los_aspirantes

def abrir_ventana_info_aspirante(aspirantes):
    info_aspirante = Toplevel()
    info_aspirante.title("PANTALLA DE INFORMACIÓN")
    info_aspirante.geometry("1366x768") 
    info_aspirante.configure(bg="#274357")

    # FRAME 1
    frame1 = Frame(info_aspirante, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    # FRAME 2
    frame2 = Frame(info_aspirante, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55)  

    # Logo
    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(frame1, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(relx=0.5, y=80, anchor='center')
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

    # Título
    frame_info = Frame(info_aspirante, bg="#274357", width=788, height=101)
    frame_info.place(x=446, y=83)

    label_texto = Label(frame_info, text="INFORMACIÓN DEL ASPIRANTE", fg="White", font=("Arial", 38))  
    label_texto.configure(bg="#274357")
    label_texto.place(relx=0.5, rely=0.5, anchor='center')

    # Árbol
    arbol = ttk.Treeview(frame2, columns=("Campo", "info"), show="headings", height=20)
    arbol.heading("Campo", text="Campo")
    arbol.heading("info", text="Información")
    arbol.column("Campo", width=300, anchor="w") 
    arbol.column("info", width=400, anchor="w")  
    arbol.place(relx=0.5, y=410, anchor='center')  # Ajusta la posición vertical aquí

    # Obtener la información de los aspirantes
    aspirante_info = leer_todos_los_aspirantes()
    if aspirante_info:
        aspirante = aspirante_info[2]  # Solo se mostrará el primer aspirante
        print(aspirante)

        campos = [
            ('Nombre', aspirante[1]),
            ('Apellido', aspirante[2]),
            ('DNI', aspirante[3]),
            ('Género', aspirante[4]),
            ('CUIL', aspirante[5]),
            ('Domicilio', aspirante[6]),
            ('Barrio', aspirante[7]),
            ('Localidad', aspirante[8]),
            ('Código Postal', aspirante[9]),
            ('Teléfono', aspirante[10]),
            ('Mail', aspirante[11]),
            ('Fecha de Nacimiento', aspirante[12]),
            ('País de Nacimiento', aspirante[13]),
            ('Provincia de Nacimiento', aspirante[14]),
            ('Localidad de Nacimiento', aspirante[15]),
            ('Completo Nivel Medio', aspirante[16]),
            ('Año Ingreso Medio', aspirante[17]),
            ('Año Egreso Medio', aspirante[18]),
            ('Provincia Medio', aspirante[19]),
            ('Título Medio', aspirante[20]),
            ('Completo Nivel Superior', aspirante[21]),
            ('Carrera Superior', aspirante[22]),
            ('Institución Superior', aspirante[23]),
            ('Provincia Superior', aspirante[24]),
            ('Año Ingreso Superior', aspirante[25]),
            ('Año Egreso Superior', aspirante[26]),
            ('Trabajo', aspirante[27]),
            ('Horas Trabajo', aspirante[28]),
            ('Descripción Trabajo', aspirante[29]),
            ('Personas Cargo', aspirante[30]),
        ]

        # Insertar los campos y su información en el árbol
        for campo, info in campos:
            arbol.insert("", "end", values=(campo, info))

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=arbol.yview)
    scrollbar.place(x=876, y=198, height=424) 
    arbol.configure(yscrollcommand=scrollbar.set)

    label_aspirantes = Label(frame1, text="ASPIRANTES", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')

    def volver():
        info_aspirante.destroy()
        aspirantes.deiconify()

    boton_volver = Button(info_aspirante, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=volver)
    boton_volver.place(x=1200, y=715)

    info_aspirante.mainloop()
