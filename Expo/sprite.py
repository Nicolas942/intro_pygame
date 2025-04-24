import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo Sprite")

# Definir la clase usando Sprite
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llama al constructor de Sprite
        self.image = pygame.Surface((50, 50))  # Crea una "imagen" para el sprite
        self.image.fill((255, 0, 0))  # Rellena con rojo
        self.rect = self.image.get_rect()  # Obtiene el rectángulo asociado a la imagen
        self.rect.topleft = (100, 100)  # Posición inicial

    def update(self):
        self.rect.x += 5  # Mover a la derecha cada vez que se actualiza

# Crear una instancia del sprite
jugador = Jugador()

# Crear un grupo para gestionar sprites
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(jugador)

# Bucle principal
reloj = pygame.time.Clock()
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    todos_los_sprites.update()  # Llama al método update() de cada sprite del grupo

    screen.fill((30, 30, 30))  # Fondo gris oscuro
    todos_los_sprites.draw(screen)  # Dibuja todos los sprites en pantalla
    pygame.display.flip()  # Actualiza la pantalla

    reloj.tick(60)  # Limita a 60 FPS