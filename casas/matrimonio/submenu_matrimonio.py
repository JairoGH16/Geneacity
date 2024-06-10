import pygame
from arbol.consultas import Consulta_persona_por_id
from escritor_texto import Escritor
from casas.matrimonio.submapa_boda import Submapa_boda

class Submenu_matrimonio:
    def __init__(self,screen):
        self.imagen_fondo_menu_matrimonio=pygame.image.load("casas/matrimonio/gui_submenu_matrimonio.png")
        self.screen=screen
        self.escritor=Escritor(self.screen)

    def crear_menu_matrimonio(self,pretendiente,lista_posiciones_casas,personaje_jugador):
        self.submapa_boda=Submapa_boda(self.screen,lista_posiciones_casas)
        en_menu = True
        while en_menu:
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_fondo_menu_matrimonio, (0, 0))

            self.escritor.escribir(370,400,pretendiente["name"],15,(0,0,0))

            pygame.display.flip()
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    x=mouse_pos[0]
                    y=mouse_pos[1]
                    if x>313 and x<450 and y>435 and y<477:
                        if self.submapa_boda.crear_interfaz_mapa(pretendiente,personaje_jugador):
                            return True
                    if x>264 and x<539 and y>493 and y<549:
                        en_menu=False