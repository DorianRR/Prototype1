import pygame, math
from obstacles import *
from spriteSheetToList import *

class Player:
    def __init__(self, filename):
        self.moving = False
        self.direction = pygame.math.Vector2(0, -1)
        self.image = pygame.image.load(filename)
        self.image = spriteSheetToList(self.image, 8)
        self.rect = self.image[0].get_rect()
        sqrt2 = math.sqrt(2)/2
        self.rotationList = [(0,-1),(sqrt2,-sqrt2),(1,0),(sqrt2,sqrt2),(0,1),(-sqrt2,sqrt2),(-1,0),(-sqrt2,-sqrt2)]

        self.imageRotated = 0
        self.rect.center = (1920 / 2, 1080 / 2)

        self.fuelLevel = 3000
        self.MoneyDamage = 0
        self.momentum = 0


        self.delayTimer = 5.5
        self.delay = 6

    """
    def getPositionOffset(self):
        if self.count == 0:
            self.temp = list(self.rect.center)
            self.temp[0] -= 1920 - self.rect.centerx
            self.temp[1] -= 1080 - self.rect.centery
            self.count = 1
            return self.temp
        else:
            self.temp[0] -= self.cameraOffsetX
            self.temp[1] -= self.cameraOffsetY
            return self.temp
    """


    def draw(self, screen):
        screen.blit(self.image[self.imageRotated], self.rect)

    def update(self):
        mouse_v = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_v += (pygame.math.Vector2(-(self.rect.centerx),-(self.rect.centery)))
        if mouse_v != (0, 0):
            mouse_v = pygame.math.Vector2.normalize(mouse_v)
        self.direction = mouse_v
        count = 0
        for angle in self.rotationList:
            if (abs(mouse_v[0] - angle[0]) < 0.2) and (abs(mouse_v[1] - angle[1]) < .2):
                self.imageRotated = count
            count += 1

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > 1920:
            self.rect.right = 1920
        if self.rect.bottom > 1080:
            self.rect.bottom = 1080
        if self.rect.left < 0:
            self.rect.left = 0
