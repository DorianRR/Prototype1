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
        self.fuelLevel = 3000
        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0
        self.count = 0
        self.temp = []

        self.delayTimer = 5.5
        self.delay = 6

    def getPositionOffset(self):
        if self.count == 0:
            self.temp = list(self.rect.center)
            self.temp[0] -= 512
            self.temp[1] -= 384
            self.count = 1
            return self.temp
        else:
            self.temp[0] -= self.cameraOffsetX
            self.temp[1] -= self.cameraOffsetY
            return self.temp



    def draw(self, screen):
        screen.blit(self.image[self.imageRotated], self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.fuelLevel > 0:
            mouse_v = pygame.math.Vector2(pygame.mouse.get_pos())
            mouse_v = pygame.math.Vector2.normalize(mouse_v)
            self.direction.setDirection(mouse_v)
            """
            self.delayTimer += .5
            if self.delayTimer%self.delay == 0:
                self.delayTimer = 0
                if self.imageRotated < 7:
                    self.imageRotated += 1
                    self.direction.setDirection(self.rotationList[self.imageRotated])
                else:
                    self.imageRotated =0
                    self.direction.setDirection(self.rotationList[self.imageRotated])
                self.fuelLevel -= 10
                self.delay -= 1
                if self.delay <= 1:
                    self.delay = 1
                self.rotationSpeed *= .9
            self.rotationSpeed *= .95
            

        else:
            self.rotationSpeed = 100
            self.delay = 5.5
        self.kickCounter -= 1
        self.lateralSpeed *= .95
        """
