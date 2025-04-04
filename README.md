# Estructura de un juego en pygame

## Inicialización 

- Como en todo programa en python se debe importar los módulos o librerias a utilizar. 
`import pygame`

- Inicializar pygame usando la función init(). Inicializa todos los módulos de pygame iportados.
`pygame.init()`

## Visualización de la ventana

`ventana = pygame.display.set_mode((600, 400))`

- set_mode() es la función encargada de definir el tamaño de la ventana. En el ejemplo se esta definienfo una ventana de 600 px de ancho y 400 px de alto.

`pygame.display.set_caption("Mi ventana")`

- set_caption() es la función que añade un titulo a la ventana.

### Función set_mode().

`set_mode(size = (0,0), flags = 0, depth = 0, display = 0)`

- size = (600,400) : define el tamaño de la ventana.

- flags: define uno o más comportamienetos para la ventana.
    - Valores:
        - pygame.FULLSCREEN.
        - pygame.RESIZABLE.
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla copleta, dimenciones modificables. 

## Bucle del juego - game loop.

- Bucle infinito que se interrumpirá  al cumplir ciertos criterios.

- Reloj interno del juego.

- En cada iteración del bucle del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado a otro, o que se a cruzado la linea de llegada lo que quiere decir que la partida a terminado.

- Cada iteración es una oportunidad para realizar todo las datos relacionados con el estado actual de la partida.

- En cada iteracion se realizan las siguientes tareas:

    1. comprobar que no se alcanzan las condicones de parada, en cuyo caso se interrumpe el bucle.

    2. Actualizar los recursos nesesarios para la iteracion actual.

    3. Optener las entradas del sistema, o la interacción con el jugador.

    4. Actualizar todas las entidades que caracterizan el juego.

    5. Refrescar la pantalla.

## Superficies pygame

- Superficie:
    
    - Elemento geométrico

    - Linea, poligono, imagen, texto que se mmuestra en la pantalla

    - El poligono se puede o no rellenar de color

    - Las superficies se crean de diferente manera dependiendo del tipo: 

        - image: image.load()
        
        - texto: font.render()

        - Superficie generica: pygame.surface()

        - Ventana del juego: pygame.display.set_mode()

### Bandera de Colombia

```Python
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
```

![Bandera de Colombia](bandera_colombia.jpg "Bandera de Colombia")