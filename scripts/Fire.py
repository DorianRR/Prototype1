import pygame


class Fire(pygame.sprite.Sprite):

    def __init__(self, position, filename):

        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.image.load("../Animation/" + filename + ".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)