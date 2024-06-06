import pygame
import arbol.consultas as consultas

class Ventana_seleccion_personajes:
    def __init__(self,screen,mouse_pos):
        self.mouse_pos=mouse_pos
        self.screen=screen
        self.imagen_ventana_seleccion_personajes = pygame.image.load("imagenes/interfaz/gui_seleccion_personaje.png")
        self.organizador:Organizador_seleccionador_personajes=Organizador_seleccionador_personajes()
        self.organizador.carga_inicial()
        self.dibujador_personajes_disponibles:Dibujador_personajes_disponibles=Dibujador_personajes_disponibles(self.organizador,self.screen)
        self.dibujador_personaje_seleccionando:Dibujador_personaje_seleccionando=Dibujador_personaje_seleccionando(self.organizador,self.screen)

    def dibujar_ventana(self, x=0, y=0):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        self.screen.blit(self.imagen_ventana_seleccion_personajes, (x, y))
        self.dibujador_personajes_disponibles.dibujar_personajes_disponibles()
        self.dibujador_personaje_seleccionando.dibujar_personaje_seleccionando(self.mouse_pos)

class Organizador_seleccionador_personajes:
    def __init__(self):
        self.primer_habitante_impreso:int=0
        self.ultimo_habitante_impreso:int=12
        self.lista_habitantes_disponibles:list=None
        self.lista_habitantes_impresos:list=None
    def carga_inicial(self):
        self.lista_habitantes_disponibles:list=consultas.Consulta_habitantes_disponibles.consultar_habitantes()
        self.lista_habitantes_impresos:list=[]
        for personaje in self.lista_habitantes_disponibles[self.primer_habitante_impreso:self.ultimo_habitante_impreso]:
            if int(personaje["age"])>=0: #Validar que la edad sea valida.
                self.lista_habitantes_impresos.append(personaje)
        print(self.lista_habitantes_impresos)

class Dibujador_personajes:
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

    def _dibujar_un_personaje(self,personaje,x,y):
        if int(personaje["age"])<2:
                self.screen.blit(self.sprite_bebe, (x, y))
        elif personaje["gender"]=="Male":
            if int(personaje["age"])>=2 and int(personaje["age"])<12:
                self.screen.blit(self.sprite_niño, (x, y))
            elif int(personaje["age"])>=12 and int(personaje["age"])<20:
                self.screen.blit(self.sprite_adolescente_hombre, (x, y))
            elif int(personaje["age"])>=20 and int(personaje["age"])<40:
                self.screen.blit(self.sprite_adulto_joven, (x, y))
            elif int(personaje["age"])>=40 and int(personaje["age"])<65:
                self.screen.blit(self.sprite_adulto_normal, (x, y))
            elif int(personaje["age"])>=65:
                self.screen.blit(self.sprite_adulto_mayor, (x, y))
        elif personaje["gender"]=="Female":
            if int(personaje["age"])>=2 and int(personaje["age"])<12:
                self.screen.blit(self.sprite_niña, (x, y))
            elif int(personaje["age"])>=12 and int(personaje["age"])<20:
                self.screen.blit(self.sprite_adolescente_mujer, (x, y))
            elif int(personaje["age"])>=20 and int(personaje["age"])<40:
                self.screen.blit(self.sprite_adulta_joven, (x, y))
            elif int(personaje["age"])>=40 and int(personaje["age"])<65:
                self.screen.blit(self.sprite_adulta_normal, (x, y))
            elif int(personaje["age"])>=65:
                self.screen.blit(self.sprite_adulta_mayor, (x, y))

class Dibujador_personajes_disponibles(Dibujador_personajes):
        def dibujar_personajes_disponibles(self):
            lista_personajes=self.organizador.lista_habitantes_impresos
            limite=len(lista_personajes)
        #espacio1:
            if limite>=1:
                self._dibujar_un_personaje(lista_personajes[0],249,253)
            #espacio2:
            if limite>=2:
                self._dibujar_un_personaje(lista_personajes[1],337,253)
            #espacio3:
            if limite>=3:
                self._dibujar_un_personaje(lista_personajes[2],425,253)
            #espacio4:
            if limite>=4:
                self._dibujar_un_personaje(lista_personajes[3],513,253)
            #espacio5:
            if limite>=5:
                self._dibujar_un_personaje(lista_personajes[4],249,340)
            #espacio6:
            if limite>=6:
                self._dibujar_un_personaje(lista_personajes[5],337,340)
            #espacio7:
            if limite>=7:
                self._dibujar_un_personaje(lista_personajes[6],425,340)
            #espacio8:
            if limite>=8:
                self._dibujar_un_personaje(lista_personajes[7],513,340)
            #espacio9:
            if limite>=9:
                self._dibujar_un_personaje(lista_personajes[8],249,427)
            #espacio10:
            if limite>=10:
                self._dibujar_un_personaje(lista_personajes[9],337,427)
            #espacio11:
            if limite>=11:
                self._dibujar_un_personaje(lista_personajes[10],425,427)
            #espacio12:
            if limite>=12:
                self._dibujar_un_personaje(lista_personajes[11],513,427)

class Dibujador_personaje_seleccionando(Dibujador_personajes):
        def dibujar_personaje_seleccionando(self,mouse_pos):
            lista_personajes=self.organizador.lista_habitantes_impresos
            x=mouse_pos[0]
            y=mouse_pos[1]
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
                self._dibujar_un_personaje(lista_personajes[indice],253,593)