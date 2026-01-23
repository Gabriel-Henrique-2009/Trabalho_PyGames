import pygame
import time

pygame.init()
# CONFIGURAÇÕES DO BOTÃO 
botao_menu_teste = pygame.Rect(435, 453, 362, 110)
cor_botao_menu_teste = (0, 153, 102)
tela = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
rodando = True
estado_jogo = "MENU"


# CONFIGURAÇÕES DO TIRO
armazenar_tiro = []
velocidade_tiro = 10 
imagem_tiro = pygame.image.load("projetil-teste.png").convert_alpha() 
imagem_tiro = pygame.transform.scale(imagem_tiro, (25, 25))
vida_teste = 0
var_muni = 1
temposs = 0
carregando_tiro = False


# CONFIGURAÇÕES DO ATAQUE DO BOSS 
armazenar_tiro_boss = []
velocidade_tiro_boss = 7
imagem_atk_chatgpt = pygame.image.load("chatgptlogo.png").convert_alpha()


# CONFIGURAÇÕES GERAIS DO JOGO 
imagem = pygame.image.load("unnamed.jpg")
imagem = pygame.transform.scale(imagem, (1200, 800))
imagem = imagem.convert()

font = pygame.font.Font("Silkscreen-Regular.ttf", 36)

texto_surface_texto_frente = font.render("Jogar", True, (215, 238, 244))
texto_sombra = font.render("Jogar", True, (80, 123, 70))
texto_rect = texto_surface_texto_frente.get_rect(topleft=(540, 480))
texto_rect_sombra = texto_sombra.get_rect(topleft=(543,483))


