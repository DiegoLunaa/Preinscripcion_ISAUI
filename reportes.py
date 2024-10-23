from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import *
from mod1 import abrir_mod1
from mod2 import abrir_mod2
from db.funciones_db import *

# def abrir_ventana_reportes():
    
def buscar_aspirantes_por_carrera(carrera):
    aspirantes  = leer_todos_los_aspirantes_basico()

    aspirantes_confirmados = [
        (nombre, apellido, dni, id_carrera, estado) for nombre, apellido, dni, id_carrera, estado in aspirantes if estado == 'Confirmado'
    ]

    if carrera != 0:
        texto = f"Lista de Aspirantes confirmados para {carrera}:\n"
        aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[0], x[1]))
        for nombre, apellido, dni, id_carrera, estado in aspirantes_confirmados:
            if estado == 'Confirmado' and id_carrera == carrera:
                texto += f"Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Carrera: {id_carrera}\n"
    else:
        texto = f"Lista de Aspirantes confirmados de todas las carreras:\n"
        aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[3], x[0], x[1]))  
        for nombre, apellido, dni, id_carrera, estado in aspirantes_confirmados:
            if estado == 'Confirmado':
                texto += f"Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Carrera: {id_carrera}\n"

    def generar_reporte_pdf(nombre_archivo, titulo, contenido):
        # Crear el PDF con tamaño de hoja Carta
        pdf = canvas.Canvas(nombre_archivo, pagesize=letter)
        ancho, alto = letter

        # Establecer título
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(100, alto - 50, titulo)

        # Establecer contenido
        pdf.setFont("Helvetica", 12)
        textobject = pdf.beginText(100, alto - 100)
        textobject.textLines(contenido)

        # Agregar el contenido al PDF
        pdf.drawText(textobject)

        # Guardar el archivo PDF
        pdf.save()

    # Usar la función para crear un reporte
    titulo = "Reporte de Ejemplo"
    contenido = f"""
    {texto}
    """
    nombre_archivo = "reporte_ejemplo.pdf"
    generar_reporte_pdf(nombre_archivo, titulo, contenido)

    print(texto)
    return texto
# Crear la ventana principal
ventana = Tk()
ventana.title("Generar reportes")
ventana.geometry("500x580")
ventana.configure(bg="#1F6680")

# Frame
frame_titulo = Frame(ventana,bg="#274357", width=217, height=75)
frame_titulo.place(x=140,y=17)

#label
label_titulo = Label(frame_titulo, text="GENERAR\nREPORTES", fg="White", font=("Arial", 14))
label_titulo.configure(bg="#274357")
label_titulo.place(relx=0.5, rely=0.5, anchor='center')
# Botones
boton_desarrollo = Button(ventana, text="Desarrollo de Software", command=lambda: buscar_aspirantes_por_carrera(1), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_desarrollo.place(relx=0.5, y=125, anchor='center')

boton_diseño = Button(ventana, text="Diseño de Espacios", command=lambda: buscar_aspirantes_por_carrera(2), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_diseño.place(relx=0.5, y=185, anchor='center')

boton_datos_enfermeria = Button(ventana, text="Enfermería", command=lambda: buscar_aspirantes_por_carrera(3), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_datos_enfermeria.place(relx=0.5, y=245, anchor='center')

boton_turismo_hoteleria = Button(ventana, text="Turismo y hotelería", command=lambda: buscar_aspirantes_por_carrera(4), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_turismo_hoteleria.place(relx=0.5, y=305, anchor='center')

boton_datos_turismo = Button(ventana, text="Guía de Turismo", command=lambda: buscar_aspirantes_por_carrera(5), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_datos_turismo.place(relx=0.5, y=365, anchor='center')

boton_trekking = Button(ventana, text="Guía de Trekking", command=lambda: buscar_aspirantes_por_carrera(6), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_trekking.place(relx=0.5, y=425, anchor='center')

boton_todas = Button(ventana, text="Todas las carreras", command=lambda: buscar_aspirantes_por_carrera(0), bg="#274357", width=25, fg="White", font=("Arial", 10))
boton_todas.place(relx=0.5, y=485, anchor='center')

boton_salir = Button(ventana,text="Salir",command=ventana.destroy,bg="#274357", width=25,fg="White", font=("Arial", 10))
boton_salir.place(relx=0.5, y = 545, anchor='center')



ventana.mainloop()

def generar_reporte_pdf(nombre_archivo, titulo, contenido):
    # Crear el PDF con tamaño de hoja Carta
    pdf = canvas.Canvas(nombre_archivo, pagesize=letter)
    ancho, alto = letter

    # Establecer título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, alto - 50, titulo)

    # Establecer contenido
    pdf.setFont("Helvetica", 12)
    textobject = pdf.beginText(100, alto - 100)
    textobject.textLines(contenido)

    # Agregar el contenido al PDF
    pdf.drawText(textobject)

    # Guardar el archivo PDF
    pdf.save()

# Usar la función para crear un reporte
titulo = "Reporte de Ejemplo"
contenido = """
{texto}
"""
nombre_archivo = "reporte_ejemplo.pdf"
generar_reporte_pdf(nombre_archivo, titulo, contenido)
