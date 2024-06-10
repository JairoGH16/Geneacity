from interfaz_en_juego.botones.boton import Boton
import pygame

class Boton_tener_hijo(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.imagen_normal=pygame.image.load("casas/hijos/gui_tener_hijo1.png")
        self.imagen_marcado=pygame.image.load("casas/hijos/gui_tener_hijo2.png")