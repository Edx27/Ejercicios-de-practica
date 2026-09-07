import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Eduardo Rodriguez")

fuente = pygame.font.SysFont(None, 40)
texto = fuente.render("Eduardo Rodriguez", True, (255, 255, 255))
rect_texto = texto.get_rect(center=(300, 200))

ejecutando = True
while ejecutando:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      ejecutando = False

  pantalla.fill((0, 0, 0))
  pantalla.blit(texto, rect_texto)
  pygame.display.flip()

pygame.quit()
