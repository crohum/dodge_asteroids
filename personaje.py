import pygame


class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 5
        self.color = 'red'
        self.imagen = pygame.image.load('assets/nave.png')
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # Este es un placeholder de la nave
        # pygame.draw.rect(ventana, self.color, self.forma)
        ventana.blit(self.imagen, self.forma)
