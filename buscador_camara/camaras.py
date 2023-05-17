from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datos.datos import Funciones
import webbrowser
import os



class Camaras(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()


    def inicializar_gui(self):

        self.ip_camara = StringVar()
        self.usuario = StringVar()
        self.password = StringVar()


        # FRAME
        self.frame = LabelFrame(self, text="Estado de Camaras",fg='snow',bg='gray24',font=('Arial',15))
        self.frame.pack(fill="both", expand="yes", padx=20, pady=10)

        # BUZON
        self.lbl_buzon = Label(self.frame, text="Camara:",fg='green2', bg='gray24')
        self.lbl_buzon.grid(row=0, column=0, padx=10, pady=10)

        # COMBOBOX

        equipo = Funciones().mostrar_equipos()

        self.combo_ubi = ttk.Combobox(self.frame,width=30, justify=CENTER, value=equipo)
        self.combo_ubi.grid(row=1,column=0,padx=10,pady=10)
        self.combo_ubi.current(0)
        self.combo_ubi.bind("<<ComboboxSelected>>", self.buscar_ubicacion)

        self.lbl_camara = Label(self.frame, text='IP Camara',fg='green2', bg='gray24')
        self.lbl_camara.grid(row=0,column=1,padx=10,pady=10)

        self.txt_camara = Entry(self.frame,justify=CENTER,textvariable=self.ip_camara)
        self.txt_camara.grid(row=1,column=1,padx=10,pady=10)

        self.lbl_usuario = Label(self.frame, text='Usuario',fg='green2', bg='gray24')
        self.lbl_usuario.grid(row=2,column=0,padx=10,pady=10)

        self.txt_usuario = Entry(self.frame,width=30,justify=CENTER,textvariable=self.usuario)
        self.txt_usuario.grid(row=3,column=0,padx=10,pady=10)


        self.lbl_pass = Label(self.frame, text='Password',fg='green2', bg='gray24')
        self.lbl_pass.grid(row=2,column=1,padx=10,pady=10)

        self.txt_pass = Entry(self.frame,justify=CENTER,textvariable=self.password)
        self.txt_pass.grid(row=3,column=1,padx=10,pady=10)

#BOTONES

        # BOTON CONSULTAR IP PLC
        self.btn_consultar = Button(self.frame, text="IP",cursor='hand2', command=self.ping_camara)
        self.btn_consultar.grid(row=1, column=2,columnspan=2, padx=10, pady=10, sticky=W+E)

#BOTONES CAMARA 1
        self.btn_cam1 = Button(self.frame, text="Ver Navegador",cursor='hand2', command=self.conectarse_cam)
        self.btn_cam1.grid(row=3, column=2, padx=10, pady=10)


#==============================================================================================
#FUNCIONES

    def buscar_ubicacion(self,dato):

        dato = self.combo_ubi.get()

        self.leer_ip_cam(dato)
        self.leer_usuario(dato)
        self.leer_pass(dato)


    def leer_ip_cam(self,dato):

        buscar = Funciones().buscar_camara(dato)
        self.ip_camara.set(buscar)


    def leer_usuario(self,dato):

        buscar = Funciones().buscar_usuario(dato)
        self.usuario.set(buscar)


    def leer_pass(self,dato):

        buscar = Funciones().buscar_pass(dato)
        self.password.set(buscar)

#==============================================================================================
#FUNCIONES DE BOTONES

    def ping_camara(self):

        ip_camara = self.txt_camara.get()

        if ip_camara:
            os.system(f'ping -t {ip_camara}')
        else:
            messagebox.showwarning('Mensaje', 'No a introducido ningun valor.')


    def conectarse_cam(self):

        ip_camara = self.txt_camara.get()

        if ip_camara:
            webbrowser.open_new_tab(f'http://{ip_camara}')
        else:
            messagebox.showwarning('Mensaje','No se a introducido ningun valor.')