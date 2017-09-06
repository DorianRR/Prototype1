import pygame
from spriteSheetToList import *

class Fire(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../ArtResource/" + image +".png").convert_alpha()
        self.image = spriteSheetToList(self.image, 4)
        self.rect = self.image[0].get_rect()
        self.rect.topleft = position
        self.count = 0
        self.imageCount = 0


    def animate(self):
        if self.count%10 == 0:
            self.imageCount += 1
            self.count = 0
            if self.imageCount > 2:
                self.imageCount = 0
        self.count += 1

    def draw(self, screen):
        screen.blit(self.image[self.imageCount], self.rect)
