from tkinter import *
from tkinter import ttk
from interfaz_grafica.config import path_isaui
from PIL import Image, ImageTk
from db.funciones_db import *

def abrir_ventana_info_aspirante(aspirante_id):
    info_aspirante = Toplevel()
    info_aspirante.title("PANTALLA DE INFORMACIÓN")
    info_aspirante.geometry("1366x768") 
    info_aspirante.configure(bg="#274357")

    def activar_pantalla_completa(event=None):
        info_aspirante.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        info_aspirante.attributes("-fullscreen", False)

    info_aspirante.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    info_aspirante.bind("<Escape>", desactivar_pantalla_completa)
    info_aspirante.bind("<F11>", activar_pantalla_completa)

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

    aspirante_info = leer_aspirante(aspirante_id)

    if aspirante_info:
            (
        id, nombre, apellido, dni, sexo, 
        cuil, domicilio, barrio, localidad_personal,
        codigo_postal, telefono, email,  
        fecha_nacimiento, pais_nacimiento,
        provincia_nacimiento, ciudad_nacimiento, nivel_medio, año_ingreso_medio,
        año_egreso_medio, provincia_medio, titulo_medio, nivel_superior, 
        carrera_superior, institucion, provincia_superior, año_ingreso_superior,
        año_egreso_superior, trabaja, horas_lab, descripcion_laboral, a_cargo,
        estado, fecha_envio, carrera, activo
        ) = aspirante_info
        
            datos = [
            ('ID Aspirante', id),
            ('Carrera', carrera),     
            ('Nombre', nombre),
            ('Apellido', apellido),
            ('DNI', dni),
            ('Género', sexo),
            ('CUIL', cuil),
            ('Domicilio', domicilio),
            ('Barrio', barrio),
            ('Localidad', localidad_personal),
            ('Código Postal', codigo_postal),
            ('Teléfono', telefono),
            ('Email', email),
            ('Fecha de nacimiento', fecha_nacimiento),
            ('País de nacimiento', pais_nacimiento),
            ('Provincia de nacimiento', provincia_nacimiento),
            ('Localidad de nacimiento', ciudad_nacimiento),
            ('¿Nivel medio completo?', nivel_medio),
            ('Año de ingreso medio', año_ingreso_medio),
            ('Año de egreso medio', año_egreso_medio),
            ('Provincia estudios medios', provincia_medio),
            ('Título estudios medios', titulo_medio),
            ('¿Nivel superior completo?', nivel_superior),
            ('Carrera superior', carrera_superior),
            ('Institución superior', institucion),
            ('Provincia superior', provincia_superior),
            ('Año de ingreso superior', año_ingreso_superior),
            ('Año de egreso superior', año_egreso_superior),
            ('¿Trabaja?', trabaja),
            ('Horas de trabajo', horas_lab),
            ('Descripción laboral', descripcion_laboral),
            ('¿Tiene personas a cargo?', a_cargo),
            ('Estado del registro', estado),
            ('Fecha de envío', fecha_envio),
            ('Está activo?', activo)
        ]
        # Insertar los campos y su información en el árbol
            for campo, info in datos:
                if campo == 'Carrera':
                    # Obtener el nombre de la carrera según su ID
                    nombre_carrera = obtener_nombre_carrera(info)
                    arbol.insert("", "end", values=(campo, nombre_carrera))
                elif campo != 'ID_Aspirante':
                    if info is None:
                        info = 'No tiene'
                    elif info == 0:
                        info = 'No'
                    elif info == 1:
                        info = 'Si'
                    arbol.insert("", "end", values=(campo, info))
                else:
                    arbol.insert("", "end", values=(campo, info))
    # Scrollbar
    scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=arbol.yview)
    scrollbar.place(x=876, y=198, height=424) 
    arbol.configure(yscrollcommand=scrollbar.set)

    label_aspirantes = Label(frame1, text="ASPIRANTES", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')

    def volver():
        info_aspirante.destroy()

    boton_volver = Button(info_aspirante, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=volver)
    boton_volver.place(x=1200, y=715)

    info_aspirante.mainloop()
