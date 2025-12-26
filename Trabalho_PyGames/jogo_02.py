import pygame

pygame.init()
janela = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
quadrado = pygame.Surface([30, 30])
quadrado.fill((0, 0, 0))
y = 50
x = 50       	# coordenada x do quadrado
velocidade = 8   # velocidade de movimentação do quadrado

while True:
  for event in pygame.event.get():   	# detecta a ocorrência de um evento
    if event.type == pygame.QUIT:    	# para tratar o evento de fechamento da janela
      pygame.quit()                  	# encerra o programa
 
  teclas = pygame.key.get_pressed() # Para capturar o pressionamento das teclas de forma contínua
  if teclas[pygame.K_LEFT]:   # tecla direcional esquerda está sendo pressionada?
    x = x - velocidade
  if teclas[pygame.K_RIGHT]:  # tecla direcional direita está sendo pressionada?
    x = x + velocidade
  if teclas[pygame.K_UP]:  # tecla direcional direita está sendo pressionada?
    y = y - velocidade
  if teclas[pygame.K_DOWN]:  # tecla direcional direita está sendo pressionada?
    y = y + velocidade
  if teclas[pygame.K_a]:   # tecla direcional esquerda está sendo pressionada?
    x = x - velocidade
  if teclas[pygame.K_d]:  # tecla direcional direita está sendo pressionada?
    x = x + velocidade
  if teclas[pygame.K_w]:  # tecla direcional direita está sendo pressionada?
    y = y - velocidade
  if teclas[pygame.K_s]:  # tecla direcional direita está sendo pressionada?
    y = y + velocidade
 	 
  janela.fill((255, 255, 255))
  janela.blit(quadrado, (x, y))
  pygame.display.flip()
  clock.tick(60)
