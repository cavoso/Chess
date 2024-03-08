import pygame
import sys


SIZE  = 800
CASILLA = SIZE / 8 
TABLERO  = []

pygame.init()
pantalla = pygame.display.set_mode((SIZE, SIZE))
FUENTE = pygame.font.SysFont("Arial", 24)

CASILLA_BLANCA = pygame.image.load("assets/tablero/square_brown_light.png")
CASILLA_NEGRA = pygame.image.load("assets/tablero/square_brown_dark.png")

while True:
    # Leer eventos
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar el juego
    # ...

    # Dibujar el tablero y las piezas
    for fila in range(8):
        for columna in range(8):
            if (fila + columna) % 2 == 0:
                pantalla.blit(CASILLA_BLANCA, (columna * CASILLA, fila * CASILLA))
            else:
                pantalla.blit(CASILLA_NEGRA, (columna * CASILLA, fila * CASILLA))

            


    # Actualizar la pantalla
    pygame.display.update()