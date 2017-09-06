import pygame
from spriteSheetToList import *

class Fire(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../ArtResource/" + image +".png").convert_alpha()
        self.image = spriteSheetToList(self.image, 3)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.count = 0


    def animate(self):
        if self.count%30 == 0:
            self.image = self.image[self.count]
            self.count = 0
        self.count += 1