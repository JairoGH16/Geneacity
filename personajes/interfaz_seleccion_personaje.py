import pygame
from escritor_texto import Escritor
from personajes.enlistador_seleccion import Enlistador_seleccionador_personajes

class Dibujador_personajes:
    def __init__(self,enlistador:Enlistador_seleccionador_personajes,screen):
        self.enlistadors=enlistador
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
        def dibujar_personajes_disponibles(self,enlistador:Enlistador_seleccionador_personajes):
            lista_personajes=enlistador.lista_habitantes_impresos
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
        def dibujar_personaje_seleccionando(self,mouse_pos,enlistador:Enlistador_seleccionador_personajes):
            escritor=Escritor(self.screen)
            lista_personajes=enlistador.lista_habitantes_impresos
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
                personaje=lista_personajes[indice]
                escritor.escribir(344,555,"NOMBRE",20)
                escritor.escribir(344,568,f"{personaje["name"][0:17]}",25)
                if len(personaje["name"])>17: #Para cambiarse de reglón si el nombre tiene más de 17 caracteres.
                    escritor.escribir(344,588,f"-{personaje["name"][17:]}",25)
                escritor.escribir(400,613,"EDAD",20)
                if int(personaje["age"])<10:
                    escritor.escribir(415,613,f"{personaje["age"]}",60)
                else:
                    escritor.escribir(400,613,f"{personaje["age"]}",60)
                self._dibujar_un_personaje(personaje,253,593)