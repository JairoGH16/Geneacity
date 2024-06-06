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

    def tecla_presionada(self, key, last_action_time,personaje_x,personaje_y):
        if key not in last_action_time:
            last_action_time[key] = time.time()
            self.recargar_casas(personaje_x,personaje_y)

    def tecla_alzada(self, key, last_action_time):
        if key in last_action_time:
            del last_action_time[key]

    def recargar_casas(self,personaje_x,personaje_y):
        try:
            self.lista_casas=(consultas.Consulta_casas_cercanas.consultar_casas(personaje_x,personaje_y))
            print(self.lista_casas)
        except:
            print("No hay casas")

    def dibujar_casas(self,screen,personaje_x,personaje_y):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        centro_x = screen.get_width() / 2
        centro_y = screen.get_height() / 2
        for casa in self.lista_casas:
            casa_x = float(centro_x) + float(casa["x"]) - float(personaje_x)
            casa_y = float(centro_y) + float(casa["y"]) - float(personaje_y)
            screen.blit(self.edificio_ciudad, (casa_x, casa_y))