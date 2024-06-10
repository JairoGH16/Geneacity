import pygame
import sys

class Escritor:
    """escribe textos con fuente "Dubai"
    """
    def __init__(self,screen):
        self.screen=screen
    def escribir(self,x:int,y:int,texto:str,tamaño:int,color):
        # Cargar la fuente "Dubai" si está disponible en el sistema
        try:
            fuente = pygame.font.SysFont('Dubai Medium', tamaño)  # Ajusta el tamaño según necesites
        except:
            print("Fuente no disponible.")
            sys.exit()
        # Crear un texto
        texto_imprimir = fuente.render(texto, True, color)
        # Blit text
        self.screen.blit(texto_imprimir, (x, y))