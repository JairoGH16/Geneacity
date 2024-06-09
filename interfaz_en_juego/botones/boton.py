import pygame

class Boton:
    def __init__(self,screen,x_inicial,x_final,y_inicial,y_final):
        self.screen=screen
        self.imagen_normal=None
        self.imagen_marcado=None
        self.x_inicial:int=x_inicial
        self.x_final:int=x_final
        self.y_inicial:int=y_inicial
        self.y_final:int=y_final
        self.marcado:bool=False
    
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
            else:
                self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
                self.marcado=False
        else:
            self.screen.blit(self.imagen_normal,(self.x_inicial,self.y_inicial))
            self.marcado=False

    def accion_clic(self):
        if self.marcado==True:
            return True