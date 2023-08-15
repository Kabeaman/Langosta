import pygame
from pygame.locals import QUIT
import random
ventana_horizontal = 800
ventana_vertical = 600
FPS = 60
negro = (0, 0 ,0)
bg = pygame.image.load("canchita.png")

class pelotaPong:
    def __init__(self, fichero_imagen):

        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()

        self.x = ventana_horizontal / 2 - self.ancho / 2
        self.y = ventana_vertical / 2 - self.alto / 2

        self.dir_x = random.choice ([-4, 4])
        self.dir_y = random.choice ([-4, 4])

        # Puntuación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0


    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y
        
    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= ventana_horizontal-12:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= ventana_vertical-12:
            self.dir_y = -self.dir_y
    
#se resta 12 a las ventanas porque es el tamaño de la pelota.

    def reiniciar(self):
        self.x = ventana_horizontal / 2 - self.ancho / 2
        self.y = ventana_vertical / 2 - self.alto / 2
        self.dir_x = - self.dir_x
        self.dir_y = random.choice ([-4, 4])


class raquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load('boquita_raqueta.png').convert_alpha()

#dimension de la raqueta

        self.ancho, self.alto = self.imagen.get_size()

#posicion de la raqueta
        self.x = 0
        self.y = ventana_vertical / 2 - self.alto / 2

# Dirección de movimiento de la Raqueta
        self.dir_y = 0
    
    def mover (self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= ventana_vertical:
            self.y = ventana_vertical - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_IA(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self. ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x 
            pelota.x = self.x - pelota.ancho

class raquetaPong2():
    def __init__(self):
        self.imagen = pygame.image.load('gallina_raqueta.png').convert_alpha()
#dimension de la raqueta

        self.ancho, self.alto = self.imagen.get_size()

#posicion de la raqueta
        self.x = 0
        self.y = ventana_vertical / 2 - self.alto / 2

# Dirección de movimiento de la Raqueta
        self.dir_y = 0
    
    def mover (self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= ventana_vertical:
            self.y = ventana_vertical - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear_IA(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self. ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x 
            pelota.x = self.x - pelota.ancho

def main():
    pygame.init()
    ventana = pygame.display.set_mode((ventana_horizontal, ventana_vertical))
    pygame.display.set_caption('PONG')
    
    fuente = pygame.font.Font(None, 60)

    pelota = pelotaPong('bola_roja.png')


    raqueta_1 = raquetaPong()
    raqueta_1.x = 60

    raqueta_2 = raquetaPong2()
    raqueta_2.x = ventana_horizontal - 60 - raqueta_2.ancho



    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_IA(pelota)

        
        ventana.blit(bg, (0, 0))
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, negro)
        ventana.blit(letrero, (ventana_horizontal / 2 - fuente.size(texto)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0
            

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()