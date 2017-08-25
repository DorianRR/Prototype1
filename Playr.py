import pygame

class Player:
    def __init__(self):

        self.rotationalSpeed
        self.direction
        self.image = pygame.image.load("TempPlayer.png")
        self.rect = self.image.get_rect()



    def draw(self, screen):
        screen.blit(self.image,self.rect)



    def update(self, width):
        self.rotationalSpeed *= .9
        keys = pygame.key.get_pressed()
        if keys[pygrame.K_SPACE]:
            self.rect
        if keys[pygame.K_LSHIFT]:
            self.rotationalSpeed *= 1.4
