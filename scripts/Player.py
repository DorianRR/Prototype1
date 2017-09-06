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
        self.mouse_v = pygame.math.Vector2(pygame.mouse.get_pos())
        self.imageRotated = 0
        self.rect.center = (1920 / 12, 1080 / 2)

        self.fuelLevel = 3000
        self.MoneyDamage = 0

        self.spinning = False
        self.delayTimer = 0
        self.delay = 0
        self.directionTimer = 0
        self.modDelay = 15



    def draw(self, screen):
        self.delayTimer += 1

        if self.delayTimer%self.modDelay == 0 and self.spinning:
            self.delay += 1
            self.imageRotated = self.delay
            if self.delay >= 7:
                self.delay = 0
            screen.blit(self.image[self.imageRotated], self.rect)
        else:
            screen.blit(self.image[self.imageRotated], self.rect)

    def update(self):

        prev_mouse_v = self.mouse_v
        self.mouse_v = pygame.math.Vector2(pygame.mouse.get_pos())
        self.mouse_v += (pygame.math.Vector2(-(self.rect.centerx),-(self.rect.centery)))
        self.mouse_v = (self.mouse_v + prev_mouse_v)
        if self.mouse_v != (0, 0):
            self.mouse_v = pygame.math.Vector2.normalize(self.mouse_v)
        count = 0
        for angle in self.rotationList:
            if (abs(self.mouse_v[0] - angle[0]) < 0.2) and (abs(self.mouse_v[1] - angle[1]) < .2):
                self.imageRotated = count
            count += 1

        if self.rect.top < 0:
            self.direction.y = -(self.direction.y)
            self.rect.top = 0
        if self.rect.right > 1920:
            self.direction.x = -(self.direction.x)
            self.rect.right = 1920
        if self.rect.bottom > 1080:
            self.direction.y = -(self.direction.y)
            self.rect.bottom = 1080
        if self.rect.left < 0:
            self.direction.x = -(self.direction.x)
            self.rect.left = 0
