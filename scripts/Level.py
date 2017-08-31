import pygame, math
from Vector import *
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        box = DestructibleObject("BoxCollider", (100,100))
        self.lateralSpeed = 0

        self.temp_X = 0
        self.temp_Y = 0

        self.kickCounter = 0
        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

        self.collidableSprites = pygame.sprite.Group()
        self.collidableSprites.add(box)
        self.map = pygame.image.load("BgForTest.png").convert()
        self.mapRect = self.map.get_rect()

    def shiftLevel(self):

        self.mapRect.x -= self.cameraOffsetX
        self.mapRect.y -= self.cameraOffsetY
        for item in self.collidableSprites:
            item.rect.x -= self.cameraOffsetX
            item.rect.y -= self.cameraOffsetY


    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)

    def update(self):
        player.update()
        self.collidableSprites.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] and self.kickCounter <= 0:
            self.kickCounter = 30
            self.lateralSpeed += 12
            self.temp_X = player.direction.x
            self.temp_Y = player.direction.y
        if self.lateralSpeed < 1.5:
            self.lateralSpeed = 0
        if pygame.sprite.spritecollide(player, self.collidableSprites, False):
            self.temp_X = -self.temp_X
            self.temp_Y = -self.temp_Y
        self.cameraOffsetX = (self.lateralSpeed * self.temp_X)
        self.cameraOffsetY = (self.lateralSpeed * self.temp_Y)

        self.kickCounter -= 1
        self.lateralSpeed *= .95
        self.shiftLevel()
        


