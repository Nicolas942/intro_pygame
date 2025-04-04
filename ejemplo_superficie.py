#importamos la libreria pygame
import pygame
import random

#inicializamos los módulas de pygame
pygame.init()

#establecer titulo ala ventana
pygame.display.set_caption("Surface")

#establecer dimenciones de la ventana
ventana = pygame.display.set_mode((400,400))

#definir un color
rojo = random.randint(0,256)
verde = random.randint(0,256)
azul = random.randint(0,256)
color_aleatorio = ((rojo,verde,azul))

#crear una superficie

color_aleatorio = pygame.Surface((200,200))

#rellenamos la superficie de azul
color_aleatorio.fill((rojo,verde,azul))

#muevo la superficie en la ventana
ventana.blit(color_aleatorio, (100,100))

#actualiza la visualizacion de la ventana
pygame.display.flip()

#bucle del juego

while True:
    event = pygame.event.wait()
    if event == pygame.QUIT:
        break

pygame.quit()

