#importamos la libreria pygame
import pygame

#inicializamos los módulas de pygame
pygame.init()

#establecer titulo ala ventana
pygame.display.set_caption("Bandera de Colombia")

#establecer dimenciones de la ventana
ventana = pygame.display.set_mode((400,400))

#definir un color
amarillo = (255, 250, 0)
azul = (0,0,255)
rojo = (255,0,0)

#crear una superficie(tamaño de la franja)

color_amarillo = pygame.Surface((400,200))
color_azul = pygame.Surface((400,100))
color_rojo = pygame.Surface((400,100))

#rellenamos la superficie de azul
color_amarillo.fill((amarillo))
color_azul.fill((azul))
color_rojo.fill((rojo))


#muevo la superficie en la ventana(coordenadas de la franja)
ventana.blit(color_amarillo, (0,0))
ventana.blit(color_azul, (0,200))
ventana.blit(color_rojo, (0,300))

#actualiza la visualizacion de la ventana
pygame.display.flip()

#bucle del juego

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()