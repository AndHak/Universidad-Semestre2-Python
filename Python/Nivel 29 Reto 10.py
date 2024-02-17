import pygame

pygame.init()

ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

x = 0
y = 270

exe = True
aumento = 1

fuente = pygame.font.SysFont("Corporation Games", 100)
fuente2 = pygame.font.SysFont("consolas", 20)

puntos = 0
vueltas = 0

texto = fuente.render("VIDEO JUEGOS", True, (0, 255, 0))

while exe:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exe = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                puntos += 1

    ventana.fill((0, 0, 0))

    x += aumento
    if x > ancho:
        x = -100
        aumento += 1
        vueltas += 1

    #Dibujar
    pygame.draw.rect(ventana, (200,200,200), (x, y, 100, 100))
    texto_puntos = fuente2.render(f"Puntos: {puntos}", True, (255,255,255))
    texto_vueltas = fuente2.render(f"Vueltas: {vueltas}", True, (255,255,255))

    ventana.blit(texto_puntos, (40, 30))
    ventana.blit(texto_vueltas, (1100, 30))
    ventana.blit(texto, (250, 10))

    pygame.display.update()



