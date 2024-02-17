import pygame

pygame.init()

ancho = 1280
alto = 720

ventana = pygame.display.set_mode((ancho, alto), pygame.FULLSCREEN)

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False

    ventana.fill((127, 200, 111))
    pygame.display.update()