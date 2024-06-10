import pygame
from interfaz_en_juego.botones.boton import Boton
from interfaz_en_juego.interfaz_mapa import Interfaz_durante_mapa
import arbol.arbol_genealogico as arbol_genealogico

class Boton_arbol():
    def __init__(self,screen):
        self.screen=screen
        self.x_inicial=400
        self.x_final=433
        self.y_inicial=30
        self.y_final=63
        self.imagen_normal=pygame.image.load("imagenes/iconos/ico_arbol.png")
        self.imagen_marcado=pygame.image.load("imagenes/iconos/ico_arbol.png")

    def boton_constante(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >= self.x_inicial and mouse_pos[0]<= self.x_final: #x
            if mouse_pos[1] >= self.y_inicial and mouse_pos[1]<= self.y_final: #y
                self.screen.blit(self.imagen_marcado, (self.x_inicial,self.y_inicial))
                self.marcado=True
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si el botón es el izquierdo
                        if event.button == 1:  # 1 es el botón izquierdo del mouse
                            self.accion_clic()
            else:
                self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
                self.marcado=False
        else:
            self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
            self.marcado=False

    def accion_clic(self):
            arbol_genealogico.arbol_grafico()