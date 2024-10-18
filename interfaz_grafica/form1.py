from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import ttk
from interfaz_grafica.form2 import abrir_ventana_form2
from interfaz_grafica.config import path_flecha
from interfaz_grafica.validaciones import *

# Variable global para almacenar el id_carrera y los datos temporalmente
id_carrera_seleccionada = None
datos_temporales = {}

def abrir_ventana_form1(id_carrera):
    global id_carrera_seleccionada
    id_carrera_seleccionada = id_carrera

    form = Toplevel()
    form.title("Formulario de preinscripción")
    form.geometry("1366x768")
    form.configure(bg="#1F6680")

    def getEntradasUsuario():
        apellido = entry_apellido.get().strip()
        nombre = entry_nombre.get().strip() 
        dni = entry_dni.get().strip()
        telefono = entry_telefono.get().strip()
        correo = entry_email.get().strip()
        domicilio = entry_domicilio.get().strip()
        cuil = entry_cuil.get().strip()
        localidad = entry_localidad.get().strip()
        barrio = entry_barrio.get().strip()
        codigo_postal = entry_cod_postal.get().strip()
        fecha_nacimiento = entry_fecha.get_date()
        sexo = combobox_sexo.get()
        pais_nacimiento = entry_pais.get().strip()
        provincia_nacimiento = entry_prov.get().strip()
        ciudad_nacimiento = entry_ciudad.get().strip()
        
        return (
    apellido, 
    nombre, 
    dni, 
    telefono, 
    correo, 
    domicilio, 
    cuil, 
    localidad, 
    barrio, 
    codigo_postal, 
    fecha_nacimiento, 
    sexo, 
    pais_nacimiento, 
    provincia_nacimiento, 
    ciudad_nacimiento
)

    def activar_pantalla_completa(event=None):
        form.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form.attributes("-fullscreen", False)

    # form.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    form.bind("<Escape>", desactivar_pantalla_completa)
    form.bind("<F11>", activar_pantalla_completa)

    # Título
    label_texto = Label(form, text="FORMULARIO\nPreinscripción", fg="White", font=("Arial", 36))  # Tamaño ajustado
    label_texto.configure(bg="#274357")
    label_texto.place(relx=0.5, y=10, anchor='n')  # Centrar horizontalmente

    # Datos personales
    label_datos = Label(form, text="DATOS PERSONALES:", fg="White", font=("Arial", 24))
    label_datos.configure(bg="#274357")
    label_datos.place(x=20, y=80)

    # Labels y Entrys
    # Primera fila
    label_nombre = Label(form, text="Nombre:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_nombre.place(x=20, y=140)
    entry_nombre = Entry(form, font=("Arial", 16))
    entry_nombre.place(x=20, y=170, width=400)

    label_apellido = Label(form, text="Apellido:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_apellido.place(x=450, y=140)
    entry_apellido = Entry(form, font=("Arial", 16))
    entry_apellido.place(x=450, y=170, width=400)

    label_dni = Label(form, text="DNI:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_dni.place(x=880, y=140)
    entry_dni = Entry(form, font=("Arial", 16))
    entry_dni.place(x=880, y=170, width=400)

    # Segunda fila
    label_cuil = Label(form, text="CUIL/CUIT:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_cuil.place(x=20, y=220)
    entry_cuil = Entry(form, font=("Arial", 16))
    entry_cuil.place(x=20, y=250, width=400)

    label_domicilio = Label(form, text="Domicilio:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_domicilio.place(x=450, y=220)
    entry_domicilio = Entry(form, font=("Arial", 16))
    entry_domicilio.place(x=450, y=250, width=400)

    # lista_provincias = [
    # "Buenos Aires", "CABA", "Catamarca", "Chaco", "Chubut", "Córdoba", 
    # "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", 
    # "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", 
    # "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe", 
    # "Santiago del Estero", "Tierra del Fuego", "Tucumán"
    # ]

    label_localidad = Label(form, text="Localidad:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_localidad.place(x=880, y=220)
    entry_localidad = Entry(form, font=("Arial", 16))
    entry_localidad.place(x=880, y=250, width=400)
    # combobox_provincia = ttk.Combobox(form, values=lista_provincias, font=("Arial", 16), state='readonly')
    # combobox_provincia.set("...")
    # combobox_provincia.place(x=880, y=250, width=400)
  
    # Tercera fila
    label_barrio = Label(form, text="Barrio:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_barrio.place(x=20, y=320)
    entry_barrio = Entry(form, font=("Arial", 16))
    entry_barrio.place(x=20, y=350, width=400)

    label_cod_postal = Label(form, text="Código postal:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_cod_postal.place(x=450, y=320)
    entry_cod_postal = Entry(form, font=("Arial", 16))
    entry_cod_postal.place(x=450, y=350, width=150)

    label_telefono = Label(form, text="Teléfono:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_telefono.place(x=620, y=320)
    entry_telefono = Entry(form, font=("Arial", 16))
    entry_telefono.place(x=620, y=350, width=230)

    label_email = Label(form, text="Email:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_email.place(x=880, y=320)
    entry_email = Entry(form, font=("Arial", 16))
    entry_email.place(x=880, y=350, width=400)

    # Cuarta fila
    label_fecha = Label(form, text="Fecha de nacimiento:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_fecha.place(x=20, y=450)
    entry_fecha = DateEntry(form, font=("Arial", 16), borderwidth=2, state='readonly')
    entry_fecha.place(x=20, y=480, width=400)

    sexo = {
        1: "Masculino",
        2: "Femenino",
        3: "Indefinido",
    }
    lista_sexo = list(sexo.values())
    label_sexo = Label(form, text="Género:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_sexo.place(x=450, y=450)
    combobox_sexo = ttk.Combobox(form, values=lista_sexo, font=("Arial", 16), state='readonly')
    combobox_sexo.set("...")
    combobox_sexo.place(x=450, y=480, width=150)

    # Lugar de nacimiento
    label_nacimiento = Label(form, text="LUGAR DE NACIMIENTO:", fg="White", font=("Arial", 24))
    label_nacimiento.configure(bg="#274357")
    label_nacimiento.place(x=20, y=550)

    # Labels con entry 
    label_pais = Label(form, text="País:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_pais.place(x=20, y=600)
    entry_pais = Entry(form, font=("Arial", 16))
    entry_pais.place(x=20, y=630, width=400)

    label_prov = Label(form, text="Provincia:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_prov.place(x=450, y=600)
    entry_prov = Entry(form, font=("Arial", 16))
    entry_prov.place(x=450, y=630, width=400)

    label_ciudad = Label(form, text="Ciudad:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_ciudad.place(x=880, y=600)
    entry_ciudad = Entry(form, font=("Arial", 16))
    entry_ciudad.place(x=880, y=630, width=400)

    # Botón para volver atrás
    imagen_flecha = Image.open(path_flecha)
    flecha_atras = ImageTk.PhotoImage(imagen_flecha)
    boton_atras = Button(form, image=flecha_atras, bg="#274357", width=48, height=48, borderwidth=2, command=form.destroy)
    boton_atras.place(x=20, y=20)
    boton_atras.image = flecha_atras  # Mantiene una referencia a la imagen

    #Funcion para pasar al siguiente form
    def avanzar_form2():

        apellido, nombre, dni, telefono, correo, domicilio, cuil, localidad, barrio, codigo_postal, fecha_nacimiento, sexo, pais_nacimiento, provincia_nacimiento, ciudad_nacimiento = getEntradasUsuario()

        # Lista para almacenar errores
        errores = []

        # Validaciones del formulario 1
        validar_nombre_apellido(nombre, apellido, errores)
        validar_dni(dni, errores)
        validar_cuil(cuil, errores)
        validar_domicilio(domicilio, errores)
        validar_localidad(localidad, errores)
        validar_barrio(barrio, errores)
        validar_codigo_postal(codigo_postal, errores)
        validar_telefono(telefono, errores)
        verificar_correo(correo, errores)
        validar_fecha(fecha_nacimiento, errores)
        validar_sexo(sexo, errores)
        validar_pais_nacimiento(pais_nacimiento, errores)
        validar_provincia_nacimiento(provincia_nacimiento, errores)
        validar_ciudad_nacimiento(ciudad_nacimiento, errores)

        # Validaciones de campos obligatorios
        entries = [entry_nombre, entry_apellido, entry_dni, entry_cuil, entry_domicilio, 
                   entry_localidad, entry_barrio, entry_cod_postal, entry_telefono, entry_email, 
                   combobox_sexo, entry_pais, entry_prov, entry_ciudad, entry_fecha]
        validar_campos_obligatorios(entries, errores)

        # Si hay errores, mostrar y no avanzar
        if errores:
            mostrar_errores(errores, form)
        else:
            # Guardar los datos temporalmente en el diccionario
            datos_temporales["Nombre"] = nombre
            datos_temporales["Apellido"] = apellido
            datos_temporales["DNI"] = dni
            datos_temporales["Genero"] = sexo
            datos_temporales["CUIL"] = cuil
            datos_temporales["Domicilio"] = domicilio
            datos_temporales["Barrio"] = barrio
            datos_temporales["Localidad"] = localidad
            datos_temporales["Codigo_Postal"] = codigo_postal
            datos_temporales["Telefono"] = telefono
            datos_temporales["Mail"] = correo
            datos_temporales["Fecha_Nacimiento"] = fecha_nacimiento
            datos_temporales["Pais_Nacimiento"] = pais_nacimiento
            datos_temporales["Provincia_Nacimiento"] = provincia_nacimiento
            datos_temporales["Localidad_Nacimiento"] = ciudad_nacimiento

            print("Datos guardados:", datos_temporales)  # Para verificar en consola

            # Código para avanzar a la siguiente parte del formulario
            form.withdraw()
            abrir_ventana_form2(form, datos_temporales)

    # Botón siguiente
    boton_siguiente = Button(form, text="Siguiente", bg="White", fg="Black", font=("Arial", 12), borderwidth=2, command=avanzar_form2)
    boton_siguiente.place(x=1240, y=700, width=120, height=64)

    form.mainloop()
