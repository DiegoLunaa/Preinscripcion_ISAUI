from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from tkinter import *
from db.funciones_db import *

# def abrir_ventana_reportes():
    
def buscar_aspirantes_por_carrera(carrera):
    aspirantes  = leer_todos_los_aspirantes_basico()
    carreras = obtener_carreras_disponibles()
    aspirantes_confirmados = [
        (nombre, apellido, dni, id_carrera, estado) for nombre, apellido, dni, id_carrera, estado in aspirantes if estado == 'Confirmado'
    ]

    if carrera != 0:
        texto = f"Lista de Aspirantes confirmados para {carrera}:"
        aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[0], x[1]))
        for nombre, apellido, dni, id_carrera, estado in aspirantes_confirmados:
            if estado == 'Confirmado' and id_carrera == carrera:
                carrera = obtener_nombre_carrera(id_carrera)
                texto += f"\n{apellido} {nombre}, {dni}, {carrera}"
        cupos = cupos_disponibles(id_carrera)
        texto += f"\n\n<b><font color='red' face='Helvetica'>Cupos disponibles:</font></b> <font color='red' face='Helvetica-Bold'>{cupos}</font>"
    else:
        texto = f"Lista de Aspirantes confirmados de todas las carreras:\n"
        aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[3], x[0], x[1]))  
        for nombre, apellido, dni, id_carrera, estado in aspirantes_confirmados:
            if estado == 'Confirmado':
                carrera = obtener_nombre_carrera(id_carrera)
                texto += f"\n{apellido} {nombre}, {dni}, {carrera}"
        texto += f"\n\n <font color='red' face='Helvetica-Bold'>Cupos disponibles:</font>"
        for carrera in carreras:
            id_carrera, nombre_carrera, cupos_disponibles, cupos_maximos = carrera
            texto += f"\n<b><font color='red' face='Helvetica'>{nombre_carrera}:</font></b> <font color='red' face='Helvetica-Bold'>{cupos_disponibles}</font>"

    def generar_reporte_pdf(nombre_archivo, titulo, contenido):
        doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Agregar título
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontName="Helvetica-Bold",
            fontSize=16,
            textColor=colors.black
        )

        content_style = ParagraphStyle(
            'ContentStyle',
            parent=styles['BodyText'],
            fontName="Helvetica",
            fontSize=10,
            leading=24  # Espaciado entre líneas para mayor legibilidad
        )

        story = []
        title = Paragraph(titulo, title_style)
        story.append(title)

        content_paragraph = Paragraph(contenido.replace("\n", "<br/>"), content_style)
        story.append(content_paragraph)


        # Crear el documento PDF
        doc.build(story)



    
    # Usar la función para crear un reporte
    titulo = "Reporte aspirantes confirmados"
    contenido = texto.replace("\n", "<br/>")  # Convertir saltos de línea para HTML
    nombre_archivo = "reporte_confirmados.pdf"
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

