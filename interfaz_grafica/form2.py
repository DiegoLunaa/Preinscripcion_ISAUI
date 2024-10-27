from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from interfaz_grafica.confirmacion import mostrar_confirmacion
from interfaz_grafica.config import path_flecha
from interfaz_grafica.validaciones import *
from db.funciones_db import *
from interfaz_grafica.notificacion_mail import confirmar_preinscripcion

def abrir_ventana_form2(form, datos_temporales):
    form2 = Toplevel()
    form2.title("Formulario de preinscripción")
    form2.geometry("1366x768")
    form2.configure(bg="#1F6680")

    # VARIABLES
    radio_medio_var = IntVar()
    radio_superior_var = IntVar()
    radio_trabaja_var = IntVar()
    radio_cargo_var = IntVar()

    def getEntradasUsuario():
        
        nivel_medio = radio_medio_var.get()
        nivel_superior = radio_superior_var.get()
        trabaja = radio_trabaja_var.get()
        a_cargo = radio_cargo_var.get()
        provincia_medio = entry_prov.get().strip()
        provincia_superior = entry_prov_ins.get().strip()
        año_ingreso_medio = combo_año_ingreso.get()
        año_egreso_medio = combo_año_egreso.get()
        año_ingreso_superior = combo_año_ingreso_sup.get()
        año_egreso_superior = combo_año_egreso_sup.get()
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
            # Cambia el estado a "readonly" si el widget es un Combobox
            if isinstance(widget, ttk.Combobox) and estado == NORMAL:
                widget.config(state="readonly")
            else:
                widget.config(state=estado)

    def activar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form2.attributes("-fullscreen", False)

    form2.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    form2.bind("<Escape>", desactivar_pantalla_completa)
    form2.bind("<F11>", activar_pantalla_completa)

    label_texto = Label(form, text="*CAMPO OBLIGATORIO", fg="White", font=("Arial", 12))  # Tamaño ajustado
    label_texto.configure(bg="#274357")
    label_texto.place(relx=0.90, y=15, anchor='n')  # Centrar horizontalmente

    # Estudios - Headers
    label_estudios = Label(form2, text="ESTUDIOS:", fg="White", font=("Arial", 24))
    label_estudios.configure(bg="#274357")
    label_estudios.place(x=20, y=80)

    label_nivel = Label(form2, text="NIVEL MEDIO:*", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=140)
    label_nivel = Label(form2, text="NIVEL SUPERIOR:*", fg="White", font=("Arial", 14))
    label_nivel.configure(bg="#1F6680")
    label_nivel.place(x=20, y=250)
    
    # Radiobuttons
    radio_medio_si = Radiobutton(form2, text="Sí", bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_medio_var, value=1)
    radio_medio_si.place(x=170, y=140)
    radio_medio_no = Radiobutton(form2, text="No", bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_medio_var, value=0)
    radio_medio_no.place(x=220, y=140)

    radio_superior_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=1)
    radio_superior_si.place(x=200, y=250)
    radio_superior_no = Radiobutton(form2, text="No",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=0)
    radio_superior_no.place(x=250, y=250)
    radio_superior_en_curso = Radiobutton(form2, text="En curso",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_superior_var, value=2)
    radio_superior_en_curso.place(x=300, y=250)

    radio_trabaja_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_trabaja_var, value=1)
    radio_trabaja_si.place(x=170, y=490)
    radio_trabaja_no = Radiobutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_trabaja_var, value=0)
    radio_trabaja_no.place(x=220, y=490)

    radio_cargo_si = Radiobutton(form2, text="Sí",bg="#1F6680",fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_cargo_var, value=1)
    radio_cargo_si.place(x=950, y=490)
    radio_cargo_no = Radiobutton(form2, text="No",bg="#1F6680", fg="White", font=("Arial", 14), selectcolor="#274357", variable=radio_cargo_var, value=0)
    radio_cargo_no.place(x=1000, y=490)

    # Nivel Medio - Labels y widgets
    años = list(range(1960, 2025))

    label_año_ingreso = Label(form2, text="Año ingreso:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=180)
    
    combo_año_ingreso = ttk.Combobox(form2, values=años, width=10, font=("Arial", 16), state="disabled")
    combo_año_ingreso.set("")  # Valor inicial vacío
    combo_año_ingreso.place(x=20, y=210, width=150)
    
    label_año_egreso = Label(form2, text="Año egreso:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=180)
    
    combo_año_egreso = ttk.Combobox(form2, values=años, width=10, font=("Arial", 16), state="disabled")
    combo_año_egreso.set("")  # Valor inicial vacío
    combo_año_egreso.place(x=190, y=210, width=150)
    
    label_prov = Label(form2, text="Provincia:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov.place(x=370, y=180)
    
    entry_prov = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_prov.place(x=370, y=210, width=400)
    
    label_titulo = Label(form2, text="Título:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_titulo.place(x=800, y=180)
    
    entry_titulo = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_titulo.place(x=800, y=210, width=400)

    # Asignar comando a los Radiobuttons después de crear los widgets
    radio_medio_si.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, combo_año_ingreso, combo_año_egreso, entry_titulo))
    radio_medio_no.config(command=lambda: toggle_entries(radio_medio_var, entry_prov, combo_año_ingreso, combo_año_egreso, entry_titulo))

    # Nivel Superior - Labels y entries
    label_carrera = Label(form2, text="Carrera:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_carrera.place(x=20, y=280)
    entry_carrera = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_carrera.place(x=20, y=310, width=400)

    label_institucion = Label(form2, text="Institución:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_institucion.place(x=450, y=280)
    entry_institucion = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_institucion.place(x=450, y=310, width=400)

    label_prov_ins = Label(form2, text="Provincia:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov_ins.place(x=880, y=280)
    entry_prov_ins = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_prov_ins.place(x=880, y=310, width=400)

    # siguiente fila
    label_año_ingreso = Label(form2, text="Año ingreso:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_ingreso.place(x=20, y=350)
    combo_año_ingreso_sup = ttk.Combobox(form2, values=años, width=10, font=("Arial", 16), state="disabled")
    combo_año_ingreso_sup.set("")  # Valor inicial vacío
    combo_año_ingreso_sup.place(x=20, y=380, width=150)

    label_año_egreso = Label(form2, text="Año egreso:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_año_egreso.place(x=190, y=350)
    combo_año_egreso_sup = ttk.Combobox(form2, values=años, width=10, font=("Arial", 16), state="disabled")
    combo_año_egreso_sup.set("")  # Valor inicial vacío
    combo_año_egreso_sup.place(x=190, y=380, width=150)
    
    # Asignar comando a los Radiobuttons después de crear los widgets
    radio_superior_si.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, combo_año_ingreso_sup, combo_año_egreso_sup))
    radio_superior_no.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, combo_año_ingreso_sup, combo_año_egreso_sup))
    radio_superior_en_curso.config(command=lambda: toggle_entries(radio_superior_var, entry_carrera, entry_institucion, entry_prov_ins, combo_año_ingreso_sup))

    # Situación laboral y responsabilidades - Headers
    label_sit_laboral = Label(form2, text="SITUACIÓN LABORAL:", fg="White", font=("Arial", 24))
    label_sit_laboral.configure(bg="#274357")
    label_sit_laboral.place(x=20, y=430)
    label_responsabilidades = Label(form2, text="RESPONSABILIDADES:", fg="White", font=("Arial", 24))
    label_responsabilidades.configure(bg="#274357")
    label_responsabilidades.place(x=650, y=430)

    label_trabajo = Label(form2, text="¿TRABAJA?:*", fg="White", font=("Arial", 14))
    label_trabajo.configure(bg="#1F6680")
    label_trabajo.place(x=20, y=490)
    label_cargo = Label(form2, text="¿TIENE PERSONAS A CARGO?:*", fg="White", font=("Arial", 14))
    label_cargo.configure(bg="#1F6680")
    label_cargo.place(x=650, y=490)

    # Situación laboral - Labels y entries
    label_horas = Label(form2, text="Horas diarias:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_horas.place(x=20, y=530)
    entry_horas = Entry(form2, font=("Arial", 16), state=DISABLED)
    entry_horas.place(x=20, y=560, width=150)
    label_descrip = Label(form2, text="Breve descripción del trabajo:*", bg="#1F6680", fg="White", font=("Arial", 14))
    label_descrip.place(x=20, y=590)
    texto_descrip = Text(form2, width=50, height=5, font=("Arial", 16), state=DISABLED)
    texto_descrip.place(x=20, y=620)

    # Asignar comando a los Radiobuttons después de crear los widgets
    radio_trabaja_si.config(command=lambda: toggle_entries(radio_trabaja_var, entry_horas, texto_descrip))
    radio_trabaja_no.config(command=lambda: toggle_entries(radio_trabaja_var, entry_horas, texto_descrip))

    #Boton Finalizar
    def finalizar():
        
        nivel_medio, nivel_superior, trabaja, a_cargo, provincia_medio, provincia_superior, año_ingreso_medio, año_egreso_medio, año_ingreso_superior, año_egreso_superior, titulo_medio, carrera_superior, institucion, horas_lab, descripcion_laboral = getEntradasUsuario()
        
        # Lista para almacenar errores
        errores = []

        # Validaciones del formulario 2
        validar_nivel_medio(nivel_medio, provincia_medio, año_ingreso_medio, año_egreso_medio, titulo_medio, errores)
        validar_nivel_superior(nivel_superior, carrera_superior, institucion, provincia_superior, año_ingreso_superior, año_egreso_superior, errores)
        validar_situacion_laboral(trabaja, horas_lab, descripcion_laboral, errores)

        entries = []
        if radio_medio_var.get() == 1:
            entries += [combo_año_ingreso, combo_año_egreso, entry_prov, entry_titulo]
        if radio_superior_var.get() == 1:
            entries += [entry_carrera, entry_institucion, entry_prov_ins, combo_año_ingreso_sup, combo_año_egreso_sup]
        if radio_superior_var.get() == 2:
            entries += [entry_carrera, entry_institucion, entry_prov_ins, combo_año_ingreso_sup]
        if radio_trabaja_var.get() == 1:
            entries += [entry_horas, texto_descrip]
        if len(entries) > 1:
            validar_campos_obligatorios(entries, errores)

        if errores:
            mostrar_errores(errores, form2)
        else:
            datos_temporales["Completo_Nivel_Medio"] = nivel_medio
            datos_temporales["Completo_Nivel_Superior"] = nivel_superior
            datos_temporales["Trabajo"] = trabaja
            datos_temporales["Personas_Cargo"] = a_cargo

            # Nivel Medio
            if radio_medio_var.get() == 1:
                datos_temporales["Año_Ingreso_Medio"] = año_ingreso_medio
                datos_temporales["Año_Egreso_Medio"] = año_egreso_medio
                datos_temporales["Provincia_Medio"] = provincia_medio
                datos_temporales["Titulo_Medio"] = titulo_medio
            else:
                datos_temporales["Año_Ingreso_Medio"] = None
                datos_temporales["Año_Egreso_Medio"] = None
                datos_temporales["Provincia_Medio"] = None
                datos_temporales["Titulo_Medio"] = None

            # Nivel Superior
            if radio_superior_var.get() in [1, 2]:
                datos_temporales["Carrera_Superior"] = carrera_superior
                datos_temporales["Institucion_Superior"] = institucion
                datos_temporales["Provincia_Superior"] = provincia_superior
                datos_temporales["Año_Ingreso_Superior"] = año_ingreso_superior
                datos_temporales["Año_Egreso_Superior"] = None
                if radio_superior_var.get() == 1:  # Solo si es "Sí"
                    datos_temporales["Año_Egreso_Superior"] = año_egreso_superior
            else:
                datos_temporales["Carrera_Superior"] = None
                datos_temporales["Institucion_Superior"] = None
                datos_temporales["Provincia_Superior"] = None
                datos_temporales["Año_Ingreso_Superior"] = None
                datos_temporales["Año_Egreso_Superior"] = None

            # Situación Laboral
            if radio_trabaja_var.get() == 1:
                datos_temporales["Horas_Trabajo"] = horas_lab
                datos_temporales["Descripcion_Trabajo"] = descripcion_laboral
            else:
                datos_temporales["Horas_Trabajo"] = None
                datos_temporales["Descripcion_Trabajo"] = None

            # Agregar campos que faltan y mover el id_carrera
            datos_temporales["Estado"] = "Pendiente"
            # datos_temporales["Fecha_Envio"] = None

            valor = datos_temporales.pop("ID_Carrera")
            datos_temporales["ID_Carrera"] = valor

            print("Datos guardados:", datos_temporales)  # Para verificar en consola

            datos_aspirante = preparar_datos_para_sql(datos_temporales)
            print(datos_aspirante)
            aspirante_id = crear_aspirante(datos_aspirante)

            # confirmar_preinscripcion(aspirante_id)

            form2.destroy()
            mostrar_confirmacion()
    
    boton_siguiente = Button(form2, text="Finalizar", bg="White", fg="Black", font=("Arial", 12), borderwidth=2,command=finalizar)
    boton_siguiente.place(x=1240, y=700, width=120, height=64)

    # Botón para volver atrás

    def volver():
        form2.destroy()
        form.deiconify()
    
    imagen_flecha = Image.open(path_flecha)
    flecha_atras = ImageTk.PhotoImage(imagen_flecha)
    boton_atras = Button(form2, image=flecha_atras, bg="#274357", width=48, height=48, borderwidth=2, command=volver)
    boton_atras.place(x=20, y=20)
    boton_atras.image = flecha_atras  # Mantiene una referencia a la imagen

    form2.mainloop()