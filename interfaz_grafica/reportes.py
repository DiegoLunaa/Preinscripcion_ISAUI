from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from db.funciones_db import *

def abrir_ventana_reportes():
    ventana = Tk()
    ventana.title("Generar reportes")
    ventana.configure(bg="#1F6680")
    ventana.resizable(False, False)
    ventana.protocol("WM_DELETE_WINDOW", lambda: None) #PARA QUE NO FUNCIONE LA X DE WINDOWS
    ventana.bind("<Configure>", lambda evento: ventana.state("normal")) #NO FUNCIONA MAXIMIZAR NI MINIMIZAR

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 500
    alto_ventana = 300

    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Frame
    frame_titulo = Frame(ventana,bg="#274357", width=217, height=75)
    frame_titulo.place(x=140,y=17)

    #label
    label_titulo = Label(frame_titulo, text="GENERAR\nREPORTES", fg="White", font=("Arial", 14))
    label_titulo.configure(bg="#274357")
    label_titulo.place(relx=0.5, rely=0.5, anchor='center')

    def seleccionar_opcion():
        seleccion = opciones.get()
        if seleccion == "Selecciona una opción": 
            messagebox.showwarning("Error", "Por favor, selecciona una opción.")
            return 
        opcion = opciones_carreras[seleccion]
        print(f'Seleccionaste: {seleccion}, Valor numérico: {opcion}')
        buscar_aspirantes_por_carrera(opcion)
        

    opciones_carreras = {
        "Desarrollo de Software": 1,
        "Diseño de Espacios": 2,
        "Enfermería": 3,
        "Turismo y Hotelería": 4,
        "Turismo": 5,
        "Guía de Trekking": 6,
        "Todas las carreras": 0
    }

    opciones = ttk.Combobox(ventana, values=list(opciones_carreras.keys()), width=25, font=("Arial", 10))
    opciones.config(state='readonly')
    opciones.set("Selecciona una opción")
    opciones.place(relx=0.5, y=125, anchor='center') 

    boton_imprimir = Button(ventana, text="Imprimir", command=seleccionar_opcion, bg="#274357", width=25, fg="White", font=("Arial", 10))
    boton_imprimir.place(relx=0.5, y=185, anchor='center')

    boton_salir = Button(ventana,text="Salir",command=ventana.destroy,bg="#274357", width=25,fg="White", font=("Arial", 10))
    boton_salir.place(relx=0.5, y = 245, anchor='center')

    def buscar_aspirantes_por_carrera(carrera):
        aspirantes  = leer_todos_los_aspirantes_basico()
        esperando = contar_aspirantes_espera()
        confirmados = contar_confirmados_por_carrera()

        aspirantes_confirmados = [
            (nombre, apellido, dni, id_carrera, estado, activo) for nombre, apellido, dni, id_carrera, estado, activo in aspirantes if estado == 'Confirmado'
        ]

        if carrera != 0:
            nombre_carrera = obtener_nombre_carrera(carrera)
            texto = f"<b><font face='Helvetica-Bold'>Lista de Aspirantes confirmados para {nombre_carrera}:</font></b>"
            aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[0], x[1]))
            for nombre, apellido, dni, id_carrera, estado, activo in aspirantes_confirmados:
                if estado == 'Confirmado' and id_carrera == carrera and activo == 1:
                    nombre_carrera = obtener_nombre_carrera(id_carrera)
                    texto += f"\n{apellido} {nombre}, {dni}, {nombre_carrera}"
            cantidad_confirmados = confirmados.get(carrera, 0)
            cantidad_esperando = esperando.get(carrera, 0)
            cupos = cupos_disponibles(carrera)
            texto += f"\n<b><font color='red' face='Helvetica-Bold'>Cantidad de confirmados: {cantidad_confirmados}</font></b>\n"
            texto += f"<b><font color='red' face='Helvetica-Bold'>Cantidad de personas en espera: {cantidad_esperando}</font></b>\n"
            texto += f"<b><font color='red' face='Helvetica-Bold'>Cupos disponibles: {cupos}</font></b>\n\n"

        else:
            texto = ''
            for i in range(1, 7):
                nombre_carrera = obtener_nombre_carrera(i)
                texto += f"<b><font face='Helvetica-Bold'>Confirmados para la {nombre_carrera}:</font></b>"
                aspirantes_confirmados = sorted(aspirantes_confirmados, key=lambda x: (x[0], x[1]))
                for nombre, apellido, dni, id_carrera, estado, activo in aspirantes_confirmados:
                    if estado == 'Confirmado' and id_carrera == i and activo == 1:
                        texto += f"\n{apellido} {nombre}, {dni}"
                cupos = cupos_disponibles(i)
                cantidad_confirmados = confirmados.get(i, 0)
                cantidad_esperando = esperando.get(i, 0)
                texto += f"\n<b><font color='red' face='Helvetica-Bold'>Cantidad de confirmados: {cantidad_confirmados}</font></b>"
                texto += f"\n<b><font color='red' face='Helvetica-Bold'>Cantidad de personas en espera: {cantidad_esperando}</font></b>"
                texto += f"\n<b><font color='red' face='Helvetica-Bold'>Cupos disponibles: {cupos}</font></b>\n\n"

        def generar_reporte_pdf(nombre_archivo, titulo, contenido):
            nombre_archivo = filedialog.asksaveasfilename(defaultextension=".pdf",
            initialfile='reporte',
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            parent=ventana)
            if not nombre_archivo:  
                return
            doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

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
                leading=24  
            )

            story = []
            title = Paragraph(titulo, title_style)
            story.append(title)

            content_paragraph = Paragraph(contenido.replace("\n", "<br/>"), content_style)
            story.append(content_paragraph)

            # Crear el documento PDF
            doc.build(story)

        titulo = "Reporte sobre los aspirantes confirmados"
        contenido = texto.replace("\n", "<br/>")  # Convertir saltos de línea para HTML
        nombre_archivo = "reporte_confirmados.pdf"
        generar_reporte_pdf(nombre_archivo, titulo, contenido)

    ventana.mainloop()

