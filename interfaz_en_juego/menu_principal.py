import pygame
from interfaz_en_juego.botones.botones_menu_pausa import Boton_salir,Boton_volver
class Menu_principal:
    def __init__(self,screen):
        self.screen=screen
        self.imagen_menu_principal=pygame.image.load("imagenes/interfaz/menu_principal/gui_menu_principal.png")
        self.boton_salir=Boton_salir(self.screen,300,511,380,438)
        self.boton_volver=Boton_volver(self.screen,300,511,443,501)

    def crear_interfaz_menu(self):
        en_pausa=True
        while en_pausa:
            #DIBUJAR IMAGEN
            self.screen.blit(self.imagen_menu_principal,(0,0))
            self.boton_salir.boton_constante()
            self.boton_volver.boton_constante()
            pygame.display.flip()
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_pausa = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_volver.accion_clic():
                        en_pausa = False  # Suponiendo que es_clic es un método de la clase Boton
                    elif self.boton_salir.accion_clic():
                        pygame.quit()  # Suponiendo que es_clic es un método de la clase Boton