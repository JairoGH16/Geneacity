import pygame

class Administrador_personajes:
    def __init__(self,screen,edad,genero):    
    # Inicializar Pygame
        pygame.init()
        self.screen=screen
        self.img_direccion:str="derecha_abajo" #Es la dirección de la imagen, no del movimiento
        self.personaje:Personaje=Personaje(screen)
        self.edad_personaje=edad
        self.genero=genero
        self.indice_animacion=0

    def actualizar_indice_personaje(self):
        if self.indice_animacion==2:
            self.indice_animacion=0
        else:
            self.indice_animacion+=1

    def actualizar_personaje(self,tecla):
        if tecla==1073741903 or tecla==100:
            self.img_direccion="derecha"
        if tecla==1073741905 or tecla==115:
            self.img_direccion="abajo"
        if tecla==1073741904 or tecla==97:
            self.img_direccion="izquierda"
        if tecla==1073741906 or tecla==119:
            self.img_direccion="arriba"
        if self.edad_personaje<2:
            self.personaje=Bebe(self.screen)
        if self.edad_personaje >=2 and self.edad_personaje<12:
            if self.genero=="Male":
                self.personaje=Niño(self.screen)
            else:
                self.personaje=Niña(self.screen)
        if self.edad_personaje >=12 and self.edad_personaje<20:
            if self.genero=="Male":
                self.personaje=Adolescente_hombre(self.screen)
            else:
                self.personaje=Adolescente_mujer(self.screen)
        if self.edad_personaje >=20 and self.edad_personaje<40:
            if self.genero=="Male":
                self.personaje=Adulto_joven(self.screen)
            else:
                self.personaje=Adulta_joven(self.screen)
        if self.edad_personaje >=40 and self.edad_personaje<65:
            if self.genero=="Male":
                self.personaje=Adulto_normal(self.screen)
            else:
                self.personaje=Adulta_normal(self.screen)
        if self.edad_personaje >=65:
            if self.genero=="Male":
                self.personaje=Adulto_mayor(self.screen)
            else:
                self.personaje=Adulta_mayor(self.screen)

    def dibujar_personaje(self):
        self.personaje.dibujar_personaje(self.img_direccion,self.indice_animacion,self.screen)

