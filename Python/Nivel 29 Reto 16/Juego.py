import pygame
import random

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
asteroide_pequeño = pygame.image.load(r"Python\Nivel 29 Reto 16\asteroide.png")
asteroide_grande = pygame.image.load(r"Python/Nivel 29 Reto 16/asteroide_grande.png")
asteroide_gigante = pygame.image.load(r"Python\Nivel 29 Reto 16\asteroide_gigante.png")
colision_img = pygame.image.load(r"Python\Nivel 29 Reto 16\colision.png")
nave = pygame.image.load(r"Python\Nivel 29 Reto 16\nave.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))


velocidad_asteroide_x = None
velocidad_asteroide_rotacion = None

#Funciones
def colision(asteroide_datos, asteroide, nave_x, nave_y, nave, margen_colision):
    if asteroide_datos[0] + asteroide.get_width() > nave_x-50 + margen_colision and \
    asteroide_datos[0] + margen_colision < nave_x-50 + nave.get_width() and \
    asteroide_datos[1] + asteroide.get_height() > nave_y-50 + margen_colision and \
    asteroide_datos[1] + margen_colision < nave_y-50 + nave.get_height():
        return True
    else:
        return False

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
pausa = False
colisionando = False

vidas = 3
nivel = 1

#Ventanas
inicio = True
jugando = False
final = False

ultima_posicion_nave_x = 590
ultima_posicion_nave_y = 610

while exe:

    while inicio:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exe = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jugando = True
                    inicio = False
                elif event.key == pygame.K_ESCAPE:
                    exe = False
                    inicio = False

        ventana.fill(negro)

        historia = ["               MISION ARMAGEDON",
                    "    La tripulación se encuentra en problemas",
                    "  Deben de atravesar el cinturon de asteroides",
                    "y llegar a la base de su planeta que esta siendo",
                    "     atacado por los aliens del planeta X",
                    "                                                 ",
                    "                            Presiona Enter para continuar...",
                    "                                              Esc para salir"]
    
        interlineado = 80
        for frase in historia:
            texto = fuente2.render(frase, True, blanco)
            ventana.blit(texto, (350, interlineado))
            interlineado += 80

        pygame.display.update()
    
    while jugando:

        #Asteroides
        asteroides_pequeños = []
        asteroides_grandes = []
        asteroides_gigantes = []

        for i in range(5*nivel):
            posicion_x, posicion_y = random.randint(0, 1280), random.randint(150, 450)
            velocidad_asteroide_x = random.randint(3, 4)
            velocidad_asteroide_rotacion = random.randint(1,360)
            asteroides_pequeños.append([posicion_x, posicion_y, velocidad_asteroide_x, velocidad_asteroide_rotacion])

        for i in range(2*nivel):
            posicion_x, posicion_y = random.randint(0, 1280), random.randint(150, 450)
            velocidad_asteroide_x = random.randint(1, 2)
            velocidad_asteroide_rotacion = random.randint(1,360)
            asteroides_grandes.append([posicion_x, posicion_y, velocidad_asteroide_x, velocidad_asteroide_rotacion])

        for i in range(1*nivel):
            posicion_x, posicion_y = random.randint(0, 1280), random.randint(150, 300)
            velocidad_asteroide_x = random.randint(1, 2)
            velocidad_asteroide_rotacion = random.randint(1, 360)
            asteroides_gigantes.append([posicion_x, posicion_y, velocidad_asteroide_x, velocidad_asteroide_rotacion])

        en_nivel = True
        nave_x = ultima_posicion_nave_x
        nave_y = ultima_posicion_nave_y

        while en_nivel:

            reloj.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exe = False
                    jugando = False
                    final = False
                    en_nivel = False
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

            texto_nivel = fuente2.render(f"Nivel: {nivel}", True, blanco)
            texto_vidas = fuente2.render(f"Vidas: {vidas}", True, blanco)

            ventana.blit(texto_nivel, (50, 50))
            ventana.blit(texto_vidas, (1150, 50))

            for asteroide in asteroides_pequeños:
                rotated_asteroide = pygame.transform.rotate(asteroide_pequeño, asteroide[3])
                rotated_asteroide_rect = rotated_asteroide.get_rect(center=(asteroide[0] + asteroide_pequeño.get_width() // 2, asteroide[1] + asteroide_pequeño.get_height() // 2))
                ventana.blit(rotated_asteroide, rotated_asteroide_rect.topleft)

                asteroide[0] += asteroide[2]
                asteroide[3] += 0.5

                if asteroide[0] > ancho:
                    asteroide[0] = -50
                
                if colision(asteroide, asteroide_pequeño, nave_x, nave_y, nave, 20):
                    explosion_x = nave_x - 50
                    explosion_y = nave_y - 50
                    pausa = True
                    break

            for asteroide in asteroides_grandes:
                rotated_asteroide = pygame.transform.rotate(asteroide_grande, asteroide[3])
                rotated_asteroide_rect = rotated_asteroide.get_rect(center=(asteroide[0] + asteroide_grande.get_width() // 2, asteroide[1] + asteroide_grande.get_height() // 2))
                ventana.blit(rotated_asteroide, rotated_asteroide_rect.topleft)

                asteroide[0] += asteroide[2]
                asteroide[3] += 0.5

                if asteroide[0] > ancho:
                    asteroide[0] = -100
                if colision(asteroide, asteroide_grande, nave_x, nave_y, nave, 20):
                    explosion_x = nave_x - 50
                    explosion_y = nave_y - 50
                    pausa = True
                    break

            for asteroide in asteroides_gigantes:
                rotated_asteroide = pygame.transform.rotate(asteroide_gigante, asteroide[3])
                rotated_asteroide_rect = rotated_asteroide.get_rect(center=(asteroide[0] + asteroide_gigante.get_width() // 2, asteroide[1] + asteroide_gigante.get_height() // 2))
                ventana.blit(rotated_asteroide, rotated_asteroide_rect.topleft)

                asteroide[0] += asteroide[2]
                asteroide[3] += 0.5

                if asteroide[0] > ancho:
                    asteroide[0] = -200

                if colision(asteroide, asteroide_gigante, nave_x, nave_y, nave, 20):
                    explosion_x = nave_x - 50
                    explosion_y = nave_y - 50
                    pausa = True
                    break
                    
            if pausa:
                ventana.blit(colision_img, (explosion_x, explosion_y))
                colisionando = True
                pausa = False

            if colisionando:
                nave_x = 590
                nave_y = 610
                vidas -= 1
                colisionando = False


            if vidas < 0:
                final = True
                exe = False
                jugando = False
                en_nivel = False

            if nave_y == -40:
                nivel += 1
                ultima_posicion_nave_x = nave_x
                ultima_posicion_nave_y = 700
                en_nivel = False

            if nivel == 4:
                final = True
                en_nivel = False
                jugando = False
            
            if not pausa and not colisionando:
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

        while final:

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exe = False
                        final = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            jugando = True
                            final = False
                            vidas = 3
                            nave_x = 590
                            nave_y = 610
                            angulo = 0
                            direccion = "arriba"
                            velocidad_x = 0
                            velocidad_y = 0
                            nivel = 1

                        elif event.key == pygame.K_ESCAPE:
                            exe = False
                            final = False

            if vidas >= 0:

                ventana.fill(negro)

                historia = ["                 Felicidades",
                            "    La tripulación se encuentra bien ahora",
                            "        Has logrado salvar a tu especie",
                            "                                                 ",
                            "                            Presiona Enter para continuar...",
                            "                                              Esc para salir"]
            
                interlineado = 80
                for frase in historia:
                    texto = fuente2.render(frase, True, blanco)
                    ventana.blit(texto, (350, interlineado))
                    interlineado += 80

                pygame.display.update()
            else:

                ventana.fill(negro)

                historia = ["                 GAME OVER",
                            "    No has conseguido llegar a tu planeta",
                            "        Tu especie fue asesinada por",
                            "                   ALIEN X                       ",
                            "                                                 ",
                            "                            Presiona Enter para continuar...",
                            "                                              Esc para salir"]
            
                interlineado = 80
                for frase in historia:
                    texto = fuente2.render(frase, True, blanco)
                    ventana.blit(texto, (350, interlineado))
                    interlineado += 80

            pygame.display.update()


pygame.quit()
