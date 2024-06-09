import pygame
from interfaz_en_juego.botones.boton import Boton
from interfaz_en_juego.interfaz_pausa import Interfaz_durante_pausa

class Boton_pausa(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.imagen_normal=pygame.image.load("imagenes/interfaz/gui_boton_pausa1.png")
        self.imagen_marcado=pygame.image.load("imagenes/interfaz/gui_boton_pausa2.png")
    def accion_clic(self):
            interfaz_pausa=Interfaz_durante_pausa(self.screen)
            interfaz_pausa.crear_interfaz_pausa()