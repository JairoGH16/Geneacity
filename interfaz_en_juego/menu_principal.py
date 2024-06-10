import pygame
from interfaz_en_juego.botones.botones_menu_pausa import Boton_salir
from interfaz_en_juego.botones.boton import Boton
class Menu_principal:
    """Menú inicial del juego
    """
    def __init__(self,screen):
        self.screen=screen
        self.imagen_menu_principal=pygame.image.load("imagenes/interfaz/menu_principal/gui_menu_principal.png")
        self.boton_nueva_partida=Boton(self.screen,300,511,340,398)
        self.boton_nueva_partida.imagen_normal=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_nuevo1.png")
        self.boton_nueva_partida.imagen_marcado=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_nuevo2.png")
        self.boton_cargar_partida=Boton(self.screen,300,511,430,488)
        self.boton_cargar_partida.imagen_normal=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_cargar1.png")
        self.boton_cargar_partida.imagen_marcado=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_cargar2.png")
        self.boton_historial=Boton(self.screen,300,511,530,588)
        self.boton_historial.imagen_normal=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_historial1.png")
        self.boton_historial.imagen_marcado=pygame.image.load("imagenes/interfaz/menu_principal/gui_boton_historial2.png")
        self.boton_salir=Boton_salir(self.screen,300,511,630,688)

    def crear_interfaz_menu(self):
        """Crea el menú inicial
        """
        en_menu=True
        while en_menu:
            #DIBUJAR IMAGEN
            self.screen.blit(self.imagen_menu_principal,(0,0))
            self.boton_nueva_partida.boton_constante()
            self.boton_cargar_partida.boton_constante()
            self.boton_historial.boton_constante()
            self.boton_salir.boton_constante()
            pygame.display.flip()
            pygame.time.delay(50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_menu = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_salir.accion_clic():
                        pygame.quit()  # Suponiendo que es_clic es un método de la clase Boton
                    elif self.boton_nueva_partida.accion_clic():
                        en_menu = False
                    elif self.boton_cargar_partida.accion_clic():
                        pass
                    elif self.boton_historial.accion_clic():
                        pass