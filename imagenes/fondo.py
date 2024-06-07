import pygame

class Fondo:
    def colocar_fondo(imagen_fondo,screen):
        for x in range(0, 800, 32):
            for y in range(0, 800, 32):
                screen.blit(imagen_fondo, (x, y))