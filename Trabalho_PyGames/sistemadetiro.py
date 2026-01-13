import pygame
import random 
pygame.init()

botao_menu_teste = pygame.Rect(435, 453, 362, 110)

cor_botao_menu_teste = (0, 153, 102)
tela = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
rodando = True
estado_jogo = "MENU"

#sistema de tiro eduardo computaria

armazenar_tiro = []
velocidade_tiro = 10 #qualquer coisa tu muda
imagem_tiro = pygame.image.load("projetil-teste.png").convert_alpha() #tirar o fundo do png maldito 😒
imagem_tiro = pygame.transform.scale(imagem_tiro, (25, 25))
vida_teste_5 = 0
###








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

imagem_alexandre = pygame.image.load("Trabalho_PyGames/imagem-alexandre.png")
imagem_robo = pygame.image.load("Trabalho_PyGames/imagem-robo.png")

imagem_alexandre = pygame.transform.scale(imagem_alexandre, (60, 60))
imagem_robo = pygame.transform.scale(imagem_robo, (60, 60))

player_rect = imagem_alexandre.get_rect()
enemy_rect = imagem_robo.get_rect()

player_rect.x = 100
player_rect.y = 100

enemy_rect.x = 400
enemy_rect.y = 300

velocidade = 5
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #  # o collidepoint verifica se o mouse está sobre o botão.
            #  #ele tbm evita ter que ficar fazendo conta da posição do mouse :) 
            # # Eduardo, aqui que a gnt vai ter que fazer o nosso jogo msm, né? eu coloquei só o botão de jgr. Acho bom fazer o jogo em um outro arquivo e depois, só passar pra cá
            if botao_menu_teste.collidepoint(evento.pos): 
                 estado_jogo = "JOGANDO"
                 vida_teste_5 = 0
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and estado_jogo == "JOGANDO": #tecla de espaço para teste, qualquer coisa nós mudamos dps
                novo_tiro = imagem_tiro.get_rect(center=player_rect.center)
                armazenar_tiro.append(novo_tiro)
        
            

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
        if teclas[pygame.K_LEFT]:
            player_rect.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            player_rect.x += velocidade
        if teclas[pygame.K_UP]:
            player_rect.y -= velocidade
        if teclas[pygame.K_DOWN]:
            player_rect.y += velocidade

        if player_rect.colliderect(enemy_rect):
            print("Fim de jogo")
            rodando = False
        for tiro in armazenar_tiro:
            tiro.x += velocidade_tiro
            if tiro.x > 1200:
                armazenar_tiro.remove(tiro)
            elif tiro.colliderect(enemy_rect):
                armazenar_tiro.remove(tiro)
                vida_teste_5 += 1
                print("OMYGODE VC ACERTOU O FUKING ROBO")
                
        
            
        if vida_teste_5 >= 5:
            print("UAU VC É INCRIVEL, VOCÊ GANHOU UM PUDIM! 🍮 ")
            estado_jogo = "MENU" #para voltar no menu

        tela.fill((255, 255, 255))
        for tiro in armazenar_tiro:
            tela.blit(imagem_tiro,tiro)

    
        tela.blit(imagem_alexandre, player_rect)
        tela.blit(imagem_robo, enemy_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()