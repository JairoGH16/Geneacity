import pygame
from casas.interfaz_menu_casas import Dibujador_personajes_casas,Dibujador_personaje_interactuando
from consultas import Consulta_persona_por_id
from interfaz_en_juego.botones.botones_menu_pausa import Boton_volver

class Controlador_menu_casas:
    def __init__(self,screen):
        self.screen=screen
        self.imagen_menu_casas=pygame.image.load("imagenes/interfaz/gui_menu_casa.png")
        self.mouse_pos=(0,0)
        self.dibujador_personajes_lista=Dibujador_personajes_casas(self.screen)
        self.dibujador_personaje_interactuando=Dibujador_personaje_interactuando(self.screen)
        self.boton_volver=Boton_volver(self.screen,292,503,710,768)
    def abrir_menu_casa(self,id_casa,lista_personajes):
        nueva_lista=[]
        for persona in lista_personajes:
                nueva_lista.append(Consulta_persona_por_id.consultar_persona(persona["id"]))
        print(nueva_lista)
        print(lista_personajes)
        en_menu=True
        while en_menu:
            self.screen.blit(self.imagen_menu_casas, (0, 0))

            self.dibujador_personajes_lista.dibujar_personajes_casa(id_casa,nueva_lista)
            self.dibujador_personaje_interactuando.dibujar_personaje_interactuando(nueva_lista)
            self.boton_volver.boton_constante()
            pygame.display.flip()
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_menu = False  # Suponiendo que es_clic es un método de la clase Boton