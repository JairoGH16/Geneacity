import pygame

class Mensajes_avisos:
    def __init__(self,screen):
        self.screen=screen
        self.texto_limite=pygame.image.load("imagenes/cuadros_texto/limite_terreno.png")

    def dibujar_mensajes_avisos(self,personaje_x,personaje_y):
        
        if personaje_x == 0 or personaje_x >= 100000 or personaje_y == 0 or personaje_y >= 100000:
            self.screen.blit(self.texto_limite, (290, 275))