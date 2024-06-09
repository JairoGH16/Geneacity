import pygame
from interfaz_en_juego.botones.boton import Boton

class Boton_salir(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.imagen_normal=pygame.image.load("imagenes/interfaz/gui_boton_salir1.png")
        self.imagen_marcado=pygame.image.load("imagenes/interfaz/gui_boton_salir2.png")
class Boton_volver(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.regresar=False
        self.imagen_normal=pygame.image.load("imagenes/interfaz/gui_boton_volver1.png")
        self.imagen_marcado=pygame.image.load("imagenes/interfaz/gui_boton_volver2.png")