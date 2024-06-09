from personajes.dibujador_personajes import Dibujador_personajes
from escritor_texto import Escritor
import pygame

class Dibujador_personajes_casas(Dibujador_personajes):
        def dibujar_personajes_casa(self,id_casa,lista_personajes):
            limite=len(lista_personajes)
            escritor=Escritor(self.screen)
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
            escritor.escribir(600,140,f"ID: {id_casa}",18,(0, 0, 0))

class Dibujador_personaje_interactuando(Dibujador_personajes):
        def dibujar_personaje_interactuando(self,lista_personajes):
            escritor=Escritor(self.screen)
            mouse_pos = pygame.mouse.get_pos()
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

            if len(lista_personajes)-1>=indice:
                personaje=lista_personajes[indice]
                escritor.escribir(344,555,"NOMBRE",20,(0, 0, 0))
                escritor.escribir(344,568,f"{personaje["name"][0:17]}",25,(0, 0, 0))
                if len(personaje["name"])>17: #Para cambiarse de reglón si el nombre tiene más de 17 caracteres.
                    escritor.escribir(344,588,f"-{personaje["name"][17:]}",25,(0, 0, 0))
                escritor.escribir(400,613,"EDAD",20,(0, 0, 0))
                if int(personaje["age"])<10:
                    escritor.escribir(415,613,f"{personaje["age"]}",60,(0, 0, 0))
                else:
                    escritor.escribir(400,613,f"{personaje["age"]}",60,(0, 0, 0))
                self._dibujar_un_personaje(personaje,253,593)