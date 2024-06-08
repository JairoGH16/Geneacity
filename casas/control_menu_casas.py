import pygame
from personajes.enlistador_seleccion import Enlistador_seleccionador_personajes
from personajes.interfaz_seleccion_personaje import Dibujador_personajes_disponibles,Dibujador_personaje_seleccionando

class Controlador_menu_personaje:
    def __init__(self,screen,personaje_x:int,personaje_y:int):
        self.screen=screen
        self.enlistador=Enlistador_seleccionador_personajes()
        self.enlistador.consultar_enlistamiento()
        self.dibujador_disponibles=Dibujador_personajes_disponibles(self.screen,self.enlistador)
        self.dibujador_seleccionando=Dibujador_personaje_seleccionando(self.screen,self.enlistador)
        self.personaje_x:int=personaje_x
        self.personaje_y:int=personaje_y
        self.imagen_menu=pygame.image.load("imagenes/interfaz/gui_seleccion_personaje.png")
        self.mouse_pos=(0,0)
    def menu_seleccion_personaje(self):
        self.seleccionando_personaje=True
        while self.seleccionando_personaje:
            self.mouse_pos = pygame.mouse.get_pos()
            pygame.time.delay(100)
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_menu, (0, 0))
            self.dibujador_disponibles.dibujar_personajes_disponibles(self.enlistador)
            self.dibujador_seleccionando.dibujar_personaje_seleccionando(self.mouse_pos,self.enlistador)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.enlistador.consultar_enlistamiento()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.enlistador.avanzar_pagina()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.enlistador.retroceder_pagina()
                if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si el botón es el izquierdo
                    if event.button == 1:  # 1 es el botón izquierdo del mouse
                        tupla_seleccion = self.seleccionar_personaje()
                        if tupla_seleccion[0] == True:
                            return tupla_seleccion[1]

    def seleccionar_personaje(self):
        lista_personajes=self.enlistador.lista_habitantes_impresos
        x=self.mouse_pos[0]
        y=self.mouse_pos[1]
        indice=13 #para que no imprima a nadie si el mouse no está sobre nadie.
        if y>241 and y<317:
            if x>221 and x<306:
                indice=0
            if x>309 and x<394:
                indice=1
            if x>397 and x<482:
                indice=2
            if x>485 and x<569:
                indice=3
        if y>329 and y<405:
            if x>221 and x<306:
                indice=4
            if x>309 and x<394:
                indice=5
            if x>397 and x<482:
                indice=6
            if x>485 and x<569:
                indice=7
        if y>414 and y<491:
            if x>221 and x<306:
                indice=8
            if x>309 and x<394:
                indice=9
            if x>397 and x<482:
                indice=10
            if x>485 and x<569:
                indice=11
        if len(lista_personajes)-1>=indice:
            self.seleccionando_personaje=False
            return(True,(lista_personajes[indice]))
        return (False,None)