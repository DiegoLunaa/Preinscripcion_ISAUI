from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from interfaz_grafica.config import path_facu, path_isaui
from interfaz_grafica.aspirantes import abrir_ventana_aspirantes
from interfaz_grafica.cupos import abrir_ventana_cupos
from interfaz_grafica.reportes import abrir_ventana_reportes
from db.funciones_db import cerrar_sesion
from db import funciones_db

def abrir_ventana_main_adm(login):
    main_adm = Toplevel()
    main_adm.title("Main Administrador")
    main_adm.geometry("1366x768")
    main_adm.configure(bg="#274357")

    def activar_pantalla_completa(event=None):
        main_adm.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        main_adm.attributes("-fullscreen", False)

    main_adm.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    main_adm.bind("<Escape>", desactivar_pantalla_completa)
    main_adm.bind("<F11>", activar_pantalla_completa)
    
    #frames
    frame1 = Frame(main_adm, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(main_adm, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55)  

    #imagenes

    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(main_adm, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(x=0, y=-22)
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

    #foto Isaui 40 años
    imagen = Image.open(path_facu)
    imagen_redimensionada = imagen.resize((889, 540))
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui40 = Label(main_adm, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui40.place(x=395, y=130)
    label_imagen_isaui40.image = imagen_logo  # Mantiene una referencia a la imagen

    #Botones
    def avanzar_aspirantes():
        main_adm.withdraw()
        abrir_ventana_aspirantes(main_adm)

    def avanzar_cupos():
        main_adm.withdraw()
        abrir_ventana_cupos(main_adm)
    
    boton_aspirantes = Button(main_adm, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=avanzar_aspirantes)
    boton_aspirantes.place(x=64, y=184) 
    
    boton_cupos = Button(main_adm, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=avanzar_cupos)
    boton_cupos.place(x=64, y=249)  
    
    boton_reportes = Button(main_adm, text="REPORTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=abrir_ventana_reportes)
    boton_reportes.place(x=64, y=314)  

    #Botones superiores
    def logout():
        # Confirmación de cierre de sesión
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas cerrar sesión?", parent=main_adm)
        if confirmar:
            print(funciones_db.usuario_autenticado)
            cerrar_sesion()
            main_adm.destroy()
            print(funciones_db.usuario_autenticado)
            login.deiconify()
        
    boton_cerrar_sesion = Button(main_adm, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2,command=logout)
    boton_cerrar_sesion.place(x=1215, y=10)
