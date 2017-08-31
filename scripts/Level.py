import pygame, math
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        box = DestructibleObject("BoxCollider", (100,100))
        self.lateralSpeed = 0

        self.temp_X = 0
        self.temp_Y = 0

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
        if keys[pygame.K_SPACE] :
            self.lateralSpeed += .3
        if self.lateralSpeed < .2:
            self.lateralSpeed = 0
        if pygame.sprite.spritecollide(player, self.collidableSprites, False):
            player.direction.x = -player.direction.x
            player.direction.y = -player.direction.y
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)

        self.lateralSpeed *= .95
        self.shiftLevel()
        


