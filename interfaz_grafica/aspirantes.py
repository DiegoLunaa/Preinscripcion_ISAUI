from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from interfaz_grafica.config import path_isaui,path_lupa,path_lapiz,path_check,path_basura,path_ojo,path_mail,path_reloj
from interfaz_grafica.confirmados import abrir_ventana_confirmados
from interfaz_grafica.en_espera import abrir_ventana_en_espera
from interfaz_grafica.info_aspirante import abrir_ventana_info_aspirante
from interfaz_grafica.main_modif import abrir_ventana_modificar
from db.funciones_db import leer_todos_los_aspirantes, eliminar_aspirante, confirmar_aspirante, obtener_nombre_carrera, obtener_carreras_disponibles,obtener_estado, poner_en_lista_espera,obtener_mail_aspirante
from interfaz_grafica.notificacion_mail import abrir_mail

def abrir_ventana_aspirantes(main_adm):
    aspirantes = Toplevel()
    aspirantes.title("PANTALLA DE ASPIRANTES")
    aspirantes.geometry("1366x768") 
    aspirantes.configure(bg="#274357")

    def activar_pantalla_completa(event=None):
        aspirantes.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        aspirantes.attributes("-fullscreen", False)

    aspirantes.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    aspirantes.bind("<Escape>", desactivar_pantalla_completa)
    aspirantes.bind("<F11>", activar_pantalla_completa)

    #frames
    frame1 = Frame(aspirantes, bg="#1F6680", width=249, height=768)
    frame1.place(x=0, y=0)  
    frame2 = Frame(aspirantes, bg="#1F6680", width=1052, height=713)
    frame2.place(x=314, y=55) 
    frame3 = Frame(aspirantes, bg="#274357", width=326 , height=50)
    frame3.place(x=997, y=181)

    #Label Acciones
    label_acciones = Label(frame3, text= "ACCIONES", fg="White", font=("Arial",28))
    label_acciones.configure(bg="#274357")
    label_acciones.place(relx=0.5, rely=0.5, anchor='center')


    def obtener_info_alumno_seleccionado():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un alumno.", parent=aspirantes)
            return
    
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')  # Obtener los valores de la fila seleccionada
        aspirante_id = aspirante_info[0]  # Obtener la ID del alumno seleccionado
        print(f"Aspirante seleccionado: {aspirante_info}, y su id es {aspirante_id}")  # Imprimir en consola
        # Llamar a la función para abrir la ventana de modificación
        abrir_ventana_modificar(aspirante_id, actualizar_lista_aspirantes)
        
    def obtener_info_y_verla():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un alumno.", parent=aspirantes)
            return
    
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')  # Obtener los valores de la fila seleccionada
        aspirante_id = aspirante_info[0]  # Obtener la ID del alumno seleccionado
        print(f"Aspirante seleccionado: {aspirante_info}, y su id es {aspirante_id}")  # Imprimir en consola
        # Llamar a la función para abrir la ventana de modificación
        abrir_ventana_info_aspirante(aspirante_id)

    def obtener_asp_mail():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un alumno.", parent=aspirantes)
            return
    
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')  # Obtener los valores de la fila seleccionada
        aspirante_id = aspirante_info[0]  # Obtener la ID del alumno seleccionado
        aspirante_mail = obtener_mail_aspirante(aspirante_id)
        print(f"Aspirante seleccionado: {aspirante_info}, y su id es {aspirante_id}")  # Imprimir en consola
        # Llamar a la función para abrir la ventana de modificación
        abrir_mail(aspirante_id,aspirante_mail)
    
    def eliminar_aspirante_seleccionado():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un aspirante.", parent=aspirantes)
            return

        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')
        aspirante_id = aspirante_info[0]

        respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro que desea eliminar al aspirante con ID {aspirante_id}?", parent=aspirantes)
        if respuesta:
            eliminar_aspirante(aspirante_id)  # Llamar a la función que elimina de la base de datos
            arbol.delete(item)  # Eliminar del Treeview
            messagebox.showinfo("Eliminado", "Aspirante eliminado correctamente.", parent=aspirantes)
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada.", parent=aspirantes)

    def confirmar_aspirante_seleccionado():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un aspirante.", parent=aspirantes)
            return
        
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')
        aspirante_id = aspirante_info[0]
        respuesta = messagebox.askyesno("Confirmación del aspirante", f"¿Está seguro que desea confirmar al aspirante con ID {aspirante_id}?", parent=aspirantes)
        if respuesta:
            resultado, mensaje = confirmar_aspirante(aspirante_id)
            if not resultado:
                messagebox.showwarning("Error", mensaje, parent=aspirantes) 
            else:
                nuevo_estado = "Confirmado"
                arbol.item(item, values=(aspirante_info[0], aspirante_info[1], aspirante_info[2], aspirante_info[3], nuevo_estado, aspirante_info[5]))
                messagebox.showinfo("Confirmado", mensaje, parent=aspirantes)  
        else:
            messagebox.showinfo("Cancelado", "Confirmación cancelada.", parent=aspirantes)

    
    def poner_aspirante_seleccionado_en_espera():
        seleccion = arbol.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor, selecciona un aspirante.", parent=aspirantes)
            return
        
        item = seleccion[0]
        aspirante_info = arbol.item(item, 'values')
        aspirante_id = aspirante_info[0]
        
        respuesta = messagebox.askyesno("Lista de espera", f"¿Está seguro que desea poner al aspirante con ID {aspirante_id} en lista de espera?", parent=aspirantes)
        if respuesta:
            resultado, mensaje = poner_en_lista_espera(aspirante_id)
            if not resultado:
                messagebox.showwarning("Advertencia", mensaje, parent=aspirantes)
            else:
                nuevo_estado = "En espera"
                arbol.item(item, values=(aspirante_info[0], aspirante_info[1], aspirante_info[2], aspirante_info[3], nuevo_estado, aspirante_info[5]))
                messagebox.showinfo("En espera", mensaje, parent=aspirantes)
        else:
            messagebox.showinfo("Cancelado", "Operación cancelada.", parent=aspirantes)

    def actualizar_lista_aspirantes(event=None):
        filtro = combobox_filtro.get()
        limpiar_arbol()
        aspirantes = leer_todos_los_aspirantes()
        limpiar_frame_filtro()

        if filtro in ["Todos", "Filtrar por:"]:
            cargar_todos_aspirantes(aspirantes)
        elif filtro == "Carreras":
            cargar_filtro_carrera(aspirantes)
        elif filtro == "Estado":
            cargar_filtro_estado(aspirantes)
        elif filtro in ["Apellido", "DNI"]:
            cargar_filtro_texto(aspirantes, filtro)


    def limpiar_arbol():
        arbol.delete(*arbol.get_children())

        
    def limpiar_frame_filtro():
        for widget in frame_filtro.winfo_children():
            widget.destroy()


    def cargar_todos_aspirantes(aspirantes):
        if aspirantes:
            for aspirante in aspirantes:
                carrera = obtener_nombre_carrera(aspirante[33])
                arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], aspirante[31], carrera))


    def cargar_filtro_carrera(aspirantes):
        combobox_carrera = ttk.Combobox(frame_filtro, font=("Arial", 14), state="readonly")
        combobox_carrera.pack(fill="both", expand=True)
        carreras_id_mapeo = {}

        def cargar_carreras():
            carreras_db = obtener_carreras_disponibles()
            lista_carreras = [nombre for _, nombre, _, _ in carreras_db]
            carreras_id_mapeo.update({nombre: id_carrera for id_carrera, nombre, _, _ in carreras_db})
            combobox_carrera['values'] = lista_carreras

        def actualizar_arbol_carrera(*args):
            limpiar_arbol()
            id_carrera_seleccionada = carreras_id_mapeo.get(combobox_carrera.get())
            if id_carrera_seleccionada:
                for aspirante in aspirantes:
                    if aspirante[33] == id_carrera_seleccionada:
                        carrera = obtener_nombre_carrera(aspirante[33])
                        arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], aspirante[31], carrera))
                        

        cargar_carreras()
        combobox_carrera.bind("<<ComboboxSelected>>", actualizar_arbol_carrera)


    def cargar_filtro_estado(aspirantes):
        combobox_estado = ttk.Combobox(frame_filtro, font=("Arial", 14), state="readonly")
        combobox_estado.pack(fill="both", expand=True)
        estados = obtener_estado()  # Lista de estados de aspirantes
        combobox_estado['values'] = estados

        def actualizar_arbol_estado(*args):
            limpiar_arbol()
            estado_seleccionado = combobox_estado.get()
            for aspirante in aspirantes:
                if aspirante[31] == estado_seleccionado:
                    carrera = obtener_nombre_carrera(aspirante[33])
                    arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], estado_seleccionado, carrera))

        combobox_estado.bind("<<ComboboxSelected>>", actualizar_arbol_estado)


    def cargar_filtro_texto(aspirantes, filtro):
        entry_buscador = Entry(frame_filtro, width=22, font=("Arial", 14))
        entry_buscador.pack(fill="both", expand=True)

        def actualizar_arbol_texto():
            texto = entry_buscador.get().lower()
            limpiar_arbol()
            for aspirante in aspirantes:
                if filtro == "Apellido" and texto in aspirante[2].lower():
                    carrera = obtener_nombre_carrera(aspirante[33])
                    arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], aspirante[31], carrera))
                elif filtro == "DNI" and texto in aspirante[3].lower():
                    carrera = obtener_nombre_carrera(aspirante[33])
                    arbol.insert("", "end", values=(aspirante[0], aspirante[2], aspirante[1], aspirante[3], aspirante[31], carrera))

        entry_buscador.bind("<KeyRelease>", lambda e: actualizar_arbol_texto())

    
    #Botones, acciones

    # ver por que no se ve
    # btn_actualizar = Button(aspirantes, text="Actualizar", bg="#1F6680", fg="White", font=("Arial", 18), command=actualizar_lista_aspirantes)
    # btn_actualizar.place(x=0, y=0) 

        #Boton y label ojo
    imagen = Image.open(path_ojo)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_ojo = ImageTk.PhotoImage(imagen_redimensionada)
    boton_ojo = Button(aspirantes, image=imagen_ojo, bg="#007AFF", width=50, height=50, borderwidth=2,command=obtener_info_y_verla)
    #boton_ojo = Button(aspirantes, image=imagen_ojo, bg="#007AFF", width=50, height=50, borderwidth=2,command=poner_aspirante_seleccionado_en_espera)
    boton_ojo.place(x=989, y=249)
    boton_ojo.image = imagen_ojo  # Mantiene una referencia a la imagen
    label_ojo = Label(aspirantes,text="VER INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_ojo.place(x=1050, y=259)

        #Boton y label Lapiz
    imagen = Image.open(path_lapiz)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_lapiz = ImageTk.PhotoImage(imagen_redimensionada)
    boton_lapiz = Button(aspirantes, image=imagen_lapiz, bg="#E7EB1E", width=50, height=50, borderwidth=2,command=obtener_info_alumno_seleccionado)
    boton_lapiz.place(x=989, y=316)
    boton_lapiz.image = imagen_lapiz
    label_lapiz = Label(aspirantes,text="EDITAR INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_lapiz.place(x=1050, y=326)

        #Boton y label Trash
    def mensaje_eliminar():
        respuesta = messagebox.askyesno("Confirmar eliminación", "Usted está a punto de eliminar al aspirante.\n¿Está seguro?", parent=aspirantes)    
        if respuesta:  
            messagebox.showwarning("ELIMINADO","ASPIRANTE ELIMINADO", parent=aspirantes)
            #eliminar_aspirante() 
        else:
            messagebox.showwarning("CANCELADO", "ELIMINACIÓN CANCELADA", parent=aspirantes)

    imagen = Image.open(path_basura)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_basura = ImageTk.PhotoImage(imagen_redimensionada)
    boton_basura = Button(aspirantes, image=imagen_basura, bg="#FF0000", width=50, height=50, borderwidth=2,command=eliminar_aspirante_seleccionado)
    boton_basura.place(x=989, y=383)
    boton_basura.image = imagen_lapiz
    label_basura = Label(aspirantes,text="ELIMINAR INFORMACIÓN", bg="#1F6680", fg="White", font=("Arial", 18))
    label_basura.place(x=1050, y=393)

        #Boton y label Check
    imagen = Image.open(path_check)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_check = ImageTk.PhotoImage(imagen_redimensionada)
    boton_check = Button(aspirantes, image=imagen_check, bg="#1F8930", width=50, height=50, borderwidth=2, command=confirmar_aspirante_seleccionado)

    boton_check.place(x=989, y=450)
    boton_check.image = imagen_check
    label_basura = Label(aspirantes,text="CONFIRMAR ASPIRANTE", bg="#1F6680", fg="White", font=("Arial", 18))
    label_basura.place(x=1050, y=460)

    #boton en espera
    imagen = Image.open(path_reloj)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_reloj = ImageTk.PhotoImage(imagen_redimensionada)
    boton_reloj = Button(aspirantes, image=imagen_reloj, bg="#B700FF", width=50, height=50, borderwidth=2,command=poner_aspirante_seleccionado_en_espera)
    boton_reloj.place(x=989, y=517)
    boton_reloj.image = imagen_reloj  # Mantiene una referencia a la imagen
    label_reloj = Label(aspirantes,text="PONER EN ESPERA", bg="#1F6680", fg="White", font=("Arial", 18))
    label_reloj.place(x=1050, y=527)

    #Boton mail
    imagen = Image.open(path_mail)
    imagen_redimensionada = imagen.resize((34,34)) 
    imagen_ojo = ImageTk.PhotoImage(imagen_redimensionada)
    boton_ojo = Button(aspirantes, image=imagen_ojo, bg="#F5A656", width=50, height=50, borderwidth=2,command=obtener_asp_mail)
    boton_ojo.place(x=989, y=584)
    boton_ojo.image = imagen_ojo  # Mantiene una referencia a la imagen
    label_ojo = Label(aspirantes,text="ENVIAR MAIL", bg="#1F6680", fg="White", font=("Arial", 18))
    label_ojo.place(x=1050, y=594)


    #Logo isaui
    imagen = Image.open(path_isaui)
    imagen_redimensionada = imagen.resize((230, 200)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_isaui = Label(aspirantes, image=imagen_logo, bg="#1F6680")
    label_imagen_isaui.place(x=0, y=-22)
    label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen


    #Arbol
    
    frame_arbol = Frame(aspirantes, width=571, height=458)
    frame_arbol.place(x=380, y=181)
    frame_arbol.pack_propagate(False) #No cambia de tamaño / tamaño fijo

    arbol = ttk.Treeview(frame_arbol, columns=("n° Orden","apellido", "nombre", "dni","estado", "carrera","acciones"), show="headings")
    arbol.pack(fill="both", expand=True) #Esto es para que ocupe todo el frame que cree recién. El frame_arbol

    arbol.heading("n° Orden", text="N° Orden")
    arbol.heading("apellido", text="Apellido")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("dni", text="DNI")
    arbol.heading("estado", text="Estado")
    arbol.heading("carrera", text="Carrera")

    arbol.column("n° Orden", width=50) 
    arbol.column("apellido", width=80)
    arbol.column("nombre", width=80)
    arbol.column("dni", width=75)
    arbol.column("estado", width=85)
    arbol.column("carrera", width=200)

    frame_filtro = Frame(aspirantes, width=24 * 10, height=27, bg="#1F6680")
    frame_filtro.place(x=380, y=140)

    combobox_filtro = ttk.Combobox(aspirantes, font=("Arial", 14), state='readonly')
    combobox_filtro.set("Filtrar por:")
    combobox_filtro['values'] = ("Todos","Carreras","Estado","Apellido","DNI")
    combobox_filtro.bind("<<ComboboxSelected>>", actualizar_lista_aspirantes)
    combobox_filtro.place(x=380, y=100)
    actualizar_lista_aspirantes(event=None)
      
    

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
    
    boton_en_espera = Button(aspirantes, text="EN ESPERA", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=ingresar_en_espera)
    boton_en_espera.place(x=894, y=689)  

    boton_confirmados = Button(aspirantes, text="CONFIRMADOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command=ingresar_confirmados)
    boton_confirmados.place(x=1039, y=689)  

    boton_inicio = Button(aspirantes, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command= volver)
    boton_inicio.place(x=1184, y=689) 


    aspirantes.mainloop()
