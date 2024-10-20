from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from interfaz_grafica.config import path_isaui
from interfaz_grafica.max_cupos import abrir_ventana_max_cupos
from db.funciones_db import cupos_disponibles, cupos_max

def abrir_ventana_cupos(main_adm):
    cupos = Toplevel()
    cupos.title("PANTALLA DE CUPOS")
    cupos.geometry("1366x768") 
    cupos.configure(bg="#274357")


    def actualizar_progreso():
        carreras = [
            (1, progress_bar_soft, label_cupos_software),
            (2, progress_bar_diseño, label_cupos_diseño),
            (3, progress_bar_enfermeria, label_cupos_enfermeria),
            (4, progress_bar_turismo_hoteleria, label_cupos_turismo_hoteleria),
            (5, progress_bar_turismo, label_cupos_turismo),
            (6, progress_bar_trekking, label_cupos_trekking)
        ]
        
        for id_carrera, progress_bar, label_cupos in carreras:
            cupos_maximos = cupos_max(id_carrera)
            cupos_restantes = cupos_disponibles(id_carrera)
            cupos_ocupados = cupos_maximos - cupos_restantes
            porcentaje = (cupos_ocupados / cupos_maximos) * 100 if cupos_maximos > 0 else 0
            progress_bar['value'] = porcentaje
            label_cupos.config(text=f"Cupos restantes: {cupos_restantes} / {cupos_maximos}")
   
   
    #frames
    frame1 = Frame(cupos, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(cupos, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55)  

    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(cupos, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(x=0, y=-22)
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

    frame_cupo = Frame(cupos,bg="#274357",width=788, height=101)
    frame_cupo.place(x=446, y=83)
    #Label cupo
    label_texto = Label(cupos, text="CUPOS", fg="White", font=("Arial", 40))  # Tamaño ajustado
    label_texto.configure(bg="#274357")
    label_texto.place(x=730, y=100)

    """#Botones
    boton_aspirantes = Button(cupos, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    boton_aspirantes.place(x=64, y=184) 
        
    boton_cupos = Button(cupos, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    boton_cupos.place(x=64, y=249) """ 

    def volver():
            cupos.destroy()
            main_adm.deiconify()

    boton_volver = Button(cupos, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2,command= volver)
    boton_volver.place(x=1215, y=10)

    boton_confirmados = Button(cupos, text="MÁXIMO DE CUPOS", width=16, fg="White", font=("Arial", 10), bg="#274357",borderwidth=2,command=abrir_ventana_max_cupos)
    boton_confirmados.place(x=1184, y=679)  

        #Botones superiores

    """boton_cerrar_sesion = Button(cupos, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
    boton_cerrar_sesion.place(x=1215, y=10)"""

    label_aspirantes = Label(frame1,text="CUPOS", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')


    #CUPOS Y PROGRESS BAR POR CADA CARRERA

    label_texto = Label(cupos, text="DESARROLLO DE SOFTWARE", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=400, y=250)
    progress_bar_soft = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_soft.place(x=400,y=300,width=400)
    label_cupos_software = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_software.place(x=400, y=330)

    label_texto = Label(cupos, text="DISEÑO DE ESPACIOS", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=400, y=389)
    progress_bar_diseño = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_diseño.place(x=400,y=442,width=400)
    label_cupos_diseño = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_diseño.place(x=400, y=472)

    label_texto = Label(cupos, text="ENFERMERÍA", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=877, y=530)
    progress_bar_enfermeria = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_enfermeria.place(x=877,y=583,width=400)
    label_cupos_enfermeria = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_enfermeria.place(x=877, y=613)

    label_texto = Label(cupos, text="TURISMO Y HOTELERÍA", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=877, y=389)
    progress_bar_turismo_hoteleria = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_turismo_hoteleria.place(x=877,y=442,width=400)
    label_cupos_turismo_hoteleria = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_turismo_hoteleria.place(x=877, y=472)

    label_texto = Label(cupos, text="GUÍA DE TURISMO", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=877, y=250)
    progress_bar_turismo = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_turismo.place(x=877,y=300,width=400)
    label_cupos_turismo = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_turismo.place(x=877, y=330)

    label_texto = Label(cupos, text="TREKKING", fg="White", font=("Arial", 20))
    label_texto.configure(bg="#1F6680")
    label_texto.place(x=400, y=530)
    progress_bar_trekking = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
    progress_bar_trekking.place(x=400,y=583,width=400)
    label_cupos_trekking = Label(cupos, text="", fg="White", font=("Arial", 14), bg="#1F6680")
    label_cupos_trekking.place(x=400, y=613)

    actualizar_progreso()

    cupos.mainloop()