import pygame

class Fondo:
    def __init__(self,screen):
        self.cesped=pygame.image.load("imagenes/escenario/esc_cesped.png")
        self.screen=screen

    def colocar_fondo(self):
        for x in range(0, 800, 32):
            for y in range(0, 800, 32):
                self.screen.blit(self.cesped, (x, y))