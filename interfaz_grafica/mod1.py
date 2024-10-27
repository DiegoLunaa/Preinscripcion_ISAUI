from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import ttk
from interfaz_grafica.config import path_flecha
from interfaz_grafica.validaciones import *
from db.funciones_db import *
import datetime


# from validaciones import mostrar_errores

# Variable global para almacenar el id_carrera y los datos temporalmente
id_carrera_seleccionada = None
datos_aspirante = {}

def abrir_mod1(aspirante_id):

    form = Toplevel()
    form.title("Modificar datos personales")
    form.geometry("1366x768")
    form.configure(bg="#1F6680")

    aspirante_info = leer_aspirante(aspirante_id)
    print(f"ID:  {aspirante_id}")

    if aspirante_info is None:
        print(f"No se encontraron datos para el alumno con ID: {aspirante_id}")
        return  # Salir de la función si no se encuentran datos


    def getEntradasUsuario():
        apellido_nuevo = entry_apellido.get().strip()
        nombre_nuevo = entry_nombre.get().strip() 
        dni_nuevo = entry_dni.get().strip()
        telefono_nuevo = entry_telefono.get().strip()
        email_nuevo = entry_email.get().strip()
        domicilio_nuevo = entry_domicilio.get().strip()
        cuil_nuevo = entry_cuil.get().strip()
        localidad_nuevo = entry_localidad.get().strip()
        barrio_nuevo = entry_barrio.get().strip()
        codigo_postal_nuevo = entry_cod_postal.get().strip()
        fecha_nacimiento_nuevo = entry_fecha.get_date()
        sexo_nuevo = combobox_sexo.get()
        pais_nacimiento_nuevo = entry_pais.get().strip()
        provincia_nacimiento_nuevo = entry_prov.get().strip()
        ciudad_nacimiento_nuevo = entry_ciudad.get().strip()
        
        return (
    nombre_nuevo, apellido_nuevo, dni_nuevo, sexo_nuevo, 
    cuil_nuevo, domicilio_nuevo, barrio_nuevo, localidad_nuevo,
    codigo_postal_nuevo, telefono_nuevo, email_nuevo, 
    fecha_nacimiento_nuevo, pais_nacimiento_nuevo,
    provincia_nacimiento_nuevo, ciudad_nacimiento_nuevo
)
    


    def activar_pantalla_completa(event=None):
        form.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        form.attributes("-fullscreen", False)

    form.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    form.bind("<Escape>", desactivar_pantalla_completa)
    form.bind("<F11>", activar_pantalla_completa)

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

    label_localidad = Label(form, text="Localidad:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_localidad.place(x=880, y=220)
    entry_localidad = Entry(form, font=("Arial", 16))
    entry_localidad.place(x=880, y=250, width=400)
  

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
    current_year = datetime.datetime.now().year
    # Cuarta fila
    label_fecha = Label(form, text="Fecha de nacimiento:", bg="#1F6680", fg="White", font=("Arial", 14))
    label_fecha.place(x=20, y=450)
    entry_fecha = DateEntry(form, font=("Arial", 16), borderwidth=2, 
                        year=current_year, date_pattern='dd/mm/yyyy',
                        mindate=datetime.date(1900, 1, 1),
                        maxdate=datetime.date(current_year, 12, 31))
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
    (
    id, nombre_actual, apellido_actual, dni_actual, sexo_actual, 
    cuil_actual, domicilio_actual, barrio_actual, localidad_personal_actual,
    codigo_postal_actual, telefono_actual, email_actual,  
    fecha_nacimiento_actual, pais_nacimiento_actual,
    provincia_nacimiento_actual, ciudad_nacimiento_actual, *otros_campos
) = aspirante_info
    
    cargar_datos = [
        (entry_nombre, nombre_actual),
        (entry_apellido, apellido_actual),
        (entry_dni, dni_actual),
        (combobox_sexo, sexo_actual),
        (entry_cuil, cuil_actual),
        (entry_domicilio, domicilio_actual),
        (entry_barrio, barrio_actual),
        (entry_localidad, localidad_personal_actual),
        (entry_cod_postal, codigo_postal_actual),
        (entry_telefono, telefono_actual),
        (entry_email, email_actual),
        (entry_fecha, fecha_nacimiento_actual),
        (entry_pais, pais_nacimiento_actual),
        (entry_prov, provincia_nacimiento_actual),
        (entry_ciudad, ciudad_nacimiento_actual)
    ]

    for clave, valor in cargar_datos:
        if valor is not None:
            if isinstance(clave, ttk.Combobox):
                clave.set(valor)
            elif isinstance(clave, DateEntry):
                clave.set_date(valor)
            else:
                clave.insert(0, valor)

    def guardar_validar():
        cambios = {}
        (
            nombre_nuevo, apellido_nuevo, dni_nuevo, sexo_nuevo, 
            cuil_nuevo, domicilio_nuevo, barrio_nuevo, localidad_personal_nuevo,
            codigo_postal_nuevo, telefono_nuevo, email_nuevo, 
            fecha_nacimiento_nuevo, pais_nacimiento_nuevo,
            provincia_nacimiento_nuevo, ciudad_nacimiento_nuevo
                       ) = getEntradasUsuario()

        # Lista para almacenar errores
        errores = []

        # Validaciones del formulario 1
        validar_nombre_apellido(nombre_nuevo, apellido_nuevo, errores)
        validar_dni(dni_nuevo, errores, dni_actual)
        validar_cuil(cuil_nuevo, errores)
        validar_domicilio(domicilio_nuevo, errores)
        validar_localidad(localidad_personal_nuevo, errores) #localidad
        validar_barrio(barrio_nuevo, errores)
        validar_codigo_postal(codigo_postal_nuevo, errores)
        validar_telefono(telefono_nuevo, errores)
        verificar_correo(email_nuevo, errores, email_actual)
        validar_fecha(fecha_nacimiento_nuevo, errores)
        validar_sexo(sexo_nuevo, errores)
        validar_pais_nacimiento(pais_nacimiento_nuevo, errores)
        validar_provincia_nacimiento(provincia_nacimiento_nuevo, errores)
        validar_ciudad_nacimiento(ciudad_nacimiento_nuevo, errores)

        # Validaciones de campos obligatorios
        entries = [entry_nombre, entry_apellido, entry_dni, entry_cuil, entry_domicilio, 
                   entry_localidad, entry_barrio, entry_cod_postal, entry_telefono, entry_email, 
                   combobox_sexo, entry_pais, entry_prov, entry_ciudad, entry_fecha]
        validar_campos_obligatorios(entries, errores)

        datos = [
        ('nombre', nombre_nuevo, nombre_actual),
        ('apellido', apellido_nuevo, apellido_actual),
        ('dni', dni_nuevo, dni_actual),
        ('genero', sexo_nuevo, sexo_actual),
        ('cuil', cuil_nuevo, cuil_actual),
        ('domicilio', domicilio_nuevo, domicilio_actual),
        ('barrio', barrio_nuevo, barrio_actual),
        ('localidad', localidad_personal_nuevo, localidad_personal_actual),
        ('codigo_postal', codigo_postal_nuevo, codigo_postal_actual),
        ('telefono', telefono_nuevo, telefono_actual),
        ('mail', email_nuevo, email_actual),
        ('fecha_nacimiento', fecha_nacimiento_nuevo, fecha_nacimiento_actual),
        ('pais_nacimiento', pais_nacimiento_nuevo, pais_nacimiento_actual),
        ('provincia_nacimiento', provincia_nacimiento_nuevo, provincia_nacimiento_actual),
        ('localidad_nacimiento', ciudad_nacimiento_nuevo, ciudad_nacimiento_actual)
    ]
        
        for campo, nuevo_valor, valor_actual in datos:
            if nuevo_valor != valor_actual:
                cambios[campo] = nuevo_valor
    
        # Si hay errores, mostrar y no avanzar
        if errores:
            mostrar_errores(errores, form)
        elif cambios:
            actualizar_aspirante(aspirante_id, cambios)
            messagebox.showinfo("Éxito", "Los datos se han guardado correctamente.", parent=form)
        else:
            messagebox.showinfo("Sin cambios", "No se realizaron cambios en los datos.", parent=form)

        form.destroy()  # Esto cerrará la ventana actual

    boton_siguiente = Button(form, text="Guardar", bg="White", fg="Black", font=("Arial", 12), borderwidth=2, command=guardar_validar)
    boton_siguiente.place(x=1240, y=700, width=120, height=64)

    form.mainloop()
