from tkinter import *
from tkinter import ttk
from interfaz_grafica.config import path_facu, path_isaui
from PIL import Image, ImageTk

def abrir_ventana_info_aspirante(aspirantes):
    info = Toplevel()
    info.title("PANTALLA DE INFORMACIÓN")
    info.geometry("1366x768") 
    info.configure(bg="#274357")

    #FRAMES
    frame1 = Frame(info, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(info, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55)  
    

    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(frame1, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(relx= 0.5, y=80, anchor='center')
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

    frame_info = Frame(info,bg="#274357",width=788, height=101)
    frame_info.place(x=446, y=83)

    #Label cupo
    label_texto = Label(frame_info, text="INFORMACIÓN DEL ASPIRANTE", fg="White", font=("Arial", 38))  # Tamaño ajustado
    label_texto.configure(bg="#274357")
    label_texto.place(relx=0.5, rely=0.5, anchor='center')

    #arbol

    arbol = ttk.Treeview(frame2, columns=("Campo", "info"), show="headings", height=20)
    arbol.heading("Campo", text="Campo")
    arbol.heading("info", text="Información")
    arbol.column("Campo", width=300, anchor="w") 
    arbol.column("info", width=400, anchor="w")  

    campos = [
        "DATOS PERSONALES:",
        "NOMBRE",
        "APELLIDO",
        "SEXO",
        "DNI",
        "CUIL/CUIT",
        "DOMICILIO",
        "LOCALIDAD",
        "BARRIO",
        "CODIGO POSTAL",
        "TELÉFONO",
        "EMAIL",
        "FECHA DE NACIMIENTO",
        "PAIS",
        "PROVINCIA",
        "ESTUDIOS:",
        "ESTUDIOS NIVEL MEDIO",
        "AÑO DE INGRESO",
        "AÑO DE EGRESO",
        "PROVINCIA",
        "TÍTULO",
        "NIVEL SUPERIOR",
        "CARRERA",
        "INSTITUCIÓN",
        "PROVINCIA",
        "AÑO DE INGRESO",
        "AÑO DE EGRESO",
        "SIT LABORAL Y RESP:",
        "TRABAJA",
        "HORAS DE TRABAJO",
        "TIENE PERSONAS A CARGO?"
    ]

    for campo in campos:
        arbol.insert("", "end", values=(campo, "")) 

    arbol.place(relx=0.5, y=410, anchor='center')

    #Scrollbar
    scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=arbol.yview)
    scrollbar.place(x=876 ,y=198, height=424)
    arbol.configure(yscrollcommand=scrollbar.set)

    label_aspirantes = Label(frame1,text="ASPIRANTES", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')

    #boton_cerrar_sesion = Button(info, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
    #boton_cerrar_sesion.place(x=1215, y=10)

    #Botones
    #boton_aspirantes = Button(info, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    #boton_aspirantes.place(x=64, y=184) 
        
    #boton_cupos = Button(info, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    #boton_cupos.place(x=64, y=249)  

    def volver():
        info.destroy()
        aspirantes.deiconify()

    boton_volver = Button(info, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=volver)
    boton_volver.place(x=1200, y=715)
    


    info.mainloop()
