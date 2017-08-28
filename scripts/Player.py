import pygame, math
from Vector import *


class Player:
    def __init__(self, filename):

        self.lateralSpeed = 0
        self.location = (512-32, 384-32)
        self.direction = Vector(0, 1)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

        self.rect.center = (512, 384)
        self.kickCounter = 0
        self.rotateCounter = 0
        self.fuelLevel = 1000


    def draw(self, screen):
        screen.blit(self.image, self.rect)



    def update(self):

        #self.rotationalSpeed *= .5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and self.kickCounter <= 0:
            self.kickCounter = 30
            self.lateralSpeed += 10
        self.rect.center = ((self.rect.centerx+(self.lateralSpeed*self.direction.x)), (self.rect.centery+(self.lateralSpeed*self.direction.y)))

        if keys[pygame.K_SPACE] and self.fuelLevel > 0:
            self.image = pygame.transform.rotate(self.image, 90)
            self.fuelLevel -= 10
        self.kickCounter -= 1
        self.lateralSpeed *= .9