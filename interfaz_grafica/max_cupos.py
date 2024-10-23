from tkinter import *
from tkinter import ttk
from db.funciones_db import obtener_carreras_disponibles, modificar_cantidad_cupos
from tkinter import messagebox

def abrir_ventana_max_cupos():
    max = Toplevel()
    max.title("MÁXIMO DE CUPOS")
    max.geometry("800x600") 
    max.configure(bg="#274357")

    #frames
    frame1 = Frame(max, bg="#1F6680", width=674, height=450)
    frame1.place(x=63, y=75)  

    #Label MAXIMO DE CUPOS
    label_max = Label(max, text="MÁXIMO DE CUPOS", fg="White", font=("Arial", 28))  
    label_max.configure(bg="#274357")
    label_max.place(relx=0.5, y=35, anchor='center')

    #botones
    boton_volver = Button(max, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#1F6680", borderwidth=2, command=max.destroy)
    boton_volver.place(x=650, y=544)

    boton_guardar = Button(max, text="GUARDAR", width=14, fg="White", font=("Arial", 12), bg="#1F6680", borderwidth=2, command=lambda: guardar_cambios(arbol), state="disabled")
    boton_guardar.place(x=500, y=544)

    boton_editar = Button(max, text="EDITAR", width=14, fg="White", font=("Arial", 12), bg="#1F6680", borderwidth=2, command=lambda: habilitar_edicion(arbol, boton_guardar))
    boton_editar.place(x=350, y=544)
    
    #ARBOL
    columnas = ("ID", "Carrera", "Cupo")
    arbol = ttk.Treeview(frame1, columns=columnas, show="headings", height=18)
    arbol.heading("ID", text="ID")
    arbol.heading("Carrera", text="Carrera")
    arbol.heading("Cupo", text="Cupo")
    arbol.column("ID", width=100)
    arbol.column("Carrera", width=370)
    arbol.column("Cupo", width=100)
    arbol.place(x=20, y=20, width=570, height=386)

    arbol.bind("<Double-1>", lambda e: "break")  # No permite la edición con doble clic

    # Definición de la función para cargar las carreras
    def cargar_carreras():
        carreras_db = obtener_carreras_disponibles()
        for id_carrera, nombre, _ , cupos_maximos in carreras_db: 
            arbol.insert("", END, values=(id_carrera, nombre, cupos_maximos))
    
    # Cargar las carreras desde la base de datos
    cargar_carreras()

    def habilitar_edicion(arbol, boton_guardar):
        def on_double_click(event):
            item = arbol.selection()  # Obtener la fila seleccionada
            if item:  # Asegurarse de que hay un item seleccionado
                item = item[0]  # Obtener el primer (y único) item seleccionado
                column = arbol.identify_column(event.x)  # Determinar en qué columna se hizo doble clic
                if column == '#3':  # Columna de los cupos
                    x, y, width, height = arbol.bbox(item, column='#3')  # Obtener la posición de la columna
                    valor_actual = arbol.item(item, 'values')[2]  # Obtener el valor actual de los cupos

                    # Crear un Entry para editar el cupo
                    entry_edit = Entry(frame1)
                    entry_edit.place(x=x, y=y, width=width, height=height)  # Colocar el Entry en la posición adecuada
                    entry_edit.insert(0, valor_actual)
                    entry_edit.focus()

                    # Cuando se presione la tecla 'Enter', actualiza el valor en el árbol
                    def on_enter(event):
                        nuevo_cupo = entry_edit.get()
                        arbol.item(item, values=(arbol.item(item, 'values')[0], arbol.item(item, 'values')[1], nuevo_cupo))
                        entry_edit.destroy()  # Eliminar el Entry después de la edición
                    
                    entry_edit.bind("<Return>", on_enter)  # Bind del evento 'Enter'
                    entry_edit.bind("<FocusOut>", lambda e: entry_edit.destroy())  # Destruir el Entry al salir del foco

        arbol.bind("<Double-1>", on_double_click)  # Habilitar la edición
        boton_guardar.config(state="normal")  # Habilitar el botón de guardar



    def guardar_cambios(arbol):
        for item in arbol.get_children():
            id_carrera, nombre, cupos_max_nuevo = arbol.item(item, 'values')
            print(f"Actualizando carrera {nombre} con nuevo cupo maximo: {cupos_max_nuevo}")
            modificar_cantidad_cupos(id_carrera, cupos_max_nuevo)
    
        arbol.unbind("<Double-1>")  # Deshabilitar la edición después de guardar
        messagebox.showinfo("Guardado", "Cambios guardados exitosamente.")

    max.mainloop()
