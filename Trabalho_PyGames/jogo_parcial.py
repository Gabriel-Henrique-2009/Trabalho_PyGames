import pygame
import time

pygame.init()

botao_menu_teste = pygame.Rect(435, 453, 362, 110)
cor_botao_menu_teste = (0, 153, 102)
tela = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
rodando = True
estado_jogo = "MENU"


vermelho_fundo = (128, 36, 36)
vermelho = (216, 0, 0)
verde = (0, 153, 102)
branco = (255, 255, 255)


fonte_contagem = pygame.font.Font("Silkscreen-Regular.ttf", 100)
fonte_vitoria = pygame.font.Font("Silkscreen-Regular.ttf", 110)
contagem = 3
contagem_final = 0


tempo_inicio_vitoria = 0
posicao_y_vitoria = 850
imagem_vitoria = pygame.image.load("alexandrevitoria2.png").convert_alpha()
imagem_vitoria = pygame.transform.scale(imagem_vitoria,(500,500))

armazenar_tiro = []
velocidade_tiro = 10 
imagem_tiro = pygame.image.load("projetil-teste.png").convert_alpha() #tirar o fundo do png maldito 😒
imagem_tiro = pygame.transform.scale(imagem_tiro, (25, 25))
vida_teste = 10
vida_player = 3
tempo_imunidade_player = 0
var_muni = 1
temposs = 0
carregando_tiro = False

tempo_ultimo_tiro_player = 0
intervalo_tiro_player = 1.2


#sistema de atk do boss 
armazenar_tiro_boss = []
velocidade_tiro_boss = 7
imagem_atk_chatgpt = pygame.image.load("chatgptlogo.png").convert_alpha()
imagem_atk_chatgpt = pygame.transform.scale(imagem_atk_chatgpt,(40, 40)) # deixei maior que o tiro do jogador para intimidar kkkkkkk
tempo_ultimo_tiro_robo = 0
intervalo_dos_tiro = 1.5
vida_boss_max = 2 #VIDA BOSS
vida_teste_5 = 0
###

imagem = pygame.image.load("unnamed.png")
imagem = pygame.transform.scale(imagem, (1200, 800))
imagem = imagem.convert()
#essa linha tava conflitando com a imagem 
#essa tbm 
fase1 = "round 1"
fase2 = "round 2"
fase3 = "round 3"
fase4 = "round 4"
fase5 = "round 5"
usando = fase1
modo_vitoria = 1


font = pygame.font.Font("Silkscreen-Regular.ttf", 36)

texto_surface_texto_frente = font.render("Jogar", True, (215, 238, 244))
texto_rect = texto_surface_texto_frente.get_rect(topleft=(540, 480)) #certinho rs
texto_sombra = font.render("Jogar", True, (80, 123, 70)) # efeito de sombra igual tilulo 
texto_rect_sombra = texto_sombra.get_rect(topleft=(543,483))


# TEXTO DO MENU DOIS
texto_surface_texto_frente2 = font.render("Continuar", True, (215, 238, 244))
texto_rect2 = texto_surface_texto_frente2.get_rect(topleft=(492, 455))
texto_sombra2 = font.render("Continuar", True, (80, 123, 70))
texto_rect_sombra2 = texto_sombra2.get_rect(topleft=(495,458))

texto_fase = font.render(usando, True, (215, 238, 244))
texto_rect_fase = texto_fase.get_rect(topleft=(516, 505))
texto_fase_sombra = font.render(usando, True, (80, 123, 70))
estado_jogo = "MENU"
texto_rect_fase_sombra = texto_fase_sombra.get_rect(topleft=(519,508))


texto_gameover_titulo = fonte_contagem.render("Você perdeu", True, (255, 0, 0))
texto_rect_gameover_titulo = texto_gameover_titulo.get_rect(center=(600, 300))
texto_retry = font.render("Tentar Novamente", True, (215, 238, 244))
texto_rect_retry = texto_retry.get_rect(center=(616, 508))
texto_retry_sombra = font.render("Tentar Novamente", True, (80, 123, 70))
texto_rect_retry_sombra = texto_retry_sombra.get_rect(center=(619, 511))


# VOU TENTAR COLOCAR O JOGO A PARTIR DAQUI :)

