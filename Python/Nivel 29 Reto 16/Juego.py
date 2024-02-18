import pygame

# Medidas
ancho = 1280
alto = 720

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul = (0, 0, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Imagenes
fondo = pygame.image.load(r"Python\Nivel 29 Reto 16\fondo.jpg")
asteroide = pygame.image.load(r"Python\Nivel 29 Reto 16\asteroide.png")
nave = pygame.image.load(r"Python\Nivel 29 Reto 16\nave.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))


# Inicializar
pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
fuente = pygame.font.SysFont("Corporation Games", 60)
fuente2 = pygame.font.SysFont("consolas", 20)

# Posición, ángulo y velocidad de la nave
nave_x = 590
nave_y = 610
angulo = 0

# Modulo
exe = True
reloj = pygame.time.Clock()
direccion = "arriba"
velocidad_x = 0
velocidad_y = 0

while exe:

    reloj.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direccion = "arriba"
                velocidad_y = -5
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                velocidad_y = 5
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                velocidad_x = -5
            if event.key == pygame.K_RIGHT:
                direccion = "derecha"
                velocidad_x = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidad_y = 0
            if event.key == pygame.K_DOWN:
                velocidad_y = 0
            if event.key == pygame.K_LEFT:
                velocidad_x = 0
            if event.key == pygame.K_RIGHT:
                velocidad_x = 0
        

    coordenadas_recorte = (0, 0, ancho, alto)
    fondo_recortado = fondo.subsurface(coordenadas_recorte)

    ventana.blit(fondo_recortado, (0, 0))
    ventana.blit(asteroide, (100, 300))

    nave_x += velocidad_x
    nave_y += velocidad_y

    rotated_nave = pygame.transform.rotate(nave, angulo)  

    if direccion == "arriba":
        angulo = 0
    elif direccion == "abajo":
        angulo = 180
    elif direccion == "derecha":
        angulo = -90
    elif direccion == "izquierda":
        angulo = 90

    rotated_nave_rect = rotated_nave.get_rect(center=(nave_x, nave_y))
    ventana.blit(rotated_nave, rotated_nave_rect.topleft)

    pygame.display.update()

pygame.quit()
