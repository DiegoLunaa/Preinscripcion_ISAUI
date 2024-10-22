from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from interfaz_grafica.config import path_isaui,path_lupa,path_lapiz,path_check,path_basura,path_ojo
from interfaz_grafica.confirmados import abrir_ventana_confirmados
from interfaz_grafica.en_espera import abrir_ventana_en_espera
from interfaz_grafica.info_aspirante import abrir_ventana_info_aspirante
from db.funciones_db import leer_todos_los_aspirantes, eliminar_aspirante, obtener_nombre_carrera
from main_modif import abrir_ventana_modificar


def abrir_ventana_aspirantes(main_adm):
    aspirantes = Toplevel()
    aspirantes.title("PANTALLA DE CUPOS")
    aspirantes.geometry("1366x768") 
    aspirantes.configure(bg="#274357")

    #frames
    frame1 = Frame(aspirantes, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(aspirantes, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55) 
    frame3 = Frame(aspirantes, bg="#274357", width=326 , height=90)
    frame3.place(x=997, y=181)

    #Label Acciones
    label_acciones = Label(aspirantes, text= "ACCIONES", fg="White", font=("Arial",38))
    label_acciones.configure(bg="#274357")
    label_acciones.place(x=1027,y=201)

    #BUSCADOR
    entry_buscador = Entry(aspirantes, width = 22, font=("Arial",14))
    entry_buscador.place(x=380, y=140)
    #Boton lupa
    imagen = Image.open(path_lupa)
    imagen_redimensionada = imagen.resize((16,16)) 
    imagen_lupa = ImageTk.PhotoImage(imagen_redimensionada)
    boton_lupa = Button(aspirantes, image=imagen_lupa, bg="#274357", width=20, height=20, borderwidth=2)
    boton_lupa.place(x=630, y=141)
    boton_lupa.image = imagen_lupa  # Mantiene una referencia a la imagen


    def obtener_info_alumno_seleccionado():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un alumno.")
            return
    
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')  # Obtener los valores de la fila seleccionada
        aspirante_id = aspirante_info[0]  # Obtener la ID del alumno seleccionado
        print(f"Aspirante seleccionado: {aspirante_info}, y su id es {aspirante_id}")  # Imprimir en consola
        # Llamar a la función para abrir la ventana de modificación
        abrir_ventana_modificar(aspirante_id)
    
    def obtener_info_y_verla():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un alumno.")
            return
    
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')  # Obtener los valores de la fila seleccionada
        aspirante_id = aspirante_info[0]  # Obtener la ID del alumno seleccionado
        print(f"Aspirante seleccionado: {aspirante_info}, y su id es {aspirante_id}")  # Imprimir en consola
        # Llamar a la función para abrir la ventana de modificación
        abrir_ventana_info_aspirante(aspirante_id)
    
    def eliminar_aspirante_seleccionado():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un aspirante.")
            return

        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')
        aspirante_id = aspirante_info[0]

        respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro que desea eliminar al aspirante con ID {aspirante_id}?")
        if respuesta:
            eliminar_aspirante(aspirante_id)  # Llamar a la función que elimina de la base de datos
            arbol.delete(item)  # Eliminar del Treeview
            messagebox.showinfo("Eliminado", "Aspirante eliminado correctamente.")
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada.")

    #Botones acciones
        #Boton y label ojo

    def ver_info():
        aspirantes.withdraw()
        abrir_ventana_info_aspirante(aspirantes)
    
    def modificar():
        aspirantes.withdraw()
        

    imagen = Image.open(path_ojo)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_ojo = ImageTk.PhotoImage(imagen_redimensionada)
    boton_ojo = Button(aspirantes, image=imagen_ojo, bg="#007AFF", width=50, height=50, borderwidth=2,command=obtener_info_y_verla)
    boton_ojo.place(x=989, y=326)
    boton_ojo.image = imagen_ojo  # Mantiene una referencia a la imagen
    label_ojo = Label(aspirantes,text="VER INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_ojo.place(x=1050, y=337)
        #Boton y label Lapiz
    imagen = Image.open(path_lapiz)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_lapiz = ImageTk.PhotoImage(imagen_redimensionada)
    boton_lapiz = Button(aspirantes, image=imagen_lapiz, bg="#E7EB1E", width=50, height=50, borderwidth=2,command=obtener_info_alumno_seleccionado)
    boton_lapiz.place(x=989, y=393)
    boton_lapiz.image = imagen_lapiz
    label_lapiz = Label(aspirantes,text="EDITAR INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_lapiz.place(x=1050, y=403)
        #Boton y label Trash

    def mensaje_eliminar():
        respuesta = messagebox.askyesno("Confirmar eliminación", "Usted está a punto de eliminar al aspirante.\n¿Está seguro?")    
        if respuesta:  
            messagebox.showwarning("ELIMINADO","ASPIRANTE ELIMINADO")
            #eliminar_aspirante() 
        else:
            messagebox.showwarning("CANCELADO", "ELIMINACIÓN CANCELADA")

    imagen = Image.open(path_basura)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_basura = ImageTk.PhotoImage(imagen_redimensionada)
    boton_basura = Button(aspirantes, image=imagen_basura, bg="#FF0000", width=50, height=50, borderwidth=2,command=eliminar_aspirante_seleccionado)
    boton_basura.place(x=989, y=460)
    boton_basura.image = imagen_lapiz
    label_basura = Label(aspirantes,text="ELIMINAR INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_basura.place(x=1050, y=470)

        #Boton y label Check
    imagen = Image.open(path_check)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_check = ImageTk.PhotoImage(imagen_redimensionada)
    boton_check = Button(aspirantes, image=imagen_check, bg="#1F8930", width=50, height=50, borderwidth=2)
    boton_check.place(x=989, y=527)
    boton_check.image = imagen_check
    label_basura = Label(aspirantes,text="CONFIRMAR ASPIRANTE", bg="#1F6680", fg="White", font=("Arial", 18))
    label_basura.place(x=1050, y=540)
    #Logo isaui
    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(aspirantes, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(x=0, y=-22)
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen


    #Arbol
    aspirante_data = leer_todos_los_aspirantes()
    frame_arbol = Frame(aspirantes, width=571, height=458)
    frame_arbol.place(x=380, y=181)
    frame_arbol.pack_propagate(False) #No cambia de tamaño / tamaño fijo

    arbol = ttk.Treeview(frame_arbol, columns=("n° Orden","apellido", "nombre", "dni", "carrera","acciones"), show="headings")
    arbol.pack(fill="both", expand=True) #Esto es para que ocupe todo el frame que cree recién. El frame_arbol

    arbol.heading("n° Orden", text="N° Orden")
    arbol.heading("apellido", text="Apellido")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("dni", text="DNI")
    arbol.heading("carrera", text="Carrera")

    arbol.column("n° Orden", width=50) 
    arbol.column("apellido", width=110)
    arbol.column("nombre", width=110)
    arbol.column("dni", width=100)
    arbol.column("carrera", width=200)

    if aspirante_data:
        for aspirante in aspirante_data:
            carrera = obtener_nombre_carrera(aspirante[33])
            arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], carrera))  

    #Botones superiores
    def volver():
        aspirantes.destroy()
        main_adm.deiconify()
    
    def ingresar_confirmados():
        aspirantes.withdraw()
        abrir_ventana_confirmados(aspirantes)

    def ingresar_en_espera():
        aspirantes.withdraw()
        abrir_ventana_en_espera(aspirantes)

    def cerrar_sesion():
        aspirantes.destroy()
        main_adm.destroy()
        #login.deiconify()

     #Botones
    label_aspirantes = Label(frame1,text="ASPIRANTES", bg="#274357", fg="White", font=("Arial", 16))
    label_aspirantes.place(relx=0.5, y=200, anchor='center')
    
    """boton_aspirantes = Button(aspirantes, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    boton_aspirantes.place(x=64, y=184) 
        
    boton_cupos = Button(aspirantes, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
    boton_cupos.place(x=64, y=249)  """
    
    boton_en_espera = Button(aspirantes, text="EN ESPERA", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=ingresar_en_espera)
    boton_en_espera.place(x=1039, y=679)  

    boton_confirmados = Button(aspirantes, text="CONFIRMADOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=ingresar_confirmados)
    boton_confirmados.place(x=1184, y=679)  

    boton_inicio = Button(aspirantes, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2,command= volver)
    boton_inicio.place(x=1215, y=10)

    """boton_cerrar_sesion = Button(aspirantes, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2,command=cerrar_sesion)
    boton_cerrar_sesion.place(x=1215, y=10)
"""
    #combobox
    combobox_carreras = ttk.Combobox(aspirantes, font=("Arial", 14), state='readonly')
    combobox_carreras.set("Filtrado de carrera")
    combobox_carreras.place(x=380, y=100)


    aspirantes.mainloop()
