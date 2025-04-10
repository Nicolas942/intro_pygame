import pygame
import sys
import random


verde = (255, 143, 0)
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul = (0,0,255)
rojo = (255,0,0)


pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("¡100 LINEAS RANDOM!")

fuente_arial = pygame.font.SysFont("arial", 30, 1, 1)

clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(azul)  

    texto = fuente_arial.render("Colegio San José De Guanentá", True, blanco)
    ventana.blit(texto, (25, 25))

    sistemas = fuente_arial.render("Especialidad de sistemas", True, blanco)
    ventana.blit(sistemas, (75, 60))

    nombre = fuente_arial.render("Nicolás Alfonso Cabrera Suárez", True, blanco)
    ventana.blit(nombre, (0, 475))

    pygame.draw.rect(ventana, verde, (50, 125,400,300 ),2)

    for i in range(100):
        linea_x = random.randint(50, 400)
        linea_y = random.randint(125,400)
        tamaño1 = random.randint(50, 400)
        tamaño2 = random.randint(125,400)

        color_aleatorio = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pygame.draw.line(ventana, color_aleatorio, (linea_x, linea_y), (tamaño1,tamaño2))

        

    pygame.display.flip()
