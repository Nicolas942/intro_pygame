# Ejemplo de Sprite del módulo sprite de Pygame

## Explicación de Sprites

Un Sprite en Pygame es una forma fácil de representar cosas en tu juego, como personajes o enemigos.
Te permite:

    - Ponerle una imagen y una posición al objeto.

    - Agruparlos para moverlos y dibujarlos todos juntos.

    - Aprovechar cosas listas para detectar choques o animarlos fácilmente.



## Código

```Python
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

pygame.quit()
```


## Explicación de Group

Un Group es una forma fácil de organizar y controlar muchos sprites juntos.
Te permite:

    - Dibujarlos todos con una sola línea.

    - Actualizarlos todos al mismo tiempo.

    - Revisar colisiones entre ellos.

```Python
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

```