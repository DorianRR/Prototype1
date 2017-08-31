import pygame, math
from obstacles import *
from Vector import *
from spriteSheetToList import *

class Player:
    def __init__(self, filename):
        self.lateralSpeed = 0
        self.rotationSpeed = 100
        self.location = (512-32, 384-32)
        self.direction = Vector(0, -1)
        self.image = pygame.image.load(filename)
        self.image = spriteSheetToList(self.image, 8)
        self.rect = self.image[0].get_rect()
        sqrt2 = math.sqrt(2)/2
        self.rotationList = [(0,-1),(sqrt2,-sqrt2),(1,0),(sqrt2,sqrt2),(0,1),(-sqrt2,sqrt2),(-1,0),(-sqrt2,-sqrt2)]
        self.temp_X = 0
        self.temp_Y = 0
        
        self.imageRotated = 0
        self.rect.center = (512, 384)
        self.kickCounter = 0
        self.rotateCounter = 0
        self.fuelLevel = 30000
        self.MoneyDamage = 0

    def draw(self, screen):
        screen.blit(self.image[self.imageRotated], self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and self.kickCounter <= 0:
            self.kickCounter = 30
            self.lateralSpeed += 12
            self.temp_X = self.direction.x
            self.temp_Y = self.direction.y
        if self.lateralSpeed < 1.5:
            self.lateralSpeed = 0
        self.rect.center = ((self.rect.centerx+(self.lateralSpeed*self.temp_X)), (self.rect.centery+(self.lateralSpeed*self.temp_Y)))
        self.location = [self.rect.centerx,self.rect.centery]

        if keys[pygame.K_SPACE] and self.fuelLevel > 0:
            pygame.time.delay (int(self.rotationSpeed))
            if self.imageRotated < 7:
                self.imageRotated += 1
                self.direction.setDirection(self.rotationList[self.imageRotated])
            else:
                self.imageRotated =0
                self.direction.setDirection(self.rotationList[self.imageRotated])
            self.fuelLevel -= 10
            self.rotationSpeed *= .9
        else:
            self.rotationSpeed = 100
        self.kickCounter -= 1
        self.lateralSpeed *= .95
