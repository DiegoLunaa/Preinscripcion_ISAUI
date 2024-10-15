import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

cupos = tk.Tk()
cupos.title("PANTALLA DE CUPOS")
cupos.geometry("1366x768") 
cupos.configure(bg="#274357")

#funciones

def actualizar_progreso():
    global cupos_confirmados
    if cupos_confirmados < cupos_totales:
        cupos_confirmados += 1  # Incrementar cupo confirmado
        progress_bar_soft['value'] = (cupos_confirmados / cupos_totales) * 100  # Actualizar progreso
        cupos_restantes = cupos_totales - cupos_confirmados
        label_cupos.config(text=f"Cupos restantes: {cupos_restantes}")

#frames
frame1 = tk.Frame(cupos, bg="#1F6680", width=249, height=768)
frame1.place(x=0, y=0)  
frame2 = tk.Frame(cupos, bg="#1F6680", width=1052, height=713)
frame2.place(x=314, y=55)  

imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Preinscripcion_ISAUI/interfaz_grafica/isaui.png")
imagen_redimensionada = imagen.resize((230, 200)) 
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen_isaui = tk.Label(cupos, image=imagen_logo, bg="#1F6680")
label_imagen_isaui.place(x=0, y=-22)
label_imagen_isaui.image = imagen_logo  # Mantiene una referencia a la imagen

frame_cupo = tk.Frame(cupos,bg="#274357",width=788, height=101)
frame_cupo.place(x=446, y=83)
#Label cupo
label_texto = tk.Label(cupos, text="CUPOS", fg="White", font=("Arial", 40))  # Tamaño ajustado
label_texto.configure(bg="#274357")
label_texto.place(x=730, y=100)

#Botones
boton_aspirantes = tk.Button(cupos, text="ASPIRANTES", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_aspirantes.place(x=64, y=184) 
    
boton_cupos = tk.Button(cupos, text="CUPOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_cupos.place(x=64, y=249)  

boton_en_espera = tk.Button(cupos, text="EN ESPERA", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2)
boton_en_espera.place(x=64, y=314)  

boton_confirmados = tk.Button(cupos, text="CONFIRMADOS", width=14, fg="White", font=("Arial", 12), bg="#274357",borderwidth=2,command= actualizar_progreso)
boton_confirmados.place(x=64, y=379)  

    #Botones superiores
boton_inicio = tk.Button(cupos, text="VOLVER", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
boton_inicio.place(x=1068, y=10)

boton_cerrar_sesion = tk.Button(cupos, text="CERRAR SESIÓN", width=14, fg="White", font=("Arial", 12), bg="#1F6680",borderwidth=2)
boton_cerrar_sesion.place(x=1215, y=10)

#CUPOS
cupos_confirmados = 0
cupos_totales = 50
cupos_restantes = cupos_totales - cupos_confirmados

label_texto = tk.Label(cupos, text="DESARROLLO DE SOFTWARE", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=400, y=250)
progress_bar_soft = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar_soft.place(x=400,y=300,width=400)
label_cupos = tk.Label(cupos, text=f"Cupos restantes: {cupos_restantes}", fg="White", font=("Arial", 14), bg="#1F6680")
label_cupos.place(x=400, y=330)


label_texto = tk.Label(cupos, text="DISEÑO DE ESPACIOS", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=400, y=389)
progress_bar = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar.place(x=400,y=442,width=400)

label_texto = tk.Label(cupos, text="TREKKING", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=400, y=530)
progress_bar = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar.place(x=400,y=583,width=400)

label_texto = tk.Label(cupos, text="GUÍA DE TURISMO", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=877, y=250)
progress_bar = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar.place(x=877,y=300,width=400)

label_texto = tk.Label(cupos, text="TURISMO Y HOTELERÍA", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=877, y=389)
progress_bar = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar.place(x=877,y=442,width=400)

label_texto = tk.Label(cupos, text="ENFERMERÍA", fg="White", font=("Arial", 20))
label_texto.configure(bg="#1F6680")
label_texto.place(x=877, y=530)
progress_bar = ttk.Progressbar(cupos, orient="horizontal",mode="determinate")
progress_bar.place(x=877,y=583,width=400)



tk.mainloop()