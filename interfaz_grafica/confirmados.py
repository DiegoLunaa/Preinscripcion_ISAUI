from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from interfaz_grafica.config import path_isaui
from db.funciones_db import obtener_aspirantes_confirmados, obtener_nombre_carrera, obtener_carreras_disponibles, leer_todos_los_aspirantes

def abrir_ventana_confirmados(aspirantes):
    confirmados = Toplevel()
    confirmados.title("PANTALLA DE CONFIRMADOS")
    confirmados.geometry("1366x768") 
    confirmados.configure(bg="#274357")

    def activar_pantalla_completa(event=None):
        confirmados.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        confirmados.attributes("-fullscreen", False)

    confirmados.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    confirmados.bind("<Escape>", desactivar_pantalla_completa)
    confirmados.bind("<F11>", activar_pantalla_completa)

    #FRAMES
    frame1 = Frame(confirmados, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(confirmados, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55)  

    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(frame1, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(relx= 0.5, y=80, anchor='center')
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

    frame_confirmados = Frame(confirmados,bg="#274357",width=788, height=101)
    frame_confirmados.place(x=446, y=83)

    #Label cupo
    label_texto = Label(frame_confirmados, text="CONFIRMADOS", fg="White", font=("Arial", 40))  # Tamaño ajustado
    label_texto.configure(bg="#274357")
    label_texto.place(relx=0.5, rely=0.5, anchor='center')

    #arbol

    arbol = ttk.Treeview(frame2, columns=("n° Orden","apellido", "nombre", "dni","mail", "carrera"), show="headings", height=20)
    arbol.place(relx=0.5, y=420, anchor='center')

    arbol.heading("n° Orden", text="N° Orden")
    arbol.heading("apellido", text="Apellido")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("dni", text="DNI")
    arbol.heading("mail", text="Mail")
    arbol.heading("carrera", text="Carrera")

    arbol.column("n° Orden", width=50) 
    arbol.column("apellido", width=120)
    arbol.column("nombre", width=120)
    arbol.column("dni", width=100)
    arbol.column("mail", width=250)
    arbol.column("carrera", width=250)

    def cargar_confirmados(event):
        aspirantes = leer_todos_los_aspirantes()
        arbol.delete(*arbol.get_children())
        id_carrera_seleccionada = carreras_id_mapeo.get(combobox_filtro.get())
        if id_carrera_seleccionada:
            print(aspirantes)
            for aspirante in aspirantes:
                if aspirante[33] == id_carrera_seleccionada and aspirante[31] == "Confirmado":
                    carrera = obtener_nombre_carrera(aspirante[33])
                    arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], aspirante[11], carrera))
    

    frame_filtro = Frame(confirmados, width=24 * 10, height=27, bg="#1F6680")
    frame_filtro.place(x=380, y=140)

    carreras_id_mapeo = {}
    carreras_db = obtener_carreras_disponibles()
    lista_carreras = [nombre for _, nombre, _, _ in carreras_db]
    carreras_id_mapeo.update({nombre: id_carrera for id_carrera, nombre, _, _ in carreras_db})

    combobox_filtro = ttk.Combobox(confirmados, font=("Arial", 14), state='readonly')
    combobox_filtro.set("Filtrar por:")
    combobox_filtro['values'] = lista_carreras
    combobox_filtro.bind("<<ComboboxSelected>>", cargar_confirmados)
    combobox_filtro.place(x=400, y=200)

    cargar_confirmados(None)

    #Scrollbar
    scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=arbol.yview)
    scrollbar.place(x=972 ,y=208, height=424)
    arbol.configure(yscrollcommand=scrollbar.set)

    #combobox
    # combobox_carreras = ttk.Combobox(confirmados, font=("Arial", 14), state='readonly')
    # combobox_carreras.set("Filtrado de carrera")
    # combobox_carreras.place(x=395, y=230) 

    label_aspirantes = Label(frame1,text="ASPIRANTES", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')

    #Insertar datos en el árbol
    aspirantes_confirmados = obtener_aspirantes_confirmados()
    if aspirantes_confirmados:
            for aspirante in aspirantes_confirmados:
                carrera = obtener_nombre_carrera(aspirante[33])
                arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3],  aspirante[11], carrera)) 

    def volver():
        confirmados.destroy()
        aspirantes.deiconify()

    boton_volver = Button(confirmados, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=volver)
    boton_volver.place(x=1200, y=715)
    


    confirmados.mainloop()
