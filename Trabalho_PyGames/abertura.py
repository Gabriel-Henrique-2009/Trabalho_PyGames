import pygame

# att 3
pygame.init()

botao_menu_teste = pygame.Rect(435, 453, 362, 110)

cor_botao_menu_teste = (0, 153, 102)
tela = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
rodando = True


imagem = pygame.image.load("unnamed.jpg")
imagem = pygame.transform.scale(imagem, (1200, 800))
imagem = imagem.convert()
#essa linha tava conflitando com a imagem 
#essa tbm 

font = pygame.font.Font("Silkscreen-Regular.ttf", 36)

texto_surface_texto_frente = font.render("Jogar", True, (215, 238, 244))
texto_sombra = font.render("Jogar", True, (80, 123, 70)) # efeito de sombra igual tilulo 
texto_rect = texto_surface_texto_frente.get_rect(topleft=(540, 480)) #certinho rs
texto_rect_sombra = texto_sombra.get_rect(topleft=(543,483))

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
         if botao_menu_teste.collidepoint(evento.pos): # o collidepoint verifica se o mouse está sobre o botão.
             #ele tbm evita ter que ficar fazendo conta da posição do mouse :) 
             print("botão teste foi clicado , iniciar o game")
            # Eduardo, aqui que a gnt vai ter que fazer o nosso jogo msm, né? eu coloquei só o botão de jgr. Acho bom fazer o jogo em um outro arquivo e depois, só passar pra cá

    mouse_pos = pygame.mouse.get_pos()

    tela.fill((200, 200, 200))
    tela.blit(imagem, (0,0))
    pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste) #Man se quiser ver o texto sem o sistema de colisão
    #do mouse é só tirar essa linha 
    # e o hitbox funciona ainda rs
    tela.blit(texto_sombra, texto_rect_sombra) 
    tela.blit(texto_surface_texto_frente, texto_rect)
    
    pygame.display.update()

    clock.tick(60)










pygame.quit()
