import pygame

pygame.init()

ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

x =1280
y = 100

x2 = 0
y2 = 0

exe = True

while exe:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exe = False

    ventana.fill((0, 0, 0))

    x -= 1
    if x < -100:
        x = 1380

    x2 += 1
    y2 += 1
    if x2 > ancho:
        x2 = -100
    if y2 > alto:
        y2 = -100


    #Dibujar
    pygame.draw.rect(ventana, (0,255,0), (x2, y2, 100, 100))
    pygame.draw.rect(ventana, (0,0,255), (x, y, 100, 100))

    pygame.display.update()

    pygame.time.delay(2)

