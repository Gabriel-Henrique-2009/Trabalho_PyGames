# Vou fazer o sistema do jogo aqui msm, eduardo
# tipoman, ficou meio paia mas é só pra ver msm. dps a gnt concerta
import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

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

rodando = True
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

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

    tela.fill((255, 255, 255))
    tela.blit(imagem_alexandre, player_rect)
    tela.blit(imagem_robo, enemy_rect)
    pygame.display.update()

pygame.quit()
exit()

