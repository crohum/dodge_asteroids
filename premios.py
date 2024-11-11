import pygame


class Premio:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 6
        self.tipo = 1
        self.color = 'yellow'
        self.imagen = pygame.image.load('assets/estrella.png')
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.forma = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # Este es un placeholder de los premios
        # pygame.draw.rect(ventana, self.color, self.forma)
        ventana.blit(self.imagen, self.forma)

    def movimiento(self):
        self.y += self.velocidad


'''class Bonus(Premio):
    def __init__(self):
        self.tipo = 2
        self.color = 'green'
'''