import pygame
import sys

# Colores
verde = (19, 255, 0)
verde_claro = (103, 187, 41)
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul_cian = (0, 224, 255)
rojo = (255, 0, 0)
morado = (255, 0, 197)
gris = (103, 108, 100)
gris_oscuro = (40, 41, 40)
ventana_color = (187, 224, 229)
azul_oscuro = (18, 112, 174)
cafe = (174, 115, 18)
amarillo = (255, 255, 0)
gris_luna = (60, 60, 60)
rosa_chicle = (255, 105, 180)
turquesa = (64, 224, 208)
naranja = (255, 140, 0)
violeta = (138, 43, 226)
verde_menta = (152, 255, 152)

# Inicialización
pygame.init()
ventana = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Tren")
fuente_arial = pygame.font.SysFont("arial", 30, 1, 1)
clock = pygame.time.Clock()


arbol = pygame.image.load("img/árbol.png") 
arbol = pygame.transform.scale2x(arbol)

# Variables
XX = 25
MOVIMIENTO = 2.5
pupila_dre = 480
pupila_izq = 420

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(blanco)

    # Movimiento del árbol
    XX += MOVIMIENTO
    if XX >= 385:
        XX = -175
        MOVIMIENTO = 2.5
    elif XX >= 200:
        pupila_dre = 500
        pupila_izq = 440
    else:
        pupila_dre = 480
        pupila_izq = 420

    # Textos
    ventana.blit(fuente_arial.render("Colegio San José De Guanentá", True, morado), (200, 25))
    ventana.blit(fuente_arial.render("Especialidad de sistemas", True, verde), (235, 60))
    ventana.blit(fuente_arial.render("Nicolás Alfonso Cabrera Suárez", True, azul_cian), (0, 670))

    # Dibujo del tren y escenario
    pygame.draw.rect(ventana, verde, (25, 125, 750, 500))
    pygame.draw.circle(ventana, rosa_chicle, (225, 500), 40)
    pygame.draw.rect(ventana, violeta, (235, 460, 15, 80))
    pygame.draw.rect(ventana, violeta, (210, 440, 25, 115))
    pygame.draw.rect(ventana, naranja, (250, 450, 325, 100))
    pygame.draw.circle(ventana, turquesa, (320, 550), 40)
    pygame.draw.circle(ventana, turquesa, (415, 550), 40)
    pygame.draw.circle(ventana, turquesa, (510, 550), 40)
    pygame.draw.rect(ventana, rosa_chicle, (320, 540, 80, 30))
    pygame.draw.rect(ventana, rosa_chicle, (440, 540, 80, 30))
    pygame.draw.rect(ventana, violeta, (275, 390, 40, 60))
    pygame.draw.rect(ventana, violeta, (255, 360, 80, 30))
    pygame.draw.rect(ventana, morado, (360, 300, 200, 150))
    pygame.draw.rect(ventana, ventana_color, (392, 315, 140, 125))
    pygame.draw.rect(ventana, naranja, (345, 265, 235, 35))
    pygame.draw.rect(ventana, naranja, (385, 230, 160, 35))
    pygame.draw.circle(ventana, azul_oscuro, (460, 376), 60)
    pygame.draw.circle(ventana, blanco, (430, 370), 20)
    pygame.draw.circle(ventana, blanco, (490, 370), 20)
    pygame.draw.circle(ventana, rojo, (460, 405), 15)

    # Pupilas
    pygame.draw.circle(ventana, cafe, (pupila_dre, 370), 5)
    pygame.draw.circle(ventana, cafe, (pupila_izq, 370), 5)

    # Árbol
    ventana.blit(arbol, (XX, 280))

    pygame.display.flip()


