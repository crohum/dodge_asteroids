import random
import pygame
from pygame import mixer
from personaje import Ship
from enemigos import Asteroid
from premios import Premio


# Iniciamos pygame
pygame.init()


# Personalizar el Icono y Titulo (superiores)
icono = pygame.image.load('icono.png')
pygame.display.set_icon(icono)
pygame.display.set_caption("Asteroid's Rain")


# Musica de fondo  *** Pendiente buscar una rolita cumplidora ***
#mixer.music.load('musica_fondo.mp3')
#mixer.music.set_volume(0.5)
#mixer.music.play(-1)


# Poner el fondo
fondo = pygame.image.load('assets/fondo.png')


# Definimos propiedades de la ventana de juego
ancho = 1000
alto = 800
ventana = pygame.display.set_mode([ancho, alto])
textos = pygame.font.SysFont('Comics Sans', 45)

# Estandarizamos la velocidad del juego sin importar que tan potente sea el ordenador
fps = 60


# Indicador para que no cierre la ventana
jugando = True
se_ejecuta = True


# Reloj para control de sucesos
reloj = pygame.time.Clock()
tiempo_transcurrido = 0


# Bloque de personaje
nave = Ship(500, 400)
vidas = 5
puntaje = 0


# Bloque de enemigos
asteroides = []
tiempo_entre_asteroides = 500


# Bloque de premios
premios = []
contador = 0
bonificador = 0


def gestionar_teclas(teclas):
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        nave.y -= nave.velocidad
    elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        nave.y += nave.velocidad
    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        nave.x -= nave.velocidad
    elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        nave.x += nave.velocidad


# Funcion texto final del juego
def texto_final():
    mensaje_final = textos.render(' JUEGO TERMINADO', True, (255, 255, 255))
    ventana.blit(mensaje_final, (80, 200))


# Loop del juego
while jugando and vidas > 0:

    # Colocar la Imagen del fondo de pantalla
    ventana.blit(fondo, (0, 0))

    # Aparicion de asteroides
    tiempo_transcurrido += reloj.tick(fps)
    if tiempo_transcurrido > tiempo_entre_asteroides:
        asteroides.append(Asteroid(random.randint(0, ancho), -80))
        tiempo_transcurrido = 0

        # Aparicion de las cajas de premios
        contador += 1
        if contador > 5:
            premios.append(Premio(random.randint(0, ancho), -15))
            contador = 0

    # Aparicion de cajas Bonus
    if bonificador > 5:
        pass

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()
    gestionar_teclas(teclas)

    texto_vidas = textos.render(f'Vidas: {vidas}', True, 'white')
    texto_puntos = textos.render(f'Puntos: {puntaje}', True, 'white')

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    nave.dibujar(ventana)

    for premio in premios:
        premio.dibujar(ventana)
        premio.movimiento()

        # captura de premios
        if pygame.Rect.colliderect(nave.forma, premio.forma):
            sonido_premio = mixer.Sound("assets/premio.mp3")
            sonido_premio.play()
            puntaje += 100
            premios.remove(premio)

    for asteroide in asteroides:
        asteroide.dibujar(ventana)
        asteroide.movimiento()

        # daño de enemigos
        if pygame.Rect.colliderect(nave.forma, asteroide.forma):
            sonido_colision = mixer.Sound("assets/explosion.mp3")
            sonido_colision.play()
            vidas -= 1
            asteroides.remove(asteroide)

        # remover enemigos fuera de pantalla
        if asteroide.alto + asteroide.y > alto + 80:
            puntaje += 1
            asteroides.remove(asteroide)

    ventana.blit(texto_vidas, (10, 10))
    ventana.blit(texto_puntos, (10, 50))

    pygame.display.update()


# Fin del juego
while se_ejecuta:

texto_final()
pygame.display.update()
