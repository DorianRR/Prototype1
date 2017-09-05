import pygame

class Flame(pygame.sprite.Sprite):

    def __init__(self, image, position):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(".../ArtResource/" + image +".png")