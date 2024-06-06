import pygame
import consultas

class Ventana_seleccion_personajes:
    def __init__(self,screen):
        self.screen=screen
        self.imagen_ventana_seleccion_personajes = pygame.image.load("imagenes/interfaz/gui_seleccion_personaje.png")
        self.organizador=Organizador_seleccionador_personajes()
        self.organizador.carga_inicial()
        self.dibujador_personajes_disponibles=Dibujador_personajes_disponibles(self.organizador,self.screen)

    def dibujar_ventana(self, x=0, y=0):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        self.screen.blit(self.imagen_ventana_seleccion_personajes, (x, y))
        self.dibujador_personajes_disponibles.dibujar_personajes_disponibles()

class Organizador_seleccionador_personajes:
    def __init__(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12
        self.lista_habitantes_disponibles:list=None
        self.lista_habitantes_impresos:list=None
    def carga_inicial(self):
        self.lista_habitantes_disponibles:list=consultas.Consulta_habitantes_disponibles.consultar_habitantes()
        self.lista_habitantes_impresos:list=self.lista_habitantes_disponibles[self.primer_habitante_impreso:self.ultimo_habitante_impreso]
        print(self.lista_habitantes_impresos)

class Dibujador_personajes_disponibles:
    def __init__(self,organizador,screen):
        self.organizador:Organizador_seleccionador_personajes=organizador
        self.screen=screen
        self.sprite_bebe=pygame.image.load("personajes/bebe/abajo1.png")
        self.sprite_niño=pygame.image.load("personajes/niño/abajo_derecha1.png")
        self.sprite_niña=pygame.image.load("personajes/niña/abajo_derecha1.png")
        self.sprite_adolescente_hombre=pygame.image.load("personajes/adolescente_hombre/abajo_derecha1.png")
        self.sprite_adolescente_mujer=pygame.image.load("personajes/adolescente_mujer/abajo_derecha1.png")
        self.sprite_adulto_joven=pygame.image.load("personajes/adulto1/abajo_derecha1.png")
        self.sprite_adulta_joven=pygame.image.load("personajes/adulta1/abajo_derecha1.png")
        self.sprite_adulto_normal=pygame.image.load("personajes/adulto2/abajo_derecha1.png")
        self.sprite_adulta_normal=pygame.image.load("personajes/adulta2/abajo_derecha1.png")
        self.sprite_adulto_mayor=pygame.image.load("personajes/adulto_mayor/abajo_derecha1.png")
        self.sprite_adulta_mayor=pygame.image.load("personajes/adulta_mayor/abajo_derecha1.png")

    def dibujar_personajes_disponibles(self):
        lista_personajes=self.organizador.lista_habitantes_impresos
        limite=len(lista_personajes)
        #espacio1:
        if limite>=1:
            self.__dibujar_un_personaje(lista_personajes[0],249,253)
        #espacio2:
        #espacio3:
        #espacio4:
        #espacio5:
        #espacio6:
        #espacio7:
        #espacio8:
        #espacio9:
        #espacio10:
        #espacio11:
        #espacio12:
        pass

    def __dibujar_un_personaje(self,personaje,x,y):
        if personaje["gender"]=="Male":
            if int(personaje["age"])>20:
                self.screen.blit(self.sprite_adulto_joven, (x, y))