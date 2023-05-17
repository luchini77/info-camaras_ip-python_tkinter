import pandas as pd

class Funciones:

    def mostrar_equipos(self):
        leer = pd.read_excel('datos/camaras_TyM_208.xlsx')
        equipo = leer['ubicación']
        lista = list()

        for i in equipo:
            lista.append(i)

        return lista


    def buscar_camara(self,dato):
        
        datos = pd.read_excel('datos/camaras_TyM_208.xlsx')
        datos.index = datos['ubicación']
        buscar = datos.loc[dato,'ip camara']
        return buscar


    def buscar_usuario(self,dato):
        
        datos = pd.read_excel('datos/camaras_TyM_208.xlsx')
        datos.index = datos['ubicación']
        buscar = datos.loc[dato,'usuario']
        return buscar


    def buscar_pass(self,dato):
        
        datos = pd.read_excel('datos/camaras_TyM_208.xlsx')
        datos.index = datos['ubicación']
        buscar = datos.loc[dato,'password']
        return buscar
