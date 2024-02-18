import pygame

#Medidas
ancho = 1280
alto = 720

#Colores
negro = (0,0,0)
blanco = (255,255,255)
azul = (0,0,255)
verde = (0,255,0)
rojo = (255,0,0)

#Inicializar
pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
fuente = pygame.font.SysFont("Corporation Games", 60)
fuente2 = pygame.font.SysFont("consolas", 20)
asteroide_x = -100
asteroide_y = 100
asteroide_x_vel = 5
nave_x = 540
nave_y = 610
nave_x_vel = 0
nave_y_vel = 0

#Modulo
exe = True
reloj = pygame.time.Clock()

while exe:

    reloj.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave_x_vel = 10
            if event.key == pygame.K_LEFT:
                nave_x_vel = -10
            if event.key == pygame.K_UP:
                nave_y_vel = -10
            if event.key == pygame.K_DOWN:
                nave_y_vel = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave_x_vel = 0
            if event.key == pygame.K_LEFT:
                nave_x_vel = 0
            if event.key == pygame.K_UP:
                nave_y_vel = 0
            if event.key == pygame.K_DOWN:
                nave_y_vel = 0


    asteroide_x += asteroide_x_vel
    if asteroide_x > 1280:
        asteroide_x = -100

    nave_x += nave_x_vel
    nave_y += nave_y_vel

    titulo = fuente.render("Mover personaje", True, verde)
    ventana.fill(negro)
    ventana.blit(titulo, (300, 20))
    pygame.draw.rect(ventana, azul, (nave_x, nave_y, 100, 100))
    pygame.draw.rect(ventana, rojo, (asteroide_x, asteroide_y, 100, 100))


    pygame.display.update()

pygame.quit()