# CONFIGURAÇÕES DOS PERSONAGENS
imagem_fundo = pygame.image.load("Gemini_Generated_Image_pgro94pgro94pgro.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 800))

imagem_alexandre_original = pygame.image.load("imagem-alexandre.png")
imagem_alexandre = pygame.transform.scale(imagem_alexandre_original, (267, 300))
imagem_alexandre_virado = pygame.transform.flip(imagem_alexandre, True, False)
imagem_alexandre_parado = pygame.image.load("alexandreparado.png")
imagem_alexandre_parado = pygame.transform.scale(imagem_alexandre_parado, (267, 300))

imagem_robo_original = pygame.image.load("imagem-robo.png")
imagem_robo = pygame.transform.scale(imagem_robo_original, (267, 300))


# CONFIGURAÇÕES DO SPRITE  
class jogador(pygame.sprite.Sprite):
    def __init__(self,img_parado2,img_parado3,img_ataque,img_pulo):
        super().__init__()
        self.frames_idle = [img_parado2,img_parado3]
        self.img_ataque = img_ataque
        self.index_animacao = 0
        self.image = self.frames_idle[self.index_animacao]
        self.rect = self.image.get_rect()
        self.img_pulo = img_pulo
        self.frames_ataque_restante = 0
        self.esquerda = False
        self.velocidade_animacao = 0.05

    def update(self,posicao_do_rect,olhando_para_esquerda):
        self.rect.topleft = posicao_do_rect
        self.esquerda = olhando_para_esquerda
        
        if self.frames_ataque_restante > 0:
            imagem_atual = self.img_ataque
            self.frames_ataque_restante -= 1 
        else:
            self.index_animacao += self.velocidade_animacao
            if self.index_animacao >= len(self.frames_idle):
                self.index_animacao = 0
            imagem_atual = self.frames_idle[int(self.index_animacao)]
        self.image = pygame.transform.flip(imagem_atual,self.esquerda,False)
        

# CONFIGURAÇÕES DOS PERSONAGENS
img_base = pygame.image.load("alexandreparado.png").convert_alpha()
img_base_2 = pygame.image.load("alexandre_transicao (1).png").convert_alpha()
img_base_3 = pygame.image.load("alexandre_transicao (2) (1).png").convert_alpha()

img_f2 = pygame.transform.scale(img_base_2, (277,310))
img_f3 = pygame.transform.scale(img_base_3, (267, 310))

img_atk_raw = pygame.image.load("imagem-alexandre.png").convert_alpha()
img_atk = pygame.transform.scale(img_atk_raw, (285,320))

img_pulo_raw = pygame.image.load("alexandrepulando.png")
img_pulo = pygame.transform.scale(img_pulo_raw,(267,310))


alexandre = jogador(img_f2,img_f3,img_atk,img_pulo)


grupo_jogador = pygame.sprite.GroupSingle(alexandre)

imagem_atual = imagem_alexandre_parado
player_rect = imagem_alexandre.get_rect()
enemy_rect = imagem_robo.get_rect()


# CONFIGURAÇÕES DAS VARIÁVEIS DO JOGO 
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


# LOOP DO JOGO
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_jogo == "MENU":
                if botao_menu_teste.collidepoint(evento.pos): 
                    estado_jogo = "JOGANDO"
                    vida_teste = 0

            elif estado_jogo == "JOGANDO":
                if evento.button == 1:
                    if var_muni == 1:
                        alexandre.frames_ataque_restante = 15 # velocidade do ataque(quando clica para atirar) IMPORTANTE
                        novo_tiro_rect = imagem_tiro.get_rect(center=player_rect.center)
                        direcao = -1 if virado_para_esquerda else 1 #logica de virar o tiro, com o script de antes eles(projeteis) iam somente para a direita  :)
                        armazenar_tiro.append({"rect": novo_tiro_rect, "dire": direcao}) # aqui tá guardando as info
                        var_muni -= 1

                    if var_muni == 0 and not carregando_tiro:
                        temposs = time.time()
                        carregando_tiro = True

                    if carregando_tiro and time.time() - temposs >= 1.0:
                        var_muni += 1
                        carregando_tiro = False
                        print("DEMOROU TROPINHAAAAAAA")


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando and estado_jogo == "JOGANDO":
                player_velocidade_y = velocidade_pulo
                pulando = True


        if estado_jogo == "MENU":
            tela.fill((200, 200, 200))
            tela.blit(imagem, (0,0))
            pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste) 
            tela.blit(texto_sombra, texto_rect_sombra) 
            tela.blit(texto_surface_texto_frente, texto_rect)


        elif estado_jogo == "JOGANDO":
            teclas = pygame.key.get_pressed()
        
            if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
                player_rect.x -= velocidade
                virado_para_esquerda = True

            if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]: 
                player_rect.x += velocidade
                virado_para_esquerda = False

            if player_rect.left < 0:
                player_rect.left = 0

            if player_rect.right > 1200:
                player_rect.right = 1200

            player_velocidade_y += gravidade
            player_rect.y += player_velocidade_y

            if player_rect.y >= 800 - player_rect.height:
                player_rect.y = 800 - player_rect.height
                pulando = False
                player_velocidade_y = 0

            if player_rect.colliderect(enemy_rect):
                print("Fim de jogo")
                rodando = False


        for tiro in armazenar_tiro:
            tiro["rect"].x += velocidade_tiro * tiro["dire"]
            if tiro["rect"].x > 1200 or tiro["rect"].x < 0:
                armazenar_tiro.remove(tiro)

            elif tiro["rect"].colliderect(enemy_rect):
                armazenar_tiro.remove(tiro)
                vida_teste_5 += 1
                print("OMYGODE VC ACERTOU O FUKING ROBO")


        if vida_teste >= 15: 
            print("UAU VC É INCRIVEL, VOCÊ GANHOU UM PUDIM! 🍮 ")
            estado_jogo = "MENU"
        

        tela.blit(imagem_fundo, (0,0))
        for tiro in armazenar_tiro:
            tela.blit(imagem_tiro, tiro["rect"])
        

        grupo_jogador.update(player_rect.topleft, virado_para_esquerda)
        grupo_jogador.draw(tela)    
        tela.blit(imagem_robo,enemy_rect)        
    pygame.display.update()
    clock.tick(60)
pygame.quit()