import pygame
import time
import consultas

class Cargador_casas:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        self.lista_casas=[]
        # Pre-cargar la imagen para mejorar el rendimiento
        self.edificio_ciudad = pygame.image.load('casas/ciudad.png')

    def tecla_presionada(self, key, last_action_time, screen):
        if key not in last_action_time:
            last_action_time[key] = time.time()
            self.cargar_casas()

    def tecla_alzada(self, key, last_action_time):
        if key in last_action_time:
            del last_action_time[key]

    def cargar_casas(self):
        self.lista_casas=(consultas.Consulta_casas_cercanas.consultar_casas(300, 300))
        print(self.lista_casas)

    def dibujar_casas(self,screen):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        for casa in self.lista_casas: # Dibuja la imagen de cada casa
            screen.blit(self.edificio_ciudad, (int(casa["x"]), int(casa["y"])))