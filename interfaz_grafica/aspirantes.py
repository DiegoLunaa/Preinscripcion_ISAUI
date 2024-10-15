import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

aspirantes = tk.Tk()
aspirantes.title("PANTALLA DE CUPOS")
aspirantes.geometry("1366x768") 
aspirantes.configure(bg="#274357")

#frames
frame1 = tk.Frame(aspirantes, bg="#1F6680", width=249, height=768)
frame1.place(x=0, y=0)  
frame2 = tk.Frame(aspirantes, bg="#1F6680", width=1052, height=713)
frame2.place(x=314, y=55) 

imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Preinscripcion_ISAUI/interfaz_grafica/isaui.png")
imagen_redimensionada = imagen.resize((230, 200)) 
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen_isaui = tk.Label(aspirantes, image=imagen_logo, bg="#1F6680")
label_imagen_isaui.place(x=0, y=-22)
label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen


#Arbol

frame_arbol = tk.Frame(aspirantes, width=920, height=458)
frame_arbol.place(x=380, y=181)
frame_arbol.pack_propagate(False) #No cambia de tamaño / tamaño fijo

arbol = ttk.Treeview(frame_arbol, columns=("n° Orden","apellido", "nombre", "dni", "carrera","acciones"), show="headings")
arbol.pack(fill="both", expand=True) #Esto es para que ocupe todo el frame que cree recién. El frame_arbol

arbol.heading("n° Orden", text="N° Orden")
arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")
arbol.heading("acciones", text="Acciones")

arbol.column("n° Orden", width=50) 
arbol.column("apellido", width=110)
arbol.column("nombre", width=110)
arbol.column("dni", width=100)
arbol.column("carrera", width=200)
arbol.column("acciones", width=350)

#Botones
boton_aspirantes = tk.Button(aspirantes, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_aspirantes.place(x=64, y=184) 
    
boton_cupos = tk.Button(aspirantes, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_cupos.place(x=64, y=249)  

boton_en_espera = tk.Button(aspirantes, text="EN ESPERA", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_en_espera.place(x=1039, y=679)  

boton_confirmados = tk.Button(aspirantes, text="CONFIRMADOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_confirmados.place(x=1184, y=679)  

#Botones superiores
boton_inicio = tk.Button(aspirantes, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
boton_inicio.place(x=1068, y=10)

boton_cerrar_sesion = tk.Button(aspirantes, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
boton_cerrar_sesion.place(x=1215, y=10)

#combobox
combobox_carreras = ttk.Combobox(aspirantes, font=("Arial", 14), state='readonly')
combobox_carreras.set("Filtrado de carrera")
combobox_carreras.place(x=380, y=100)

#Botones de acciones


aspirantes.mainloop()
