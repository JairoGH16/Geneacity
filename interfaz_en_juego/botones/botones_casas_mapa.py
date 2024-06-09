from interfaz_en_juego.botones.boton import Boton
import pygame

class Botones_casas_mapa(Boton):
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        super().__init__(screen,x_inicial,x_final,y_inicial,y_final)
        self.casa_asignada:tuple=()
        self.imagen_normal=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa1.png")
        self.imagen_marcado=pygame.image.load("imagenes/interfaz/mapa/casa_en_mapa2.png")

    def boton_constante(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >= self.x_inicial and mouse_pos[0]<= self.x_final: #x
            if mouse_pos[1] >= self.y_inicial and mouse_pos[1]<= self.y_final: #y
                self.screen.blit(self.imagen_marcado, (self.x_inicial,self.y_inicial))
                self.marcado=True
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si el botón es el izquierdo
                        if event.button == 1:  # 1 es el botón izquierdo del mouse
                            self.accion_clic()
                return True
            else:
                self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
                self.marcado=False
            return False
        else:
            self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
            self.marcado=False
        return False

    def accion_clic(self):
            pass
            #interfaz_mapa=Interfaz_durante_mapa(self.screen)
            #interfaz_mapa.crear_interfaz_mapa()