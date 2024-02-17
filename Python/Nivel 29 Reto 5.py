import pygame

pygame.init()

ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

exe = True

while exe:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exe = False

    ventana.fill((148, 0, 163))

    #Dibujar
    pygame.draw.rect(ventana, (200,200,200), (10, 10, 100, 100))

    pygame.display.update()
