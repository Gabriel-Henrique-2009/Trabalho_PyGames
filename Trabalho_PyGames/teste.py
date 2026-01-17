import pygame

pygame.init()

botao_menu_teste = pygame.Rect(435, 453, 362, 110)

cor_botao_menu_teste = (0, 153, 102)
tela = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
rodando = True
estado_jogo = "MENU"

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

# VOU TENTAR COLOCAR O JOGO A PARTIR DAQUI :)

imagem_fundo = pygame.image.load("Gemini_Generated_Image_pgro94pgro94pgro.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 800))

imagem_alexandre_original = pygame.image.load("imagem-alexandre.png")
imagem_alexandre = pygame.transform.scale(imagem_alexandre_original, (267, 300))
imagem_alexandre_virado = pygame.transform.flip(imagem_alexandre, True, False)

imagem_robo_original = pygame.image.load("imagem-robo.png")
imagem_robo = pygame.transform.scale(imagem_robo_original, (267, 300))

player_rect = imagem_alexandre.get_rect()
enemy_rect = imagem_robo.get_rect()

player_rect.x = 100
player_rect.y = 800 - player_rect.height 

enemy_rect.x = 800
enemy_rect.y = 800 - enemy_rect.height

velocidade = 5
gravidade = 0.5
velocidade_pulo = -15     
player_velocidade_y = 0
pulando = False
virado_para_esquerda = False

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # # o collidepoint verifica se o mouse está sobre o botão.
            # #ele tbm evita ter que ficar fazendo conta da posição do mouse :) 
            # # Eduardo, aqui que a gnt vai ter que fazer o nosso jogo msm, né? eu coloquei só o botão de jgr. Acho bom fazer o jogo em um outro arquivo e depois, só passar pra cá
            if botao_menu_teste.collidepoint(evento.pos): 
                estado_jogo = "JOGANDO"
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando and estado_jogo == "JOGANDO":
                player_velocidade_y = velocidade_pulo
                pulando = True

    if estado_jogo == "MENU":
        tela.fill((200, 200, 200))
        tela.blit(imagem, (0,0))
        pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste) #Man se quiser ver o texto sem o sistema de colisão
        #do mouse é só tirar essa linha 
        # e o hitbox funciona ainda rs
        tela.blit(texto_sombra, texto_rect_sombra) 
        tela.blit(texto_surface_texto_frente, texto_rect)

    elif estado_jogo == "JOGANDO":
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_a]:
            player_rect.x -= velocidade
            virado_para_esquerda = True
        if teclas[pygame.K_d]:
            player_rect.x += velocidade
            virado_para_esquerda = False

        player_velocidade_y += gravidade
        player_rect.y += player_velocidade_y

        if player_rect.y >= 800 - player_rect.height:
            player_rect.y = 800 - player_rect.height
            pulando = False
            player_velocidade_y = 0

        if player_rect.colliderect(enemy_rect):
            print("Fim de jogo")
            rodando = False

        tela.blit(imagem_fundo, (0, 0))
        
        if virado_para_esquerda:
            tela.blit(imagem_alexandre_virado, player_rect)
        else:
            tela.blit(imagem_alexandre, player_rect)
            
        tela.blit(imagem_robo, enemy_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()