import pygame
import time
from casas.cargador_casas import Cargador_casas
from personajes.personaje import Administrador_personajes

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.running = True
        self.last_action_time = {}
        self.cargador_casas = Cargador_casas()
        self.admin_personajes=Administrador_personajes(self.screen,17,"Male") #ESTO HAY QUE CONSULTARLO
        self.moviendose=False
        self.personaje_x=300
        self.personaje_y=300

    def run(self):
        self.admin_personajes.actualizar_personaje(115)
        while self.running:

            keys_pressed = pygame.key.get_pressed()  # Revisar el estado de las teclas fuera de los eventos
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                self.personaje_y -= 15
            if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                self.personaje_y += 15
            if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                self.personaje_x -= 15
            if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                self.personaje_x += 15

            self.handle_events()
            self.repeat_actions()
            pygame.time.delay(100)  # Pausa de 100 milisegundos en el bucle para reducir el uso de CPU.
            self.screen.fill((0,0,0))
            if self.moviendose:
                self.admin_personajes.actualizar_indice_personaje()
            self.admin_personajes.dibujar_personaje()
            self.cargador_casas.dibujar_casas(self.screen,self.personaje_x,self.personaje_y)
            pygame.display.flip()  # Actualizar la pantalla
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.moviendose=True
                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    self.cargador_casas.tecla_presionada(event.key,self.last_action_time,self.personaje_x,self.personaje_y)
                    self.admin_personajes.actualizar_personaje(event.key)
            elif event.type == pygame.KEYUP:
                keys_pressed = pygame.key.get_pressed()  # Retorna un array de bools para cada tecla
                if not any(keys_pressed):  # `any()` retorna True si al menos una tecla está presionada
                    self.moviendose=False
                if event.key in self.last_action_time:
                    self.cargador_casas.tecla_alzada(event.key,self.last_action_time)

    def repeat_actions(self):
        current_time = time.time()
        keys_to_check = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        for key in keys_to_check:
            if key in self.last_action_time and (current_time - self.last_action_time[key]) >= 5:
                self.last_action_time[key] = current_time
                self.cargador_casas.recargar_casas(self.personaje_x,self.personaje_y)

if __name__ == "__main__":
    game = Game()
    game.run()