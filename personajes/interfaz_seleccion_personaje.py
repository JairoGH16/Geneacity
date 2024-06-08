from personajes.dibujador_personajes import Dibujador_personajes
from escritor_texto import Escritor
from personajes.enlistador_seleccion import Enlistador_seleccionador_personajes

class Dibujador_personajes_seleccionador(Dibujador_personajes):
    def __init__(self,screen,enlistador):
        super().__init__(screen)
        self.enlistador=enlistador

class Dibujador_personajes_disponibles(Dibujador_personajes_seleccionador):
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

class Dibujador_personaje_seleccionando(Dibujador_personajes_seleccionador):
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