import pygame
from escritor_texto import Escritor
import sys

class Tener_hijo:
    def __init__(self, screen):
        self.screen = screen
        self.imagen_fondo=pygame.image.load("imagenes/interfaz/gui_nombrar_hijo.png")
        self.escritor=Escritor(self.screen)

    def nombrar_hijo(self):
        pygame.display.set_caption("Nombrar hijo")

        nombre_hijo = ""
        running = True
        while running:
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_fondo, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nombre_hijo = nombre_hijo[:-1]
                    elif event.key == pygame.K_RETURN:
                        return(nombre_hijo)
                    else:
                        if len(nombre_hijo)<25:
                            nombre_hijo += event.unicode

            self.escritor.escribir(270,340,nombre_hijo,25,(255,255,255))
            pygame.display.flip()

        pygame.quit()
