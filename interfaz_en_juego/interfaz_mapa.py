import pygame
from interfaz_en_juego.botones.botones_menu_pausa import Boton_volver
from interfaz_en_juego.botones.botones_casas_mapa import Botones_casas_mapa
class Interfaz_durante_mapa:
    def __init__(self,screen,lista_posiciones_casas):
        self.screen=screen
        self.lista_posiciones_casas:list["tuple"]=lista_posiciones_casas
        self.imagen_fondo_mapa=pygame.image.load("imagenes/interfaz/mapa/gui_fondo_mapa.png")
        self.imagen_cubierta_mapa=pygame.image.load("imagenes/interfaz/mapa/gui_cubierta_mapa.png")
        self.boton_casa_imagen_normal=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa1.png")
        self.boton_casa_imagen_marcado=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa2.png")
        self.boton_volver=Boton_volver(self.screen,300,511,20,78)

    def crear_interfaz_mapa(self):
        self.posicion_mapa_x=0
        self.posicion_mapa_y=0

        self.lista_botones_casas:list["Botones_casas_mapa"]=[]
        for casa in self.lista_posiciones_casas:
            x_boton=(casa[0]/16) + 115
            y_boton= -(casa[1]/16) + 553
            self.lista_botones_casas.append(Botones_casas_mapa(self.screen,x_boton,x_boton+6,y_boton,y_boton+6))
        en_mapa=True
        while en_mapa:
            #DIBUJAR IMAGEN
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_fondo_mapa,(0,0))

            for boton_casa in self.lista_botones_casas:
                self.screen.blit(self.boton_casa_imagen_normal,(boton_casa.x_inicial,boton_casa.y_inicial))

            self.screen.blit(self.imagen_cubierta_mapa,(0,0))
            self.boton_volver.boton_constante()
            pygame.display.flip()
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_mapa = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_mapa = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.posicion_mapa_x>0:
                            for boton_casa in self.lista_botones_casas:
                                boton_casa.x_inicial -= 200
                            self.posicion_mapa_x -= 200
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if self.posicion_mapa_x<6000:
                            for boton_casa in self.lista_botones_casas:
                                boton_casa.x_inicial += 200
                            self.posicion_mapa_x += 200
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.posicion_mapa_y>0:
                            for boton_casa in self.lista_botones_casas:
                                boton_casa.y_inicial += 200
                            self.posicion_mapa_y -= 200 #Manejo normal del plano cartesiano
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.posicion_mapa_y<6000:
                            for boton_casa in self.lista_botones_casas:
                                boton_casa.y_inicial -= 200
                            self.posicion_mapa_y += 200 #Manejo normal del plano cartesiano
                