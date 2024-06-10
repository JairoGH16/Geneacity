import pygame
from interfaz_en_juego.botones.botones_menu_pausa import Boton_volver
from interfaz_en_juego.botones.botones_casas_mapa import Botones_casas_mapa
from escritor_texto import Escritor
from arbol.consultas import Casar_habitantes

from interfaz_en_juego.interfaz_mapa import Interfaz_durante_mapa

class Submapa_boda(Interfaz_durante_mapa):
    def __init__(self,screen,lista_posiciones_casas):
        super().__init__(screen,lista_posiciones_casas)

    def crear_interfaz_mapa(self,pretendiente,personaje_jugador):
        self.imagen_fondo_mapa=pygame.image.load("imagenes/interfaz/mapa/gui_fondo_mapa.png")
        self.imagen_cubierta_mapa=pygame.image.load("imagenes/interfaz/mapa/gui_cubierta_mapa.png")
        self.boton_casa_imagen_normal=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa1.png")
        self.boton_casa_imagen_marcado=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa2.png")
        self.boton_volver=Boton_volver(self.screen,300,511,20,78)
        self.escritor=Escritor(self.screen)

        self.posicion_mapa_x=0
        self.posicion_mapa_y=0

        self.lista_botones_casas:list["Botones_casas_mapa"]=[]
        for casa in self.lista_posiciones_casas:
            x_boton=(casa[0]/16) + 115
            y_boton= -(casa[1]/16) + 553
            boton=Botones_casas_mapa(self.screen,x_boton,x_boton+6,y_boton,y_boton+6)
            boton.casa_asignada=(int(casa[0]),int(casa[1]))
            self.lista_botones_casas.append(boton)
        en_mapa=True
        while en_mapa:

            keys_pressed = pygame.key.get_pressed()  # Revisar el estado de las teclas fuera de los eventos
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                    if self.posicion_mapa_y<6000:
                        for boton_casa in self.lista_botones_casas:
                            boton_casa.y_inicial += 200
                        self.posicion_mapa_y += 200 #Manejo normal del plano cartesiano
            if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                    if self.posicion_mapa_y>0:
                        for boton_casa in self.lista_botones_casas:
                            boton_casa.y_inicial -= 200
                        self.posicion_mapa_y -= 200 #Manejo normal del plano cartesiano
            if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                    if self.posicion_mapa_x>0:
                        for boton_casa in self.lista_botones_casas:
                            boton_casa.x_inicial += 200
                        self.posicion_mapa_x -= 200
            if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                    if self.posicion_mapa_x<6000:
                        for boton_casa in self.lista_botones_casas:
                            boton_casa.x_inicial -= 200
                        self.posicion_mapa_x += 200

            #DIBUJAR IMAGEN
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_fondo_mapa,(0,0))

            coordenadas:tuple=None
            for boton_casa in self.lista_botones_casas:
                if boton_casa.boton_constante():
                    coordenadas = boton_casa.casa_asignada
                     
            self.screen.blit(self.imagen_cubierta_mapa,(0,0))
            if coordenadas:
                 self.escritor.escribir(210,715,f"X de esta casa: {coordenadas[0]}   Y de esta casa: {coordenadas[1]}",20,(0,0,0))
            self.boton_volver.boton_constante()

            #AREA ORIGINAL
            mouse_pos=pygame.mouse.get_pos()
            mouse_x=mouse_pos[0]
            mouse_y=mouse_pos[1]
            posicion_x_escogiendo= (mouse_x-115)*16
            posicion_y_escogiendo= -((mouse_y-553)*16)
            if mouse_x>=112 and mouse_x<696 and mouse_y>=68 and mouse_y<562:
                self.escritor.escribir(210,690,f"X a seleccionar: {posicion_x_escogiendo+self.posicion_mapa_x}   Y a seleccionar: {posicion_y_escogiendo+self.posicion_mapa_y}",20,(0,0,0))

            pygame.display.flip()
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_mapa = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_mapa = False
                    elif event.button == 1:  # 1 es el botón izquierdo del mouse
                        if mouse_x>=112 and mouse_x<696 and mouse_y>=68 and mouse_y<562:
                            print(Casar_habitantes.unir_pareja(int(pretendiente["id"]),int(personaje_jugador["id"]),posicion_x_escogiendo,posicion_y_escogiendo))
                            return True