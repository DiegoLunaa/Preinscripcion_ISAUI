from tkinter import *
from PIL import Image, ImageTk
from main_adm import abrir_ventana_main_adm
from interfaz_grafica.config import path_usuario


def abrir_ventana_login():
    login = Toplevel()
    login.title("Login Administrador")
    login.geometry("1366x768")
    login.configure(bg="#1F6680")

    def activar_pantalla_completa(event=None):
        login.attributes("-fullscreen", True)

    def desactivar_pantalla_completa(event=None):
        login.attributes("-fullscreen", False)

    login.attributes("-fullscreen", True)  # Iniciar en pantalla completa
    login.bind("<Escape>", desactivar_pantalla_completa)
    login.bind("<F11>", activar_pantalla_completa)
    
    #Frames
    frame1 = Frame(login, bg="#274357", width=75, height=768)
    frame1.place(x=20, y=0)  
    frame2 = Frame(login, bg="#274357", width=75, height=768)
    frame2.place(x=1271, y=0)  
    frame3 = Frame(login, bg="#274357", width=800, height=600)
    frame3.place(relx=0.5, y=75, anchor='n')

    #Logo usuario
    imagen = Image.open(path_usuario)
    imagen_redimensionada = imagen.resize((250, 250)) 
    imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
    label_imagen_usuario = Label(login, image=imagen_logo, bg="#274357")
    label_imagen_usuario.place(relx=0.5, y=80, anchor='n')  

    label_imagen_usuario.image = imagen_logo  # Mantiene una referencia a la imagen

    #Label administrador

    label_administrador = Label(login, text="ADMINISTRADOR", fg="White", font=("Arial", 28))
    label_administrador.configure(bg="#274357")
    label_administrador.place(relx=0.5, y=350, anchor='n')

    #Entrys
    label_usuario = Label(login, text="USUARIO:", bg="#274357", fg="White", font=("Arial", 10))
    label_usuario.place(x=555, y=425)
    entry_usuario = Entry(login, font=("Arial", 16))
    entry_usuario.place(relx=0.5, y=450, anchor='n')

    label_contraseña = Label(login, text="CONTRASEÑA:", bg="#274357", fg="White", font=("Arial", 10))
    label_contraseña.place(x=555, y=485)
    entry_contraseña = Entry(login, font=("Arial", 16))
    entry_contraseña.place(relx=0.5, y=510, anchor='n')

    #Check recuérdame
    check_recuerdame = Checkbutton(login, text="Recuérdame",bg="#274357",fg="White", font=("Arial", 12), selectcolor="#274357")
    check_recuerdame.place(x=555, y=550)

    #Botón ingresar
    def ingresar():
        login.withdraw()
        abrir_ventana_main_adm(login)

    boton_ingresar = Button(login, text="Ingresar", width=12, fg="Black", font=("Arial", 12), bg="White", command=ingresar)
    boton_ingresar.place(x=930, y=620)  