import pygame

pygame.init()
pantalla = pygame.display.set_mode((400, 300))

# Sprite básico
class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))  # Verde
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, mover=False):
        if mover:
            self.rect.x += 5  # Mueve a la derecha

# Crear sprites y grupo
bloque1 = Bloque(50, 50)
bloque2 = Bloque(150, 100)
grupo = pygame.sprite.Group(bloque1, bloque2)

# Bucle del juego
running = True
while running:
    mover = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verifica si se está presionando la flecha derecha
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        mover = True

    grupo.update(mover)           # Actualiza los sprites con el parámetro mover
    pantalla.fill((0, 0, 0))      # Fondo negro
    grupo.draw(pantalla)         # Dibuja todos los bloques
    pygame.display.flip()

pygame.quit()
