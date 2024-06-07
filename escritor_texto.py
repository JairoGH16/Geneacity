import pygame
import sys

class Escritor:
    def __init__(self,screen):
        self.screen=screen
    def escribir(self,x:int,y:int,texto:str,tamaño:int):
        # Cargar la fuente "Dubai" si está disponible en el sistema
        try:
            fuente = pygame.font.SysFont('Dubai Medium', tamaño)  # Ajusta el tamaño según necesites
        except:
            print("Fuente no disponible.")
            sys.exit()
        # Crear un texto
        texto_imprimir = fuente.render(texto, True, (0, 0, 0))
        # Blit text
        self.screen.blit(texto_imprimir, (x, y))