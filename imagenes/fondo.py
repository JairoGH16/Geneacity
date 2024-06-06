import pygame

class Fondo:
    def __init__(self,screen):
        self.imagen_fondo=None
        self.screen=screen

    def colocar_fondo(self):
        for x in range(0, 800, 32):
            for y in range(0, 800, 32):
                self.screen.blit(self.imagen_fondo, (x, y))

class Fondo_cesped(Fondo):
    def __init__(self,screen):
        super().__init__(screen)
        self.imagen_fondo=pygame.image.load("imagenes/escenario/esc_cesped.png")