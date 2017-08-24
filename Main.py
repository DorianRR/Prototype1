import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Destructo-Spin!")

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()