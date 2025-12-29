import pygame

# att 1
pygame.init()

botao_menu_teste = pygame.Rect(500, 350, 200, 100)
cor_botao_menu_teste = (255, 0, 0)
tela = pygame.display.set_mode((1200, 800))
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
         if botao_menu_teste.collidepoint(evento.pos): # o collidepoint verifica se o mouse está sobre o botão.
             #ele tbm evita ter que ficar fazendo conta da posição do mouse :) 
             print("botão teste foi clicado iniciar o game")

    mouse_pos = pygame.mouse.get_pos()

    if botao_menu_teste.collidepoint(mouse_pos):
        cor_botao_menu_teste = (0, 255, 0)
    else:
        cor_botao_menu_teste = (255, 0, 0)


    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste)
    pygame.display.update()

    pygame.time.Clock().tick(60)













    
pygame.quit()
