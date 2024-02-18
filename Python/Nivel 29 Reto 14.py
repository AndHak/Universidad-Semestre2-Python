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

#Funciones

def nave_arriba(superficie, x, y):
    pygame.draw.rect(ventana, azul, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x, y, 30, 60))
    pygame.draw.rect(ventana, negro, (x + 70, y, 30, 60))
def nave_abajo(superficie, x, y):
    pygame.draw.rect(ventana, azul, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x, y + 40, 30, 60))
    pygame.draw.rect(ventana, negro, (x + 70, y + 40, 30, 60))
def nave_izquierda(superficie, x, y):
    pygame.draw.rect(ventana, azul, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x, y, 60, 30))
    pygame.draw.rect(ventana, negro, (x, y + 70, 60, 30))
def nave_derecha(superficie, x, y):
    pygame.draw.rect(ventana, azul, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x + 40, y, 60, 30))
    pygame.draw.rect(ventana, negro, (x + 40, y + 70, 60, 30))

def asteroide_1(superficie, x, y):
    pygame.draw.rect(ventana, rojo, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x, y, 50, 50))
def asteroide_2(superficie, x, y):
    pygame.draw.rect(ventana, rojo, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x+50, y, 50, 50))
def asteroide_3(superficie, x, y):
    pygame.draw.rect(ventana, rojo, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x, y+50, 50, 50))
def asteroide_4(superficie, x, y):
    pygame.draw.rect(ventana, rojo, (x, y, 100, 100))
    pygame.draw.rect(ventana, negro, (x+50, y+50, 50, 50))



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

direccion = "arriba"
contador = 0

while exe:

    reloj.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direccion = "derecha"
                nave_x_vel = 10
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                nave_x_vel = -10
            if event.key == pygame.K_UP:
                direccion = "arriba"
                nave_y_vel = -10
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
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

    contador += 1
    if contador >= 71:
        contador = 1
    elif contador < 11:
        asteroide_1(ventana, asteroide_x, asteroide_y)
    elif contador < 31:
        asteroide_2(ventana, asteroide_x, asteroide_y)
    elif contador < 51:
        asteroide_3(ventana, asteroide_x, asteroide_y)
    elif contador < 71:
        asteroide_4(ventana, asteroide_x, asteroide_y)

    if direccion == "arriba":
        nave_arriba(ventana, nave_x, nave_y)
    if direccion == "abajo":
        nave_abajo(ventana, nave_x, nave_y)
    if direccion == "derecha":
        nave_derecha(ventana, nave_x, nave_y)
    if direccion == "izquierda":
        nave_izquierda(ventana, nave_x, nave_y)


    pygame.display.update()

pygame.quit()