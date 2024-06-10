import pygame
import time
import arbol.consultas as consultas

class Cargador_casas:
    def __init__(self):
        # Inicializar Pygame
        self.lista_casas:list["dir"]=[]
        pygame.init()
        # Pre-cargar la imagen para mejorar el rendimiento
        self.edificio_ciudad = pygame.image.load("casas/ciudad.png")
        self.casa_condominio = pygame.image.load("casas/condominio.png")
        self.casa_madera = pygame.image.load("casas/madera.png")

    def tecla_presionada(self, key, last_action_time,personaje_x,personaje_y,lista_posiciones_casas:list):
        if key not in last_action_time:
            last_action_time[key] = time.time()
            self.recargar_casas(personaje_x,personaje_y,lista_posiciones_casas)

    def tecla_alzada(self, key, last_action_time):
        if key in last_action_time:
            del last_action_time[key]

    def recargar_casas(self,personaje_x,personaje_y,lista_posiciones_casas:list):
        try:
            self.lista_casas=(consultas.Consulta_casas_cercanas.consultar_casas(personaje_x,personaje_y))
            #print(self.lista_casas)
            for casa in self.lista_casas:
                x_casa=int(casa["x"])
                y_casa=int(casa["y"])
                if (x_casa,y_casa) not in lista_posiciones_casas:
                    lista_posiciones_casas.append((x_casa,y_casa))
                    print(lista_posiciones_casas)
        except:
            print("No hay casas")

    def dibujar_casas(self, screen, personaje_x, personaje_y):
        centro_x = screen.get_width() / 2
        centro_y = screen.get_height() / 2
        self.casa_rects = []  # Lista para almacenar los rectángulos de las casas
        for casa in self.lista_casas:
            casa_x = float(centro_x) + float(casa["x"]) - float(personaje_x)
            casa_y = float(centro_y) - float(casa["y"]) + float(personaje_y)
            if personaje_y < 4000:
                imagen_casa = self.casa_condominio
            elif personaje_x < 5000:
                imagen_casa = self.casa_madera
            elif personaje_x >= 5000:
                imagen_casa = self.edificio_ciudad
            rect = imagen_casa.get_rect(topleft=(casa_x, casa_y))
            screen.blit(imagen_casa, rect)
            self.casa_rects.append((rect,casa["id"]))  # Guardar rectángulo y id de la casa