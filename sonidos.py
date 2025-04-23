import pygame
import sys

# inicializar los modlos
pygame.init()
pygame.mixer.init()

#colores

COLOR_BLANCO = pygame.Color(255,255,255)

#ventana
PANTALLA = pygame.display.set_mode((400,400))
PANTALLA.fill(COLOR_BLANCO)
pygame.display.set_caption("Soidos en Pygame")

continuar = True

#Sonido de fondo
SILBATO = pygame.mixer.music.load("sounds/silbato.ogg")
pygame.mixer.music.play(1,0.0)

# efectos sonoros 
GALLO = pygame.mixer.Sound("sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("sound/cuervo.ogg")
BICI = pygame.mixer.Sound("sound/timbre.ogg")

#bucle del juego

while continuar:
    for event in pygame.event.get():
        # Cierra la ventana si se hace click en el boton de cerrar ventana
        if event.type == pygame.QUIT:
            continuar = False
        # detecta si se opriio una tecla
        elif event.type == pygame.KEYDOWN:
            pass

pygame.display.flip()
        