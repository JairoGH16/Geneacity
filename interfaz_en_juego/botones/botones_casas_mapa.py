from interfaz_en_juego.botones.boton import Boton

class Botones_casas_mapa(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.casa_asignada:tuple=()
    def accion_clic(self):
            pass
            #interfaz_mapa=Interfaz_durante_mapa(self.screen)
            #interfaz_mapa.crear_interfaz_mapa()