import pygame, math
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        box = DestructibleObject("BoxCollider", (1000,500))
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
        for item in self.collidableSprites:
            item.rect.x -= self.cameraOffsetX
            item.rect.y -= self.cameraOffsetY
        self.mapRect.x -= self.cameraOffsetX
        self.mapRect.y -= self.cameraOffsetY



    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)

    def update(self):
        self.collidableSprites.update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.lateralSpeed += .5
        if self.lateralSpeed < .5:
            self.lateralSpeed = 0
        if pygame.sprite.spritecollide(player, self.collidableSprites, False):
            player.direction.x = -player.direction.x
            player.direction.y = -player.direction.y
        #self.lateralSpeed += .1

        print(self.lateralSpeed)
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)
        player.update()
        self.lateralSpeed = .95 *self.lateralSpeed
        self.shiftLevel()



