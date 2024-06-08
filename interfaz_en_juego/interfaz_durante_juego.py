import pygame
from escritor_texto import Escritor
from personajes.dibujador_personajes import Dibujador_personajes

class Interfaz_durante_juego:
    def __init__(self,screen):
        self.screen=screen
        self.escritor=Escritor(self.screen)
        self.barra_personaje=pygame.image.load("imagenes/interfaz/gui_barra_personaje.png")
        self.texto_limite=pygame.image.load("imagenes/cuadros_texto/limite_terreno.png")
        self.dibujador_personaje=Dibujador_personajes(self.screen)

    def dibujar_interfaz_juego(self,personaje,personaje_x,personaje_y):
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
        
        if personaje_x == 0 or personaje_x == 10000 or personaje_y == 0 or personaje_y == 10000:
            self.screen.blit(self.texto_limite, (290, 275))