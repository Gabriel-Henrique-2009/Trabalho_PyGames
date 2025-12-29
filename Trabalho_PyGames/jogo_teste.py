import pygame

# att 1
pygame.init()

tela = pygame.display.set_mode((1200, 800))
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)

    tela.fill((0, 0, 0))
    pygame.display.update()

    pygame.time.Clock().tick(60)
pygame.quit()