imagem_fundo = pygame.image.load("Gemini_Generated_Image_pgro94pgro94pgro.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 800))

imagem_alexandre_original = pygame.image.load("imagem-alexandre.png")
imagem_alexandre = pygame.transform.scale(imagem_alexandre_original, (267, 300))
imagem_alexandre_virado = pygame.transform.flip(imagem_alexandre, True, False)

imagem_alexandre_parado = pygame.image.load("alexandreparado.png")
imagem_alexandre_parado = pygame.transform.scale(imagem_alexandre_parado, (267, 300))


imagem_robo_original = pygame.image.load("imagem_roboparado.png")
imagem_robo = pygame.transform.scale(imagem_robo_original, (267, 300))
class jogador(pygame.sprite.Sprite):
    def __init__(self,img_parado2,img_parado3,img_ataque,img_pulo):
        super().__init__()
        self.frames_idle = [img_parado2,img_parado3]
         #(idle é o nome da animacao de ficar parado e tals)
        self.img_ataque = img_ataque
        self.img_pulo = img_pulo
        self.index_animacao = 0
        self.image = self.frames_idle[self.index_animacao]
        self.rect = self.image.get_rect()
        self.frames_ataque_restante = 0
        self.esquerda = False
        self.velocidade_animacao = 0.05 #ajuste de velocidade da animação IMPORTANTE 

    def update(self,posicao_do_rect,olhando_para_esquerda,pulando,):
        self.rect.topleft = posicao_do_rect
        self.esquerda = olhando_para_esquerda
        
        if self.frames_ataque_restante > 0:
            imagem_atual = self.img_ataque
            self.frames_ataque_restante -= 1 
        elif pulando:
            imagem_atual = self.img_pulo
        else:
            self.index_animacao += self.velocidade_animacao
            if self.index_animacao >= len(self.frames_idle):
                self.index_animacao = 0
            imagem_atual = self.frames_idle[int(self.index_animacao)]
        self.image = pygame.transform.flip(imagem_atual,self.esquerda,False)

class boss(pygame.sprite.Sprite):
    def __init__(self,img_base_boss, img_atk_boss):
       super().__init__()
    # 
       self.img_idle = img_base_boss
       self.img_atk = img_atk_boss
       self.image = self.img_idle
       self.index_animacao = 0
       self.frames_atk_total = 30
       self.rect = self.image.get_rect()
       self.atacando = False
       self.frame_atk = 0
       self.disparo_feito = False
       self.ultimo_ataque = 0
    def update(self,posicao_do_rect,intervalo_tiro):
        self.rect.topleft = posicao_do_rect
        agora = time.time()
        
        if not self.atacando and agora - self.ultimo_ataque >= intervalo_tiro:
            self.atacando = True
            self.frame_atk = 0
            self.ultimo_ataque = agora
            self.disparo_feito = False
        if self.atacando:
            self.image = self.img_atk
            self.frame_atk += 1
            if self.frame_atk == 15 and not self.disparo_feito:
                self.disparo_feito = True
                return True
            if self.frame_atk >= self.frames_atk_total:
                self.atacando = False
        else:
            self.image = self.img_idle
        return False

def barravida_player (vida, x, y):
    proporcao = vida/3
    pygame.draw.rect(tela, branco, (x-2, y-2, 404, 34))
    pygame.draw.rect(tela, vermelho_fundo, (x, y, 400, 30))
    pygame.draw.rect(tela, verde, (x, y, 400 * proporcao, 30))
    return

def barravida_boss (vida_atual, vida_maxima, x, y):
    proporcao = (vida_maxima - vida_atual) / vida_maxima
    proporcao = max(0, min(proporcao, 1))
    largura_verde = 400 * proporcao
    pygame.draw.rect(tela, branco, (x-2, y-2, 404, 34))
    pygame.draw.rect(tela, vermelho_fundo, (x, y, 400, 30))
    x_invertido = x + (400 - largura_verde)
    pygame.draw.rect(tela, vermelho, (x_invertido, y, largura_verde, 30)) # Para a barra diminuir da esquerda para a direita
    return



img_base = pygame.image.load("alexandreparado.png").convert_alpha()
img_base_2 = pygame.image.load("alexandre_transicao (1).png").convert_alpha()
img_base_3 = pygame.image.load("alexandre_transicao (2) (1).png").convert_alpha()

img_f2 = pygame.transform.scale(img_base_2, (277,310))
img_f3 = pygame.transform.scale(img_base_3, (267, 310))

img_atk_raw = pygame.image.load("imagem-alexandre.png").convert_alpha()
img_atk = pygame.transform.scale(img_atk_raw, (285,320))  

img_pulo_raw = pygame.image.load("alexandrepulando.png")
img_pulo = pygame.transform.scale(img_pulo_raw,(267,310))

img_base_boss = pygame.image.load("imagem_roboparado.png").convert_alpha()
img_base_boss = pygame.transform.scale(img_base_boss,(267, 310))
img_atk_boss = pygame.image.load("imagem_roboatk.png").convert_alpha()
img_atk_boss = pygame.transform.scale(img_atk_boss,(277,300))

alexandre = jogador(img_f2,img_f3,img_atk,img_pulo)
grupo_jogador = pygame.sprite.GroupSingle(alexandre)
robo = boss(img_base_boss,img_atk_boss)
grupo_boss = pygame.sprite.GroupSingle(robo)

imagem_atual = imagem_alexandre_parado

player_rect = imagem_alexandre.get_rect()
enemy_rect = imagem_robo.get_rect()

player_rect.x = 100
player_rect.y = 800 - player_rect.height 

enemy_rect.x = 800
enemy_rect.y = 800 - enemy_rect.height

velocidade = 5
gravidade = 0.5
velocidade_pulo = -17
player_velocidade_y = 0
pulando = False
virado_para_esquerda = False

#frames = 0
# testando as sprites da aula, fala ai oq tu achou man

robo.rect.topleft = enemy_rect.topleft


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # # o collidepoint verifica se o mouse está sobre o botão.
            # #ele tbm evita ter que ficar fazendo conta da posição do mouse :) 
            # # Eduardo, aqui que a gnt vai ter que fazer o nosso jogo msm, né? eu coloquei só o botão de jgr. Acho bom fazer o jogo em um outro arquivo e depois, só passar pra cá
    
            if estado_jogo in ["MENU","MENU2", "GAME_OVER"]:
                if botao_menu_teste.collidepoint(evento.pos):
            # Só muda a fase aqui, quando o botão for clicado!
               #     if usando == fase2:
              #          usando = fase3
               #     elif usando == fase4:
               #         usando = fase5
                    estado_jogo = "COUNTDOWN"
                    contagem_final = time.time()
                    contagem = 3
                    vida_teste_5 = 0
                    vida_player = 3
                    player_rect.x = 100
                    player_rect.y = 800 - player_rect.height
                    pulando = False
                    player_velocidade_y = 0
                    virado_para_esquerda = False
                    armazenar_tiro.clear()
                    armazenar_tiro_boss.clear()
                    posicao_y_vitoria = 800

                    texto_fase = font.render(usando, True, (215, 238, 244))
                    texto_fase_sombra = font.render(usando, True, (80, 123, 70))
                    
            elif estado_jogo == "JOGANDO":
                if evento.button == 1:
                    agora_tiro = time.time()
                    if agora_tiro - tempo_ultimo_tiro_player >= intervalo_tiro_player:
                        if var_muni > 0:
                            tempo_ultimo_tiro_player = agora_tiro
                            alexandre.frames_ataque_restante = 15 # velocidade do ataque(quando clica para atirar) IMPORTANTE
                            novo_tiro_rect = imagem_tiro.get_rect(center=player_rect.center)
                            direcao = -1 if virado_para_esquerda else 1 #logica de virar o tiro, com o script de antes eles(projeteis) iam somente para a direita  :)
                            armazenar_tiro.append({"rect": novo_tiro_rect, "dire": direcao}) # aqui tá guardando as info
                            var_muni -= 1
                            if var_muni <= 5: 
                                outr = 5
                                var_muni += 5
                                print("somou")

                    if var_muni == 0 and not carregando_tiro:
                        temposs = time.time()
                        carregando_tiro = True

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando and estado_jogo == "JOGANDO":
                player_velocidade_y = velocidade_pulo
                pulando = True

    if estado_jogo == "JOGANDO" and carregando_tiro:
        if time.time() - temposs >= 1.0:
            var_muni += 1
            carregando_tiro = False
            print("DEMOROU TROPINHAAAAAAA")

    if estado_jogo == "MENU":
        tela.fill((200, 200, 200))
        tela.blit(imagem, (0,0))
        pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste)

        tela.blit(texto_sombra, texto_rect_sombra) 
        tela.blit(texto_surface_texto_frente, texto_rect)

    elif estado_jogo == "MENU2":
        tela.fill((200, 200, 200))
        tela.blit(imagem, (0,0))
        pygame.draw.rect(tela, cor_botao_menu_teste, botao_menu_teste)

        tela.blit(texto_sombra2, texto_rect_sombra2) 
        tela.blit(texto_surface_texto_frente2, texto_rect2)

        tela.blit(texto_fase_sombra, texto_rect_fase_sombra) 
        tela.blit(texto_fase, texto_rect_fase)

    elif estado_jogo == "GAME_OVER":
        tela.blit(imagem_fundo, (0,0))
        grupo_jogador.draw(tela)    
        grupo_boss.draw(tela)
        barravida_player(vida_player,20, 40)
        barravida_boss(vida_teste_5,vida_boss_max,780,40)

        overlay = pygame.Surface((1200,800))
        overlay.set_alpha(150)
        overlay.fill((0,0,0))
        tela.blit(overlay, (0,0))

        tela.blit(texto_gameover_titulo,texto_rect_gameover_titulo)
    
        tela.blit(texto_retry_sombra,texto_rect_retry_sombra)
        tela.blit(texto_retry,texto_rect_retry)

    elif estado_jogo == "COUNTDOWN":
            tela.blit(imagem_fundo, (0,0))
            grupo_jogador.update(player_rect.topleft, virado_para_esquerda, pulando) #draw/upd
            grupo_jogador.draw(tela)    
            grupo_boss.draw(tela)


            overlay = pygame.Surface((1200,800))
            overlay.set_alpha(150)
            overlay.fill((0,0,0))
            tela.blit(overlay, (0,0))


            tempo_atual = time.time()
            if tempo_atual - contagem_final >= 1.0:
                contagem -= 1
                contagem_final = tempo_atual

            if contagem > 0:
                texto_num = fonte_contagem.render(str(contagem),True,(255,255,255))
                rect_num = texto_num.get_rect(center=(600,400))
                tela.blit(texto_num,rect_num)
            else:
                estado_jogo = "JOGANDO"
                
    elif estado_jogo == "JOGANDO":
        teclas = pygame.key.get_pressed()
        
        tempo_atual = time.time()
        disparo = robo.update(robo.rect.topleft,intervalo_dos_tiro)
     
   
            
        
            
        
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
            # limite de borda :)

        player_velocidade_y += gravidade
        player_rect.y += player_velocidade_y

        if player_rect.y >= 800 - player_rect.height:
            player_rect.y = 800 - player_rect.height
            pulando = False
            player_velocidade_y = 0

        # if player_rect.colliderect(enemy_rect):
        #     print("colidiu com a ia e morreu 🙏😫💔")
        #     rodando = False

        if disparo:
            direcao = -1 if player_rect.centerx < robo.rect.centerx else 1
            novo_tiro = imagem_atk_chatgpt.get_rect(center=robo.rect.center)
            armazenar_tiro_boss.append({"rect": novo_tiro,"dire": direcao})

        for tiro in armazenar_tiro[:]:
            tiro["rect"].x += velocidade_tiro * tiro["dire"]
            if tiro["rect"].colliderect(robo.rect):
                armazenar_tiro.remove(tiro)
                vida_teste_5 += 1
                print("Acertou o Boss!")
            elif tiro["rect"].right < 0 or tiro["rect"].left > 1200:
                armazenar_tiro.remove(tiro)
        for tiro in armazenar_tiro_boss[:]:
            rect_tiro = tiro["rect"]
            rect_tiro.x += velocidade_tiro_boss * tiro["dire"]
            if rect_tiro.right < 0 or rect_tiro.left > 1200:
                armazenar_tiro_boss.remove(tiro)
            elif rect_tiro.colliderect(player_rect):
                armazenar_tiro_boss.remove(tiro)
                if time.time() - tempo_imunidade_player > 1.0:
                    vida_player -= 1
                    tempo_imunidade_player = time.time()
                    print(f"VC tomou um tiro da IA sigma 🤣🤣, vidas restantes: {vida_player}")
        # if player_rect.colliderect(enemy_rect) and time.time() - tempo_imunidade_player:
        #     vida_player -= 1
        #     tempo_imunidade_player = time.time()

        

      #  if usando == fase5:
       #     modo_vitoria += 1
            
        # sistema de tiro ajustado 
        if vida_teste_5 >= vida_boss_max: #alterar vida do boss # IF MALDITO PPRRT
            print("MOGOU A IA BETA")  
            if usando == fase5:
                tempo_inicio_vitoria = time.time()
                estado_jogo = "VITORIA"
            else:
                if usando == fase1:
                    velocidade_tiro_boss = 8
                    intervalo_dos_tiro = 1.5
                    usando = fase2
                    vida_boss_max = 5 # Exemplo de aumento de vida por fase
                elif usando ==  fase2:
                    velocidade_tiro_boss = 12
                    intervalo_dos_tiro = 1.4
                    usando = fase3
                    vida_boss_max = 8
                elif usando == fase3:
                    velocidade_tiro_boss = 16
                    intervalo_dos_tiro = 1.3
                    usando = fase4
                    vida_boss_max = 12
                elif usando == fase4:
                    velocidade_tiro_boss = 18
                    intervalo_dos_tiro = 1.2
                    usando = fase5
                    vida_boss_max = 20

                texto_fase = font.render(usando,  True,(215,238,244))
                texto_fase_sombra = font.render(usando,True,(80,123,70))
                estado_jogo = "MENU2"
            vida_teste_5 = 0
            armazenar_tiro.clear()
            armazenar_tiro_boss.clear()

        if vida_player <= 0:
            print("VC foi mogado pela IA sigma 🤣🤣🤣")
            print("tenta dnv beta 🤦‍♂️")
            estado_jogo = "GAME_OVER"
        
        tela.blit(imagem_fundo, (0,0))
        for tiro in armazenar_tiro:
            tela.blit(imagem_tiro, tiro["rect"])
        for tiro2 in armazenar_tiro_boss:
            tela.blit(imagem_atk_chatgpt, tiro2["rect"])

        grupo_jogador.update(player_rect.topleft, virado_para_esquerda, pulando)
        grupo_jogador.draw(tela)    

        grupo_boss.draw(tela)
       
        
        barravida_player(vida_player, 20, 40)
        barravida_boss(vida_teste_5, vida_boss_max, 780, 40) # Passando a variável vida_boss_max aqui
        

    elif estado_jogo == "VITORIA":
        tela.blit(imagem_fundo, (0,0))
        grupo_jogador.draw(tela)
        grupo_boss.draw(tela)

        overlay = pygame.Surface((1200,800))
        overlay.set_alpha(180)
        overlay.fill((0,0,0))
        tela.blit(overlay, (0,0))
        tempo_passado = time.time() - tempo_inicio_vitoria
        if tempo_passado < 3.0:
            txt_parabens = fonte_vitoria.render("PARABÉNS!",True,(255, 255, 255)) 
            rect_parabens = txt_parabens.get_rect(center=(600, 400)) 
            tela.blit(txt_parabens,rect_parabens)

        elif 3.0 <= tempo_passado <= 6.0:
            progresso_subida = (tempo_passado - 3.0) / 3.0
            posicao_y_vitoria = 1100 - (750 *progresso_subida)
            rect_vitoria = imagem_vitoria.get_rect(center=(600,int(posicao_y_vitoria)))
            tela.blit(imagem_vitoria,rect_vitoria)

        elif 6.0 < tempo_passado <10.0:
            rect_vitoria = imagem_vitoria.get_rect(center=(600,400))
            tela.blit(imagem_vitoria,rect_vitoria)

        if tempo_passado >= 10.0:
            estado_jogo = "MENU"  
            usando = fase1     
            vida_teste_5 = 0

    pygame.display.update()
    clock.tick(60)
pygame.quit()