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
    pygame.draw.rect(ventana, (200,200,200), (1170, 10, 100, 100))
    pygame.draw.rect(ventana, (200,200,200), (10, 610, 100, 100))
    pygame.draw.rect(ventana, (200,200,200), (1170, 610, 100, 100))
    pygame.draw.circle(ventana, (200,200,200), (170, 60), 50)
    pygame.draw.line(ventana, (200,200,200), (10, 360), (1270, 360))
    pygame.draw.polygon(ventana, (255,255,255), ((400, 400), (450, 400),
                                                 (450, 350), (500, 350),
                                                 (500, 400), (550, 400),
                                                 (550, 450), (400, 450)))

    pygame.display.update()
