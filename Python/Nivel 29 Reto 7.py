import pygame

pygame.init()

ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

x = 0
y = 100

exe = True

while exe:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exe = False

    ventana.fill((148, 0, 163))

    x += 1
    if x > ancho:
        x = 0

    #Dibujar
    pygame.draw.rect(ventana, (200,200,200), (x, y, 100, 100))

    pygame.display.update()

    pygame.time.delay(1)




