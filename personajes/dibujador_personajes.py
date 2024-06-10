import pygame

class Dibujador_personajes:
    """Dibuja personajes
    """
    def __init__(self,screen):
        self.screen=screen
        self.sprite_bebe=pygame.image.load("personajes/bebe/abajo1.png")
        self.sprite_niño=pygame.image.load("personajes/niño/abajo_derecha1.png")
        self.sprite_niña=pygame.image.load("personajes/niña/abajo_derecha1.png")
        self.sprite_adolescente_hombre=pygame.image.load("personajes/adolescente_hombre/abajo_derecha1.png")
        self.sprite_adolescente_mujer=pygame.image.load("personajes/adolescente_mujer/abajo_derecha1.png")
        self.sprite_adulto_joven=pygame.image.load("personajes/adulto1/abajo_derecha1.png")
        self.sprite_adulta_joven=pygame.image.load("personajes/adulta1/abajo_derecha1.png")
        self.sprite_adulto_normal=pygame.image.load("personajes/adulto2/abajo_derecha1.png")
        self.sprite_adulta_normal=pygame.image.load("personajes/adulta2/abajo_derecha1.png")
        self.sprite_adulto_mayor=pygame.image.load("personajes/adulto_mayor/abajo_derecha1.png")
        self.sprite_adulta_mayor=pygame.image.load("personajes/adulta_mayor/abajo_derecha1.png")

    def _dibujar_un_personaje(self,personaje,x,y):
        """_Dibuja un personaje según su edad
        """
        if int(personaje["age"])<2:
                self.screen.blit(self.sprite_bebe, (x, y))
        elif personaje["gender"]=="Male":
            if int(personaje["age"])>=2 and int(personaje["age"])<12:
                self.screen.blit(self.sprite_niño, (x, y))
            elif int(personaje["age"])>=12 and int(personaje["age"])<20:
                self.screen.blit(self.sprite_adolescente_hombre, (x, y))
            elif int(personaje["age"])>=20 and int(personaje["age"])<40:
                self.screen.blit(self.sprite_adulto_joven, (x, y))
            elif int(personaje["age"])>=40 and int(personaje["age"])<65:
                self.screen.blit(self.sprite_adulto_normal, (x, y))
            elif int(personaje["age"])>=65:
                self.screen.blit(self.sprite_adulto_mayor, (x, y))
        elif personaje["gender"]=="Female":
            if int(personaje["age"])>=2 and int(personaje["age"])<12:
                self.screen.blit(self.sprite_niña, (x, y))
            elif int(personaje["age"])>=12 and int(personaje["age"])<20:
                self.screen.blit(self.sprite_adolescente_mujer, (x, y))
            elif int(personaje["age"])>=20 and int(personaje["age"])<40:
                self.screen.blit(self.sprite_adulta_joven, (x, y))
            elif int(personaje["age"])>=40 and int(personaje["age"])<65:
                self.screen.blit(self.sprite_adulta_normal, (x, y))
            elif int(personaje["age"])>=65:
                self.screen.blit(self.sprite_adulta_mayor, (x, y))