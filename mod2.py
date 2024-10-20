from tkinter import *
from PIL import Image, ImageTk
from db.funciones_db import *
from interfaz_grafica.confirmacion import mostrar_confirmacion
from interfaz_grafica.config import path_flecha
from interfaz_grafica.validaciones import *


def abrir_mod2(aspirante_id):
    form2 = Toplevel()
    form2.title("Formulario de preinscripción")
    form2.geometry("1366x768")
    form2.configure(bg="#1F6680")

     # VARIABLES
    radio_medio_var = IntVar()
    radio_superior_var = IntVar()
    radio_trabaja_var = IntVar()
    radio_cargo_var = IntVar()


    aspirante_info = leer_aspirante(aspirante_id)

    if aspirante_info is None:
        print(f"No se encontraron datos para el alumno con ID: {aspirante_id}")
        return  # Salir de la función si no se encuentran datos
    
    def getEntradasUsuario():
        
        nivel_medio = radio_medio_var.get()
        nivel_superior = radio_superior_var.get()
        trabaja = radio_trabaja_var.get()
        a_cargo = radio_cargo_var.get()
        provincia_medio = entry_prov.get().strip()
        provincia_superior = entry_prov_ins.get().strip()
        año_ingreso_medio = spin_año_ingreso.get()
        año_egreso_medio = spin_año_egreso.get()
        año_ingreso_superior = spin_año_ingreso_sup.get()
        año_egreso_superior = spin_año_egreso_sup.get()
        titulo_medio = entry_titulo.get().strip()
        carrera_superior = entry_carrera.get().strip()
        institucion = entry_institucion.get().strip()
        horas_lab = entry_horas.get().strip()
        descripcion_laboral = texto_descrip.get("1.0", "end").strip()
        
        return (
    nivel_medio,
    nivel_superior,
    trabaja,
    a_cargo, 
    provincia_medio,
    provincia_superior, 
    año_ingreso_medio, 
    año_egreso_medio, 
    año_ingreso_superior,
    año_egreso_superior,
    titulo_medio,
    carrera_superior,
    institucion,
    horas_lab,
    descripcion_laboral
)
    
    # Funciones para habilitar/deshabilitar campos dinámicamente
    def toggle_entries(variable, *widgets):
        estado = NORMAL if variable.get() in [1, 2] else DISABLED
        for widget in widgets:
            widget.config(state=estado)  # Cambia el estado del widget
            if estado == DISABLED:  # Si se deshabilita, limpia el contenido
                if isinstance(widget, Entry):
                    widget.config(state="normal")  
                    widget.delete(0, END)  
                    widget.insert(0, '')       
                    widget.config(state="readonly")            
                elif isinstance(widget, Text):
                    widget.config(state="normal") 
                    widget.delete("1.0", END) 
                    widget.insert("1.0", '')
                    widget.config(state='disabled')
                elif isinstance(widget, Spinbox):
                    widget.config(state="normal") 
                    widget.delete(0, END)  
                    widget.insert(0, '')  
                    widget.config(state="readonly")
            elif estado == NORMAL:
                if isinstance(widget, Spinbox):
                    widget.config(state="normal") 
                    widget.delete(0, END) 
                    widget.insert(0, '1960')  
                    widget.config(state="readonly")

    def activar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", False)

    form2.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    form2.bind("<Escape>", desactivar_pantalla_completa)
    form2.bind("<F11>", activar_pantalla_completa)

    # Estudios
    label_estudios = Label(form2, text="ESTUDIOS:", fg="White", font=("Arial", 24))
    label_estudios.configure(bg="#274357")
    label_estudios.place(x=20, y=80)

    label_nivel = Label(form2, text="NIVEL MEDIO:", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=140)
    label_nivel = Label(form2, text="NIVEL SUPERIOR:", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=250)
     # Radiobuttons
    radio_medio_si = Radiobutton(form2, text="Sí", bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_medio_var, value=1)
    radio_medio_si.place(x=170, y=140)
    radio_medio_no = Radiobutton(form2, text="No", bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_medio_var, value=0)
    radio_medio_no.place(x=220, y=140)

    radio_medio_si.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, spin_año_ingreso, spin_año_egreso, entry_titulo))
    radio_medio_no.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, spin_año_ingreso, spin_año_egreso, entry_titulo))

    radio_superior_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=1)
    radio_superior_si.place(x=200, y=250)
    radio_superior_no = Radiobutton(form2, text="No",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=0)
    radio_superior_no.place(x=250, y=250)
    radio_superior_en_curso = Radiobutton(form2, text="En curso",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=2)
    radio_superior_en_curso.place(x=300, y=250)

    radio_superior_si.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup))
    radio_superior_no.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup))
    radio_superior_en_curso.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup))

    radio_trabaja_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_trabaja_var, value=1)
    radio_trabaja_si.place(x=170, y=490)
    radio_trabaja_no = Radiobutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_trabaja_var, value=0)
    radio_trabaja_no.place(x=220, y=490)

    radio_cargo_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_cargo_var, value=1)
    radio_cargo_si.place(x=950, y=490)
    radio_cargo_no = Radiobutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_cargo_var, value=0)
    radio_cargo_no.place(x=1000, y=490)
    
    #Primera fila
    label_año_ingreso = Label(form2, text="Año ingreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=180)
    
    spin_año_ingreso = Spinbox(form2, from_=1960, to=2024, width=10, font=("Arial", 16),state='readonly')
    spin_año_ingreso.place(x=20, y=210, width=150)
    
    label_año_egreso = Label(form2, text="Año egreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=180)
    
    spin_año_egreso = Spinbox(form2, from_=1960, to=2024, width=10, font=("Arial", 16),state='readonly')
    spin_año_egreso.place(x=190, y=210, width=150)
    
    label_prov = Label(form2, text="Provincia:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov.place(x=370, y=180)
    
    entry_prov = Entry(form2, font=("Arial", 16))
    entry_prov.place(x=370, y=210, width=400)
    
    label_titulo = Label(form2, text="Título:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_titulo.place(x=800, y=180)
    
    entry_titulo = Entry(form2, font=("Arial", 16))
    entry_titulo.place(x=800, y=210, width=400)

     # Asignar comando a los Radiobuttons después de crear los widgets
    radio_medio_si.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, spin_año_ingreso, spin_año_egreso, entry_titulo))
    radio_medio_no.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, spin_año_ingreso, spin_año_egreso, entry_titulo))

    #Siguiente fila de nivel superior
    label_carrera = Label(form2, text="Carrera:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_carrera.place(x=20, y=280)
    entry_carrera = Entry(form2, font=("Arial", 16))
    entry_carrera.place(x=20, y=310, width=400)

    label_institucion = Label(form2, text="Institución:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_institucion.place(x=450, y=280)
    entry_institucion = Entry(form2, font=("Arial", 16))
    entry_institucion.place(x=450, y=310, width=400)

    label_prov_ins = Label(form2, text="Provincia:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov_ins.place(x=880, y=280)
    entry_prov_ins = Entry(form2, font=("Arial", 16))
    entry_prov_ins.place(x=880, y=310, width=400)

    #siguiente fila
    label_año_ingreso = Label(form2, text="Año ingreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=350)
    spin_año_ingreso_sup = Spinbox(form2, from_=1960, to=2024, width=10, font=("Arial", 16),state='readonly')
    spin_año_ingreso_sup.place(x=20, y=380, width=150)

    label_año_egreso = Label(form2, text="Año egreso:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=350)
    spin_año_egreso_sup = Spinbox(form2, from_=1960, to=2024, width=10, font=("Arial", 16),state='readonly')
    spin_año_egreso_sup.place(x=190, y=380, width=150)

    # Asignar comando a los Radiobuttons después de crear los widgets
    radio_superior_si.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup))
    radio_superior_no.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup))
    radio_superior_en_curso.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup))
    

    #LABEL SITUACION LABORAL Y RESPONSABILIDADES
    label_sit_laboral = Label(form2, text="SITUACIÓN LABORAL:", fg="White", font=("Arial", 24))
    label_sit_laboral.configure(bg="#274357")
    label_sit_laboral.place(x=20, y=430)
    label_responsabilidades = Label(form2, text="RESPONSABILIDADES:", fg="White", font=("Arial", 24))
    label_responsabilidades.configure(bg="#274357")
    label_responsabilidades.place(x=650, y=430)

    label_trabajo = Label(form2, text="¿TRABAJA?:", fg="White", font=("Arial", 14))
    label_trabajo.configure(bg="#1F6680")
    label_trabajo.place(x=20, y=490)
    label_cargo = Label(form2, text="¿TIENE PERSONAS A CARGO?:", fg="White", font=("Arial", 14))
    label_cargo.configure(bg="#1F6680")
    label_cargo.place(x=650, y=490)

    #entrys situacion laboral
    label_horas = Label(form2, text="Horas diarias:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_horas.place(x=20, y=530)
    entry_horas = Entry(form2, font=("Arial", 16))
    entry_horas.place(x=20, y=560, width=150)
    label_descrip = Label(form2, text="Breve descripción del trabajo:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_descrip.place(x=20, y=590)
    texto_descrip = Text(form2, width=50, height=5, font=("Arial", 16))
    texto_descrip.place(x=20, y=620)

    # Asignar comando a los Radiobuttons después de crear los widgets
    radio_trabaja_si.config(command=lambda: toggle_entries(radio_trabaja_var, entry_horas, texto_descrip))
    radio_trabaja_no.config(command=lambda: toggle_entries(radio_trabaja_var, entry_horas, texto_descrip))

    (
    _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,
    nivel_medio_actual, año_ingreso_medio_actual, año_egreso_medio_actual,
    provincia_medio_actual, titulo_medio_actual, nivel_superior_actual, 
    carrera_superior_actual, institucion_actual,
    provincia_superior_actual, año_ingreso_superior_actual, año_egreso_superior_actual,
    trabaja_actual, horas_lab_actual, descripcion_laboral_actual, a_cargo_actual
) = aspirante_info

    # VER TEMA DE LA FECHA
    cargar_datos = [
        (radio_medio_var, nivel_medio_actual),
        (spin_año_ingreso, año_ingreso_medio_actual),
        (spin_año_egreso, año_egreso_medio_actual),
        (entry_prov, provincia_medio_actual),
        (entry_titulo, titulo_medio_actual),
        (radio_superior_var, nivel_superior_actual),
        (entry_carrera, carrera_superior_actual),
        (entry_institucion, institucion_actual),
        (entry_prov_ins, provincia_superior_actual),
        (spin_año_ingreso_sup, año_ingreso_superior_actual),
        (spin_año_egreso_sup, año_egreso_superior_actual),
        (radio_trabaja_var, trabaja_actual),
        (entry_horas, horas_lab_actual),
        (texto_descrip, descripcion_laboral_actual),
        (radio_cargo_var, a_cargo_actual),
    ]

    for clave, valor in cargar_datos:
        if valor is not None:
            if isinstance(clave, IntVar):
                clave.set(valor)
            elif isinstance(clave, Spinbox):
                clave.config(state="normal")
                clave.delete(0, END)
                clave.insert(0, str(valor))
                clave.config(state="readonly")
            elif isinstance(clave, Entry):
                clave.insert(0, valor)
            elif isinstance(clave, Text):
                clave.insert("1.0", valor)
        else:
            if isinstance(clave, Spinbox):
                clave.config(state="normal")
                clave.delete(0, END)
                clave.insert(0, '')
                clave.config(state="readonly")
    
    toggle_entries(radio_medio_var, entry_prov, spin_año_ingreso, spin_año_egreso, entry_titulo)
    toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup)
    toggle_entries(radio_trabaja_var, entry_horas, texto_descrip)


    def guardar_validar():
        cambios = {}
        (
            nivel_medio_nuevo,nivel_superior_nuevo,trabaja_nuevo,a_cargo_nuevo, provincia_medio_nuevo,provincia_superior_nuevo, 
            año_ingreso_medio_nuevo, año_egreso_medio_nuevo, año_ingreso_superior_nuevo,año_egreso_superior_nuevo,
            titulo_medio_nuevo,carrera_superior_nuevo,institucion_nuevo,horas_lab_nuevo,descripcion_laboral_nuevo
                       ) = getEntradasUsuario()

        # Lista para almacenar errores
        errores = []

        # Validaciones
        validar_nivel_medio(nivel_medio_nuevo, provincia_medio_nuevo, año_ingreso_medio_nuevo, año_egreso_medio_nuevo, titulo_medio_nuevo, errores)
        validar_nivel_superior(nivel_superior_nuevo, carrera_superior_nuevo, institucion_nuevo, provincia_superior_nuevo, año_ingreso_superior_nuevo, año_egreso_superior_nuevo, errores)
        validar_situacion_laboral(trabaja_nuevo, horas_lab_nuevo, descripcion_laboral_nuevo, errores)

        # Validaciones de campos obligatorios # Falta validar si tiene personas a cargo
        entries = []
        if radio_medio_var.get() == 1:
            entries += [spin_año_ingreso, spin_año_egreso, entry_prov, entry_titulo]
        if radio_superior_var.get() == 1:
            entries += [entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup, spin_año_egreso_sup]
        if radio_superior_var.get() == 2:
            entries += [entry_carrera, entry_institucion, entry_prov_ins, spin_año_ingreso_sup]
        if radio_trabaja_var.get() == 1:
            entries += [entry_horas, texto_descrip]
        if len(entries) > 1:
            validar_campos_obligatorios(entries, errores)

        datos = [
        ('completo_nivel_medio', nivel_medio_nuevo, nivel_medio_actual),
        ('año_ingreso_medio', año_ingreso_medio_nuevo, año_ingreso_medio_actual),
        ('año_egreso_medio', año_egreso_medio_nuevo, año_egreso_medio_actual),
        ('provincia_medio', provincia_medio_nuevo, provincia_medio_actual),
        ('titulo_medio', titulo_medio_nuevo, titulo_medio_actual),
        ('completo_nivel_superior', nivel_superior_nuevo, nivel_superior_actual),
        ('carrera_superior', carrera_superior_nuevo, carrera_superior_actual),
        ('institucion_superior', institucion_nuevo, institucion_actual),
        ('provincia_superior', provincia_superior_nuevo, provincia_superior_actual),
        ('año_ingreso_superior', año_ingreso_superior_nuevo, año_ingreso_superior_actual),
        ('año_egreso_superior', año_egreso_superior_nuevo, año_egreso_superior_actual),
        ('trabajo', trabaja_nuevo, trabaja_actual),
        ('horas_trabajo', horas_lab_nuevo, horas_lab_actual),
        ('descripcion_trabajo', descripcion_laboral_nuevo, descripcion_laboral_actual),
        ('personas_cargo', a_cargo_nuevo, a_cargo_actual)
    ]
        
        for campo, nuevo_valor, valor_actual in datos:
            if nuevo_valor != valor_actual:
                cambios[campo] = nuevo_valor

        # if nivel_medio_nuevo == 0:
        #     spin_año_ingreso.config(state="normal")
        #     spin_año_ingreso.delete(0, END)
        #     spin_año_ingreso.insert(0, '1999')
        #     spin_año_ingreso.config(state="readonly")

        #     spin_año_egreso.config(state="normal")
        #     spin_año_egreso.delete(0, END)
        #     spin_año_egreso.insert(0, '')
        #     spin_año_egreso.config(state="readonly")

        #     entry_prov.delete(0, END)
        #     entry_prov.insert(0, '')

        #     entry_titulo.delete(0, END)
        #     entry_titulo.insert(0, '')
        # elif nivel_superior_nuevo == 0:
        #     entry_carrera.insert(0, '')
        #     entry_institucion.insert(0, '')
        #     entry_prov_ins.insert(0, '')
        #     spin_año_ingreso_sup.config(state="normal")
        #     spin_año_ingreso_sup.delete(0, END)
        #     spin_año_ingreso_sup.insert(0, '')
        #     spin_año_ingreso_sup.config(state="readonly")
        #     spin_año_egreso_sup.config(state="normal")
        #     spin_año_egreso_sup.delete(0, END)
        #     spin_año_egreso_sup.insert(0, '')
        #     spin_año_egreso_sup.config(state="readonly")
        # elif trabaja_nuevo == 0:
        #     entry_horas.insert(0, '')
        #     texto_descrip.insert("1.0", '')
        
        # Si hay errores, mostrar y no avanzar
        if errores:
            mostrar_errores(errores)
        elif cambios:
            actualizar_aspirante(aspirante_id, cambios)
            messagebox.showinfo("Éxito", "Los datos se han guardado correctamente.")
        else:
            messagebox.showinfo("Sin cambios", "No se realizaron cambios en los datos.")

        form2.destroy()  # Esto cerrará la ventana actual

    boton_siguiente = Button(form2, text="Guardar", bg="White", fg="Black", font=("Arial", 12), borderwidth=2,command=guardar_validar)
    boton_siguiente.place(x=1240, y=700, width=120, height=64)


    def volver():
        form2.destroy()


    
    imagen_flecha = Image.open(path_flecha)
    flecha_atras = ImageTk.PhotoImage(imagen_flecha)
    boton_atras = Button(form2, image=flecha_atras, bg="#274357", width=48, height=48, borderwidth=2, command=volver)
    boton_atras.place(x=20, y=20)
    boton_atras.image = flecha_atras  # Mantiene una referencia a la imagen

    form2.mainloop()
    