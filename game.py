import pygame
import time
import arbol.consultas as consultas
from casas.cargador_casas import Cargador_casas
from personajes.personaje import Administrador_personajes
from imagenes.fondo import Fondo
from personajes.control_menu_personaje import Controlador_menu_personaje
from interfaz_en_juego.interfaz_durante_juego import Interfaz_durante_juego
from casas.control_menu_casas import Controlador_menu_casas
from interfaz_en_juego.interfaz_muerte import Interfaz_durante_muerte
from interfaz_en_juego.menu_principal import Menu_principal
from arbol.nodos_arbol import Nodo_persona
from arbol.inicializador_arbol import Inicializador_arbol

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.running = True
        self.last_action_time = {}
        self.lista_posiciones_casas:list["tuple"]=[]
        self.cargador_casas = Cargador_casas()
        self.moviendose=False
        self.fondo_cesped=pygame.image.load("imagenes/escenario/esc_cesped.png")
        self.interfaz_durante_juego=Interfaz_durante_juego(self.screen)
        self.ultima_revision_minuto = time.time()
        self.controlador_menu_casas:Controlador_menu_casas=None
        self.muerte=Interfaz_durante_muerte(self.screen)
        self.menu_principal=Menu_principal(self.screen)
        self.inicializador_arbol:Inicializador_arbol=Inicializador_arbol()
        self.mi_casa_id:int=None

    def juego_principal(self):
        while self.running:
            self.menu_principal.crear_interfaz_menu()
            self.personaje_x:int=15
            self.personaje_y:int=15

            self.controlador_menu_personaje=Controlador_menu_personaje(self.screen,self.personaje_x,self.personaje_y)
            self.personaje=self.controlador_menu_personaje.menu_seleccion_personaje()
            self.vivo=(consultas.Consulta_persona_por_id.consultar_persona(self.personaje["id"]))["alive"]
            print(self.personaje)
            #consultas.Seleccionar_habitante.seleccion_habitante(self.personaje["id"])
            self.nodo_raiz_arbol:Nodo_persona=self.inicializador_arbol.inicializar_arbol(int(self.personaje["id"]))
            self.controlador_menu_casas=Controlador_menu_casas(self.screen,self.nodo_raiz_arbol)

            self.admin_personajes:Administrador_personajes=Administrador_personajes(self.screen,self.personaje["age"],self.personaje["gender"])

            self.admin_personajes.actualizar_personaje(115)
            self.cargador_casas.recargar_casas(self.personaje_x,self.personaje_y,self.lista_posiciones_casas)
            while self.vivo == "Alive":
                keys_pressed = pygame.key.get_pressed()  # Revisar el estado de las teclas fuera de los eventos
                if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                    if self.personaje_y < 100000:
                        self.personaje_y += 15
                if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                    if self.personaje_y >0:
                        self.personaje_y -= 15
                if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                    if self.personaje_x > 0:
                        self.personaje_x -= 15
                if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                    if self.personaje_x < 100000:
                        self.personaje_x += 15
                self.manejo_eventos()
                self.acciones_temporales()
                pygame.time.delay(50)  # Pausa de 100 milisegundos en el bucle para reducir el uso de CPU.
                self.screen.fill((0,0,0))
                Fondo.colocar_fondo(self.fondo_cesped,self.screen)
                if self.moviendose:
                    self.admin_personajes.actualizar_indice_personaje()
                self.cargador_casas.dibujar_casas(self.screen,self.personaje_x,self.personaje_y)
                self.admin_personajes.dibujar_personaje()
                self.interfaz_durante_juego.crear_interfaz_juego(self.personaje,self.personaje_x,self.personaje_y,self.lista_posiciones_casas)
                pygame.display.flip()  # Actualizar la pantalla
            self.muerte.crear_aviso_muerte(self.personaje["name"])
        pygame.quit()

    def manejo_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.moviendose=True
                if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    self.cargador_casas.tecla_presionada(event.key,self.last_action_time,self.personaje_x,self.personaje_y,self.lista_posiciones_casas)
                    self.admin_personajes.actualizar_personaje(event.key)
            elif event.type == pygame.KEYUP:
                keys_pressed = pygame.key.get_pressed()  # Retorna un array de bools para cada tecla
                if not any(keys_pressed):  # `any()` retorna True si al menos una tecla está presionada
                    self.moviendose=False
                if event.key in self.last_action_time:
                    self.cargador_casas.tecla_alzada(event.key,self.last_action_time)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si el botón es el izquierdo
                if event.button == 1:  # 1 es el botón izquierdo del mouse
                    self.clic_en_casa(event.pos)

    def clic_en_casa(self, mouse_pos):
        for rect,casa_id in self.cargador_casas.casa_rects:
            if casa_id != self.mi_casa_id:
                if rect.collidepoint(mouse_pos):
                    lista_casa=(consultas.Consulta_id_personas_casa.consultar_personas_casa(casa_id))  # Imprimir si se clickea sobre una casa
                    self.controlador_menu_casas.abrir_menu_casa(casa_id,lista_casa,self.lista_posiciones_casas,self.personaje,False)
                    return
            else:
                if rect.collidepoint(mouse_pos):
                    lista_casa=(consultas.Consulta_id_personas_casa.consultar_personas_casa(casa_id))  # Imprimir si se clickea sobre una casa
                    self.controlador_menu_casas.abrir_menu_casa(casa_id,lista_casa,self.lista_posiciones_casas,self.personaje,True)
                    return


    def acciones_temporales(self):
        current_time = time.time()
        keys_to_check = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        for key in keys_to_check:
            if key in self.last_action_time and (current_time - self.last_action_time[key]) >= 5:
                self.last_action_time[key] = current_time
                self.cargador_casas.recargar_casas(self.personaje_x,self.personaje_y,self.lista_posiciones_casas)

        tiempo_actual = time.time()  # Obtener el tiempo actual cada vez que el bucle itera
        if tiempo_actual - self.ultima_revision_minuto >= 60:  # Verifica si han pasado 60 segundos
            self.ultima_revision_minuto = tiempo_actual  # Reinicia el contador de tiempo
            self.admin_personajes.actualizar_edad(self.personaje)
            self.vivo=(consultas.Consulta_persona_por_id.consultar_persona(self.personaje["id"]))["alive"]
        

if __name__ == "__main__":
    game = Game()
    game.juego_principal()