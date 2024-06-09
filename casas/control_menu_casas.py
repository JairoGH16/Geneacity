import pygame
from casas.interfaz_menu_casas import Dibujador_personajes_casas,Dibujador_personaje_interactuando,Dibujar_avisos_casas
from consultas import Consulta_persona_por_id
from interfaz_en_juego.botones.botones_menu_pausa import Boton_volver
from casas.agregar_personas_casa_arbol import Insertador_casas_arbol
import time

class Controlador_menu_casas:
    def __init__(self,screen,nodo_raiz):
        self.screen=screen
        self.nodo_raiz=nodo_raiz
        self.imagen_menu_casas=pygame.image.load("imagenes/interfaz/gui_menu_casa.png")
        self.mouse_pos=(0,0)
        self.dibujador_personajes_lista=Dibujador_personajes_casas(self.screen)
        self.dibujador_personaje_interactuando=Dibujador_personaje_interactuando(self.screen)
        self.dibujador_avisos=Dibujar_avisos_casas(self.screen)
        self.boton_volver=Boton_volver(self.screen,292,503,710,768)
        self.insertador_arbol=Insertador_casas_arbol(self.screen)
    def abrir_menu_casa(self,id_casa,lista_personajes):
        nueva_lista=[]
        for persona in lista_personajes:
                nueva_lista.append(Consulta_persona_por_id.consultar_persona(persona["id"]))
        print(nueva_lista)
        print(lista_personajes)
        self.lista_nombres_agregados=(self.insertador_arbol.insertar_grupo_personas(nueva_lista,self.nodo_raiz)) #Inserta los personajes en el árboles y retorna a quienes se insertó.

        self.inicio_temporizador_avisos=time.time()
        en_menu=True
        while en_menu:
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_menu_casas, (0, 0))

            self.dibujador_personajes_lista.dibujar_personajes_casa(id_casa,nueva_lista)
            self.dibujador_personaje_interactuando.dibujar_personaje_interactuando(nueva_lista)
            self.boton_volver.boton_constante()
            self.dibujar_aviso_con_tiempo()

            pygame.display.flip()
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_menu = False  # Suponiendo que es_clic es un método de la clase Boton

    def dibujar_aviso_con_tiempo(self):
        tiempo_actual = time.time()  # Obtener el tiempo actual cada vez que el bucle itera
        if len(self.lista_nombres_agregados)==0:
                if tiempo_actual - self.inicio_temporizador_avisos <= 2:  # Verifica si han pasado 8 segundos
                    self.dibujador_avisos.dibujar_aviso_rojo()
        else:
            if tiempo_actual - self.inicio_temporizador_avisos <= 7:
                self.dibujador_avisos.dibujar_aviso_verde(self.lista_nombres_agregados)