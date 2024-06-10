import pygame
from escritor_texto import Escritor

class Nombrar_hijo:
    def __init__(self, screen):
        self.screen = screen
        self.imagen_fondo = pygame.image.load("imagenes/interfaz/gui_nombrar_hijo.png")
        self.escritor = Escritor(self.screen)

    def nombrar_hijo(self):
        pygame.display.set_caption("Nombrar hijo")
        nombre_hijo = ""
        escribiendo = True
        while escribiendo:
            pygame.time.delay(50)
            self.screen.fill((0,0,0))
            self.screen.blit(self.imagen_fondo, (0, 0))
            self.escritor.escribir(270, 340, nombre_hijo, 25, (255, 255, 255))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Termina la ejecución del método y cierra la aplicación
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nombre_hijo = nombre_hijo[:-1]
                    elif event.key == pygame.K_RETURN:
                        escribiendo = False
                        return nombre_hijo
                    else:
                            nombre_hijo += event.unicode
