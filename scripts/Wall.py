import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
