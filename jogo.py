import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True

y = 372
x = 47
w = 47
z = 47
vel1 = 3
vel2 = -3
font = pygame.font.Font(None, 24)
surface_texto = font.render(f"Slk 😱😰", True, 'black')
a = (640 // 2) - surface_texto.get_width() // 2
b = (480 // 2) - surface_texto.get_height() // 2
mostrar_txt = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

      # apaga o quadro atual
  screen.fill((0, 150, 255))

  # Lógica de jogo e renderização do novo quadro
  # cria uma superfície quadrada com 30 pixels de lado
  figura1 = pygame.Surface([30, 30])
  figura2 = pygame.Surface([30, 30])
  figura3 = pygame.Surface([30, 30])
  figura4 = pygame.Surface([30, 30])
  

  # preenche a superfície com cor preta
  figura1.fill((0, 0, 0)) 
  figura2.fill((0, 74, 173)) 
  figura3.fill((255, 0, 255))
  figura3.fill((0, 255, 0))


  # desenha figura sobre o quadro atual nas coordenadas indicadas
  screen.blit(figura1, (x, x))
  screen.blit(figura2, (y, x))
  screen.blit(figura3, (w, 320))
  screen.blit(figura4, (320, z))

  # avança 3 pixels a cada quadro
  y = y + vel2
  if y >= 610 or y <= 0:
    vel2 *= -1

  x = x + vel1 
  if x >= 610 or x <= 0:
    vel1 *= -1

  w = w + vel1 
  if w >= 610 or w <= 0:
    vel1 *= -1

  z = z + vel1 
  if z >= 610 or z <= 0:
    vel1 *= -1
    

  if x >= 320:
    mostrar_txt = True
  else:
    mostrar_txt = False


  if mostrar_txt:
    screen.blit(surface_texto, (a, b))

# Desenha o quadro atual na tela
  pygame.display.flip() 
  clock.tick(60)

pygame.quit()