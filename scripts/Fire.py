import pygame

class Fire(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../ArtResource/" + image +".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position


    def animate(self):
        