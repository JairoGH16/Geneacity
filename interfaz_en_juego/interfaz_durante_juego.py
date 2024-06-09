import pygame
from escritor_texto import Escritor
from personajes.dibujador_personajes import Dibujador_personajes
from interfaz_en_juego.mensajes_avisos import Mensajes_avisos
from interfaz_en_juego.botones.boton_pausa import Boton_pausa
from interfaz_en_juego.botones.boton_mapa import Boton_mapa

class Interfaz_durante_juego:
    def __init__(self,screen):
        self.screen=screen
        self.escritor=Escritor(self.screen)
        self.barra_personaje=pygame.image.load("imagenes/interfaz/gui_barra_personaje.png")
        self.boton_pausa=Boton_pausa(self.screen,712,794,24,86)
        self.boton_mapa=Boton_mapa(self.screen,612,694,24,86)
        self.dibujador_personaje=Dibujador_personajes(self.screen)
        self.mensajes_avisos=Mensajes_avisos(self.screen)

    def crear_interfaz_juego(self,personaje,personaje_x,personaje_y,lista_posiciones_casas):
        #BARRA DE PERSONAJE
        self.screen.blit(self.barra_personaje, (0, 10))
        self.escritor.escribir(40,134,f"{personaje_x}",18,(255, 255, 255))
        self.escritor.escribir(116,134,f"{personaje_y}",18,(255, 255, 255))
        self.dibujador_personaje._dibujar_un_personaje(personaje,51,51)
        self.escritor.escribir(120,52,f"{personaje["name"][0:17]}",16,(255, 255, 255))
        if len(personaje["name"])>17: #Para cambiarse de reglón si el nombre tiene más de 17 caracteres.
            self.escritor.escribir(120,65,f"-{personaje["name"][17:]}",16,(255, 255, 255))
        if int(personaje["age"])<10:
            self.escritor.escribir(300,35,f"{personaje["age"]}",45,(255, 255, 255))
        else:
            self.escritor.escribir(285,35,f"{personaje["age"]}",45,(255, 255, 255))

        #BOTONES
        #Botón de pausa
        self.boton_pausa.boton_constante()
        self.boton_mapa.boton_constante(lista_posiciones_casas)
        #MANEJAR MENSAJES Y AVISOS
        self.mensajes_avisos.dibujar_mensajes_avisos(personaje_x,personaje_y)