class Personaje:
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        #COLOCAR SPRITES PARA LOS PERSONAJES

    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        #screen.blit(self.nombre_de_imagen, (x, y))
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class Adulto_joven(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulto1/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulto1/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulto1/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulto1/izquierda1.png'),
                                pygame.image.load('personajes/adulto1/izquierda2.png'),
                                pygame.image.load('personajes/adulto1/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulto1/arriba1.png'),
                                pygame.image.load('personajes/adulto1/arriba2.png'),
                                pygame.image.load('personajes/adulto1/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adulta_joven(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulta1/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulta1/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulta1/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulta1/izquierda1.png'),
                                pygame.image.load('personajes/adulta1/izquierda2.png'),
                                pygame.image.load('personajes/adulta1/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulta1/arriba1.png'),
                                pygame.image.load('personajes/adulta1/arriba2.png'),
                                pygame.image.load('personajes/adulta1/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adulto_normal(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulto2/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulto2/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulto2/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulto2/izquierda1.png'),
                                pygame.image.load('personajes/adulto2/izquierda2.png'),
                                pygame.image.load('personajes/adulto2/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulto2/arriba1.png'),
                                pygame.image.load('personajes/adulto2/arriba2.png'),
                                pygame.image.load('personajes/adulto2/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adulta_normal(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulta2/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulta2/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulta2/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulta2/izquierda1.png'),
                                pygame.image.load('personajes/adulta2/izquierda2.png'),
                                pygame.image.load('personajes/adulta2/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulta2/arriba1.png'),
                                pygame.image.load('personajes/adulta2/arriba2.png'),
                                pygame.image.load('personajes/adulta2/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adulto_mayor(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulto_mayor/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulto_mayor/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulto_mayor/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulto_mayor/izquierda1.png'),
                                pygame.image.load('personajes/adulto_mayor/izquierda2.png'),
                                pygame.image.load('personajes/adulto_mayor/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulto_mayor/arriba1.png'),
                                pygame.image.load('personajes/adulto_mayor/arriba2.png'),
                                pygame.image.load('personajes/adulto_mayor/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adulta_mayor(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adulta_mayor/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adulta_mayor/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adulta_mayor/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adulta_mayor/izquierda1.png'),
                                pygame.image.load('personajes/adulta_mayor/izquierda2.png'),
                                pygame.image.load('personajes/adulta_mayor/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adulta_mayor/arriba1.png'),
                                pygame.image.load('personajes/adulta_mayor/arriba2.png'),
                                pygame.image.load('personajes/adulta_mayor/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Niño(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/niño/abajo_derecha1.png'),
                                      pygame.image.load('personajes/niño/abajo_derecha2.png'),
                                      pygame.image.load('personajes/niño/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/niño/izquierda1.png'),
                                pygame.image.load('personajes/niño/izquierda2.png'),
                                pygame.image.load('personajes/niño/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/niño/arriba1.png'),
                                pygame.image.load('personajes/niño/arriba2.png'),
                                pygame.image.load('personajes/niño/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Niño(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/niño/abajo_derecha1.png'),
                                      pygame.image.load('personajes/niño/abajo_derecha2.png'),
                                      pygame.image.load('personajes/niño/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/niño/izquierda1.png'),
                                pygame.image.load('personajes/niño/izquierda2.png'),
                                pygame.image.load('personajes/niño/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/niño/arriba1.png'),
                                pygame.image.load('personajes/niño/arriba2.png'),
                                pygame.image.load('personajes/niño/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Niña(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/niña/abajo_derecha1.png'),
                                      pygame.image.load('personajes/niña/abajo_derecha2.png'),
                                      pygame.image.load('personajes/niña/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/niña/izquierda1.png'),
                                pygame.image.load('personajes/niña/izquierda2.png'),
                                pygame.image.load('personajes/niña/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/niña/arriba1.png'),
                                pygame.image.load('personajes/niña/arriba2.png'),
                                pygame.image.load('personajes/niña/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Bebe(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo=[pygame.image.load('personajes/bebe/abajo1.png'),
                                      pygame.image.load('personajes/bebe/abajo2.png'),
                                      pygame.image.load('personajes/bebe/abajo3.png')]
        self.animacion_derecha=[pygame.image.load('personajes/bebe/derecha1.png'),
                                      pygame.image.load('personajes/bebe/derecha2.png'),
                                      pygame.image.load('personajes/bebe/derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/bebe/izquierda1.png'),
                                pygame.image.load('personajes/bebe/izquierda2.png'),
                                pygame.image.load('personajes/bebe/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/bebe/arriba1.png'),
                                pygame.image.load('personajes/bebe/arriba2.png'),
                                pygame.image.load('personajes/bebe/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adolescente_hombre(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adolescente_hombre/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adolescente_hombre/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adolescente_hombre/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adolescente_hombre/izquierda1.png'),
                                pygame.image.load('personajes/adolescente_hombre/izquierda2.png'),
                                pygame.image.load('personajes/adolescente_hombre/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adolescente_hombre/arriba1.png'),
                                pygame.image.load('personajes/adolescente_hombre/arriba2.png'),
                                pygame.image.load('personajes/adolescente_hombre/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))

class Adolescente_mujer(Personaje):
    def __init__(self,screen):
        # Inicializar Pygame
        pygame.init()
        self.screen=screen      
        self.animacion_abajo_derecha=[pygame.image.load('personajes/adolescente_mujer/abajo_derecha1.png'),
                                      pygame.image.load('personajes/adolescente_mujer/abajo_derecha2.png'),
                                      pygame.image.load('personajes/adolescente_mujer/abajo_derecha3.png')]
        self.animacion_izquierda=[pygame.image.load('personajes/adolescente_mujer/izquierda1.png'),
                                pygame.image.load('personajes/adolescente_mujer/izquierda2.png'),
                                pygame.image.load('personajes/adolescente_mujer/izquierda3.png')]
        self.animacion_arriba=[pygame.image.load('personajes/adolescente_mujer/arriba1.png'),
                                pygame.image.load('personajes/adolescente_mujer/arriba2.png'),
                                pygame.image.load('personajes/adolescente_mujer/arriba3.png')]
    def dibujar_personaje(self,direccion,indice_animacion,screen, x=400, y=400):
        """
        Dibuja una imagen en la pantalla de Pygame en la posición (x, y).

        Parámetros:
        - screen: superficie de Pygame donde se dibuja la imagen.
        - x, y: coordenadas donde se dibujará la imagen.
        """
        if direccion=="abajo":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="derecha":
            screen.blit(self.animacion_abajo_derecha[indice_animacion], (x, y))
        if direccion=="izquierda":
            screen.blit(self.animacion_izquierda[indice_animacion], (x, y))
        if direccion=="arriba":
            screen.blit(self.animacion_arriba[indice_animacion], (x, y))