import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox, ttk

# Función para enviar correo
def enviar_notificacion():
    destinatario = entrada_destinatario.get()
    asunto = entrada_asunto.get()
    cuerpo = entrada_cuerpo.get("1.0", END)  

    # Para usar HTML en el correo.
    # cuerpo_html = f"""
    # <html>
    #     <body>
    #         <h2 style="color:blue;">{asunto}</h2>
    #         <p>{cuerpo}</p>
    #     </body>
    # </html>
    # """
    
    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    remitente = "isauipruebatecnica@gmail.com"
    contraseña = "" # Contraseña de app.
    
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto  
    
    # Adjuntar el cuerpo del mensaje con codificación UTF-8
    mensaje.attach(MIMEText(cuerpo, "plain", "utf-8"))  # Si se usara HTML esto se debe cambiar
    
    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()  
        servidor.login(remitente, contraseña)
        
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        
        messagebox.showinfo("Éxito", "Correo enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")

# Función para actualizar el asunto y el cuerpo al seleccionar un mensaje
def actualizar_mensaje(event):
    seleccionado = combobox_mensajes.get()
    if seleccionado in mensajes_predeterminados:
        asunto, cuerpo = mensajes_predeterminados[seleccionado]
        entrada_asunto.delete(0, END)
        entrada_asunto.insert(0, asunto)
        entrada_cuerpo.delete("1.0", END)
        entrada_cuerpo.insert("1.0", cuerpo)


ventana = Tk()
ventana.title("Enviar Notificaciones vía Gmail")
ventana.geometry("800x600") 


padding = 10


label_destinatario = Label(ventana, text="Destinatario:", font=("Arial", 12))
label_destinatario.pack(pady=padding)
entrada_destinatario = Entry(ventana, width=60, font=("Arial", 12))
entrada_destinatario.pack(pady=padding)

label_asunto = Label(ventana, text="Asunto:", font=("Arial", 12))
label_asunto.pack(pady=padding)
entrada_asunto = Entry(ventana, width=60, font=("Arial", 12))
entrada_asunto.pack(pady=padding)

label_cuerpo = Label(ventana, text="Cuerpo del Mensaje:", font=("Arial", 12))
label_cuerpo.pack(pady=padding)
entrada_cuerpo = Text(ventana, width=60, height=10, font=("Arial", 12), wrap=WORD)
entrada_cuerpo.pack(pady=padding)

label_mensajes = Label(ventana, text="Seleccionar Mensaje Predeterminado:", font=("Arial", 12))
label_mensajes.pack(pady=padding)

mensajes_predeterminados = {
    "Falta de documentos.": ("Información faltante en su preinscripción", """Le escribimos desde el Instituto Superior Arturo Umberto Illia para informarle que, al revisar su solicitud de preinscripción a la carrera de [Nombre de la Carrera], hemos detectado que falta información necesaria para completar su proceso de preinscripción. Los documentos/información faltante son los siguientes:
                             
[Detalle de la información o documentos faltantes]
                             
Le solicitamos que nos envíe la documentación/información requerida a la mayor brevedad posible, ya que su preinscripción no podrá ser procesada hasta que contemos con todos los datos necesarios.
Puede enviarnos la información respondiendo directamente a este correo o acercandose a la institución.
Quedamos a su disposición para cualquier consulta o asistencia que necesite en este proceso.
Atentamente,
Secretaría
Instituto Superior Arturo Umberto Illia
03541 43-1501
secretaria@isaui.edu.ar"""),
    "Información erronea.": ("Corrección necesaria en su preinscripción", """Estimado/a:
Le escribimos desde el Instituto Superior Arturo Umberto Illia para informarle que, al revisar su solicitud de preinscripción, hemos encontrado información que requiere corrección.
Específicamente, hemos identificado lo siguiente:
                  
[Detalle de la información errónea]
                  
Le solicitamos que revise la información proporcionada y nos envíe la corrección a la mayor brevedad posible, ya que su preinscripción no podrá ser procesada hasta que tengamos los datos correctos.
Puede enviarnos la información respondiendo directamente a este correo o acercandose a la institución.
Quedamos a su disposición para cualquier consulta o asistencia que necesite en este proceso.
Atentamente,
Secretaría
Instituto Superior Arturo Umberto Illia
03541 43-1501
secretaria@isaui.edu.ar"""),
}

# ComboBox con mensajes predeterminados
combobox_mensajes = ttk.Combobox(ventana, values=list(mensajes_predeterminados.keys()), width=60, font=("Arial", 12))
combobox_mensajes.pack(pady=padding)
combobox_mensajes.current(0)  # Seleccionar por defecto el primer mensaje
combobox_mensajes.bind("<<ComboboxSelected>>", actualizar_mensaje)  # Vincular la función


boton_enviar = Button(ventana, text="Enviar Correo", command=enviar_notificacion, font=("Arial", 12), bg="lightblue")
boton_enviar.pack(pady=20)


ventana.mainloop()
