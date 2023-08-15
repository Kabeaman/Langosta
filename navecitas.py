from typing_extensions import Self
import pygame 
import random
from pygame.locals import QUIT

ventana_horizontal = 800
ventana_vertical = 600
FPS = 60
FONDO = pygame.image.load('espacio.png')
class navecita:
    def __init__(self, fichero_imagen):

        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()

        self.x = ventana_horizontal / 2 - self.ancho / 2
        self.y = (ventana_vertical*1.5) / 2 - (self.alto*1.5) / 2

        self.dir_x = 0
        self.dir_y = 0

    def mover (self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= ventana_vertical:
            self.y = ventana_vertical - self.alto
        self.x += self.dir_x
        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= ventana_horizontal:
            self.x = ventana_horizontal - self.ancho

class bala:
    def __init__(self):
        self.imagen = pygame.image.load('bola_roja.png').convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()

        self.dir_x = 0
        self.dir_y = 0

        self.x = 0
        self.y = 0
        self.vel = 0


def main():
    pygame.init()
    ventana = pygame.display.set_mode((ventana_horizontal, ventana_vertical))
    pygame.display.set_caption('NAVECITA')

    nave = navecita('nave_roja.png')
    jugando = True
    while jugando:
        nave.mover()
        ventana.blit(FONDO, (0, 0))
        ventana.blit(nave.imagen, (nave.x, nave.y))
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    nave.dir_y = -5
                if event.key == pygame.K_s:
                    nave.dir_y = 5 
                if event.key == pygame.K_d:
                    nave.dir_x = 5   
                if event.key == pygame.K_a:
                    nave.dir_x = -5
                if event.key == pygame.K_f:
                    bala.dir_x = nave.dir_x 
                    bala.vel = 8
               
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    nave.dir_y = 0
                if event.key == pygame.K_s:
                    nave.dir_y = 0
                if event.key == pygame.K_d:
                    nave.dir_x = 0
                if event.key == pygame.K_a:
                    nave.dir_x = 0
                if event.key == pygame.K_f:
                    bala.vel = 0
                    bala.dir_x = 0
                

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()