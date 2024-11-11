import pygame


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 75
        self.alto = 75
        self.velocidad = 5
        self.color = 'purple'
        self.imagen = pygame.image.load('assets/asteroid.png')
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # Este es un placeholder de los asteroides
        # pygame.draw.rect(ventana, self.color, self.forma)
        ventana.blit(self.imagen, self.forma)

    def movimiento(self):
        self.y += self.velocidad
