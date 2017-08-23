import pygame

pygame.init()
SCREEN_SIZE = (1024,1024)
from pygame.locals import *
#import local parameters
screen_1 = [0]*6
print(screen_1)

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
#screen = pygame.display.set_mode((640, 480), 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.update()

    #test


