import pygame
from escritor_texto import Escritor

class Interfaz_durante_muerte:
    def __init__(self,screen):
        self.screen=screen
        self.aviso_muerte=pygame.image.load("imagenes/cuadros_texto/aviso_muerte.png")
        self.escritor=Escritor(self.screen)

    def crear_aviso_muerte(self,nombre:str):
        en_muerte=True
        while en_muerte:
            #DIBUJAR IMAGEN
            self.screen.blit(self.aviso_muerte,(0,0))
            self.escritor.escribir(72,91,nombre,40,(255,255,255))
            pygame.display.flip()
            pygame.time.delay(50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_muerte = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        en_muerte = False