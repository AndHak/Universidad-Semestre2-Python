import pygame
import random

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
funete = pygame.font.SysFont("arial", 30)
reloj = pygame.time.Clock()

#Datos
cuadrados = []
for i in range(200):
    x = random.randint(1,1279)
    y = random.randint(1, 719)
    c = [x, y]
    cuadrados.append(c)
frames = 0
transcurrido = 0
segundos = 0
fps = 0
mostrar_fps = False

#Modulo logico
exe = True
lloviendo = True
tiempo_de_lluvia = 0
velocidad_x = 0.5
velocidad_y = 1
while exe:

    tiempo = reloj.tick()
    transcurrido += tiempo
    frames += 1

    if transcurrido >= 1000:
        fps = frames
        frames = 0
        segundos += 1
        transcurrido = 0
    
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exe = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exe = False
            elif event.key == pygame.K_e:
                mostrar_fps = not mostrar_fps

    # Logica
    if lloviendo:
        tiempo_de_lluvia += tiempo

        for c in cuadrados:
            c[0] += velocidad_x
            c[1] += velocidad_y

            if c[0] > 1280:
                c[0] = 0
            if c[1] > 720:
                c[1] = 0

    #Imagenes
    ventana.fill(negro)
    for c in cuadrados:
        pygame.draw.rect(ventana, blanco, (c[0], c[1], 2, 2))

    texto = funete.render(f"{fps}", True, blanco)
    texto2 = funete.render(f"{segundos}", True, blanco)
    if mostrar_fps:
        texto = funete.render(f"FPS: {fps}", True, blanco)
        texto2 = funete.render(f"Segundos: {segundos}", True, blanco)
        ventana.blit(texto, (80, 100))
        ventana.blit(texto2, (80, 140))

    #Update
    pygame.display.update()


pygame.quit()

