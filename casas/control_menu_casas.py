import pygame
from casas.interfaz_menu_casas import Dibujador_personajes_casas,Dibujador_personaje_interactuando,Dibujar_avisos_casas
from arbol.consultas import Consulta_persona_por_id,Crear_habitante
from interfaz_en_juego.botones.botones_menu_pausa import Boton_volver
from casas.agregar_personas_casa_arbol import Insertador_casas_arbol
import time
from casas.matrimonio.submenu_matrimonio import Submenu_matrimonio
from casas.hijos.boton_tener_hijo import Boton_tener_hijo
from casas.hijos.boton_tener_hija import Boton_tener_hija
from casas.hijos.nombrar_hijo import Nombrar_hijo

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
        self.submenu_matrimonio=Submenu_matrimonio(self.screen)
        self.boton_hijo=Boton_tener_hijo(self.screen,240,398,50,94)
        self.boton_hija=Boton_tener_hija(self.screen,40,198,50,94)
        self.nombrador_hijo=Nombrar_hijo(self.screen)

    def abrir_menu_casa(self,id_casa,lista_personajes,lista_posiciones_casas,personaje_jugador,propia:bool): #lo de propia indica sí es mi casa, si es True es mi casa
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

            #if propia==True:
            self.boton_hijo.boton_constante()
            self.boton_hija.boton_constante()

            self.boton_volver.boton_constante()
            self.dibujar_aviso_con_tiempo()

            pygame.display.flip()
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_menu = False  # Suponiendo que es_clic es un método de la clase Boton
                    elif event.button == 1:  # 1 es el botón izquierdo del mouse
                        if self.botones_menu_casas(lista_personajes,lista_posiciones_casas,personaje_jugador)==True:
                            return True

    def dibujar_aviso_con_tiempo(self):
        tiempo_actual = time.time()  # Obtener el tiempo actual cada vez que el bucle itera
        if len(self.lista_nombres_agregados)==0:
                if tiempo_actual - self.inicio_temporizador_avisos <= 2:  # Verifica si han pasado 8 segundos
                    self.dibujador_avisos.dibujar_aviso_rojo()
        else:
            if tiempo_actual - self.inicio_temporizador_avisos <= 7:
                self.dibujador_avisos.dibujar_aviso_verde(self.lista_nombres_agregados)

    def botones_menu_casas(self,lista_personajes,lista_posiciones_casas,personaje_jugador):
        mouse_pos=pygame.mouse.get_pos()
        x=mouse_pos[0]
        y=mouse_pos[1]
        if x>240 and x< 398 and y> 50 and y< 97:
                nombre_hijo=self.nombrador_hijo.nombrar_hijo()
                print(nombre_hijo)
                if len(nombre_hijo)>=1:
                    Crear_habitante.nacimiento(nombre_hijo,int(personaje_jugador["id"]),"Male",0)
        elif x>40 and x< 198 and y> 50 and y< 97:
                nombre_hija=self.nombrador_hijo.nombrar_hijo()
                print(nombre_hija)
                if len(nombre_hija)>=1:
                    Crear_habitante.nacimiento(nombre_hija,int(personaje_jugador["id"]),"Female",0)
        elif y>241 and y<317:
            if x>221 and x<306:
                    indice=0
            if x>309 and x<394:
                    indice=1
            if x>397 and x<482:
                    indice=2
            if x>485 and x<569:
                    indice=3
        elif y>329 and y<405:
            if x>221 and x<306:
                    indice=4
            if x>309 and x<394:
                    indice=5
            if x>397 and x<482:
                    indice=6
            if x>485 and x<569:
                    indice=7
        try:
            if len(lista_personajes)-1>=indice:
                if self.submenu_matrimonio.crear_menu_matrimonio(lista_personajes[indice],lista_posiciones_casas,personaje_jugador):
                    return True
        except:
            pass