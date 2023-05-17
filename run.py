from buscador_camara.camaras import *

def run():
    app = Tk()
    app.title('Camaras TyM - 208')
    app.iconbitmap("imagenes/buscador.ico")
    app.resizable(0,0)


    ventana = Camaras(app)
    ventana.config(bg='gray24')
    ventana.mainloop()


if __name__ == "__main__":
    run()
