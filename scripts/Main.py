import pygame, math, sys
from Player import *
from SimpleUI import *
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
    #keep these two lines of code after any screen.blit() bacause we want texts appear above everything#
    screen.blit(uicreate(player)[0], [20, 20])                                                          #
    screen.blit(uicreate(player)[1], [654, 20])                                                         #
    player.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
