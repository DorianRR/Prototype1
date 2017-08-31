import pygame, math
from Vector import *
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")

class Level:
    def __init__(self):
        """
        Count and temp are used in the shift level method, where count makes
        the map start in the appropriate place, and then use the temp list
        to move the map when the player presses left shift.
        """
        box = DestructibleObject("BoxCollider", (100,100))
        self.count = 0
        self.temp = []
        self.lateralSpeed = 0
        self.direction = Vector(0, -1)

        self.temp_X = 0
        self.temp_Y = 0

        sqrt2 = math.sqrt(2) / 2
        self.rotationList = [(0, -1), (sqrt2, -sqrt2), (1, 0), (sqrt2, sqrt2), (0, 1), (-sqrt2, sqrt2), (-1, 0),
                             (-sqrt2, -sqrt2)]
        self.rotateCounter = 0
        self.fuelLevel = 3000
        self.imageRotated = 0
        self.kickCounter = 0
        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

        self.delayTimer = 0
        self.delay = 6

        self.collidableSprites = pygame.sprite.Group()
        self.collidableSprites.add(box)
        self.map = pygame.image.load("BgForTest.png").convert()
        self.mapRect = self.map.get_rect()
        self.mapRect.topleft = (0,0)

    def shiftLevel(self):
##
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
        #if self.lateralSpeed < 1.5:
         #   self.lateralSpeed = 0
        if pygame.sprite.spritecollide(player, self.collidableSprites, False):
            self.temp_X = -self.temp_X
            self.temp_Y = -self.temp_Y
        self.cameraOffsetX = (self.lateralSpeed * self.temp_X)
        self.cameraOffsetY = (self.lateralSpeed * self.temp_Y)

        self.kickCounter -= 1
        self.lateralSpeed *= .95
        self.shiftLevel()
        


