import pygame, math
from Player import *
from DestructibleObject import *

player = Player("../images/PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        box = DestructibleObject("../images/BoxCollider", (100,100))
        box2 = DestructibleObject("../images/BoxCollider", (250,250))
        box3 = DestructibleObject("../images/BoxCollider", (350,350))
        self.lateralSpeed = 0

        self.MoneyDamage = 0
        self.fuelLevel = 3000

        self.temp_X = 0
        self.temp_Y = 0

        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

        self.collidableSprites = pygame.sprite.Group()
        self.collidableSprites.add(box)
        self.collidableSprites.add(box2)
        self.collidableSprites.add(box3)
        self.map = pygame.image.load("../images/MapBlockout.png").convert()
        self.mapRect = self.map.get_rect()

    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)

    def update(self):
        player.update()
        self.collidableSprites.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.lateralSpeed += .5
            self.fuelLevel -= 10
        if self.lateralSpeed < .4:
            self.lateralSpeed = 0
        if pygame.sprite.spritecollide(player, self.collidableSprites, False):
            player.direction.x = -player.direction.x
            player.direction.y = -player.direction.y
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY =  (self.lateralSpeed * player.direction.y)
        player.rect.x += self.cameraOffsetX
        player.rect.y += self.cameraOffsetY
        self.lateralSpeed *= .95
        
        #self.shiftLevel()
        


