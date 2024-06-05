import time
import consultas
import pygame

class Cargador_casas:
    def tecla_presionada(self, key, last_action_time,screen):
        if key not in last_action_time:
            last_action_time[key] = time.time()
            self.cargar_casas(screen)

    def tecla_alzada(self, key, last_action_time):
        if key in last_action_time:
            del last_action_time[key]

    def cargar_casas(self,screen):
        lista_casas=(consultas.Consulta_casas_cercanas.consultar_casas(300,300))
        print(lista_casas)
        for casa in lista_casas:
            self.draw_rectangle(screen, int(casa["x"]), int(casa["y"]))

    def draw_rectangle(self, screen, x, y, width=50, height=50, color=(255, 255, 255)):
        """
        Dibuja un rectángulo en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja el rectángulo.
        - x, y: coordenadas donde se dibujará el rectángulo.
        - width, height: dimensiones del rectángulo.
        - color: color del rectángulo (por defecto es blanco).
        """
        pygame.draw.rect(screen, color, (x, y, width, height))  # Usar tuple para las coordenadas y dimensiones
