import pygame

class Personaje:
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen
        self.img_direccion:str="derecha_abajo" #Es la dirección de la imagen, no del movimiento
        #SPRITES PARA LOS PERSONAJES
        #Imagenes de bebé
        #Abajo
        self.img_bebe_abajo1=pygame.image.load('personajes/bebe/abajo1.png')
        self.img_bebe_abajo2=pygame.image.load('personajes/bebe/abajo2.png')
        self.img_bebe_abajo3=pygame.image.load('personajes/bebe/abajo3.png')
        #Imagenes de niño
        self.img_niño_derecha = pygame.image.load('personajes/niño/derecha_abajo.png')
        self.img_niño_izquierda = pygame.image.load('personajes/niño/izquierda.png')
        self.img_niño_arriba = pygame.image.load('personajes/niño/arriba.png')

    def actualizar_direccion_personaje(self,tecla):
        if tecla==1073741903 or tecla==100:
            self.img_direccion="derecha"
        if tecla==1073741905 or tecla==115:
            self.img_direccion="abajo"
        if tecla==1073741904 or tecla==97:
            self.img_direccion="izquierda"
        if tecla==1073741906 or tecla==119:
            self.img_direccion="arriba"

    def dibujar_personaje(self,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if self.img_direccion=="derecha":
            screen.blit(self.img_niño_derecha, (x, y))
        if self.img_direccion=="abajo":
            screen.blit(self.img_niño_derecha, (x, y))
        if self.img_direccion=="izquierda":
            screen.blit(self.img_niño_izquierda, (x, y))
        if self.img_direccion=="arriba":
            screen.blit(self.img_niño_arriba, (x, y))