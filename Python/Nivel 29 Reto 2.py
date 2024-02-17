import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600))

ventana.fill((200, 136, 45))

pygame.display.update()

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                jugando = False

    ventana.fill((76, 200, 121))
    pygame.display.update()


pygame.quit()