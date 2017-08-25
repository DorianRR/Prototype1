import pygame, math, sys
from Player import *

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Destructo-Spin!")
clock = pygame.time.Clock()
FPS = 60

player = Player("Temp.png")

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    player.update()
    screen.fill((0, 0, 0))
    player.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
