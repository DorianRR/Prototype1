import pygame, math
from Vector import *

class Player:
    def __init__(self, filename):

        self.rotationalSpeed = 0
        self.location = (512-32, 384-32)
        self.direction = Vector(0, 1)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()



    def draw(self, screen):
        screen.blit(self.image, self.location)



    def update(self):
        self.rotationalSpeed *= .95
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
            #self.rect
        if keys[pygame.K_LSHIFT]:
            if self.rotationalSpeed == 0:
                self.rotationalSpeed =+ .01
            self.rotationalSpeed *= 1.2
        self.image = pygame.transform.rotate(self.image, (self.rotationalSpeed*(10 * (math.pi/180))))

