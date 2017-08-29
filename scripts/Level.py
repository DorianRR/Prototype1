import pygame, math
from Vector import *
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")
#box = DestructibleObject("BoxCollider", (100, 100))

class Level:
    def __init__(self, map):

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
        self.count = 0
        self.temp = []

        self.delayTimer = 0
        self.delay = 6

        #collidableSprites = pygame.sprite.Group()
        #collidableSprites.add(box)
        map = pygame.image.load(map)

    def shiftLevel(self):
        if self.count == 0:
            self.temp = [544, 352]
            self.temp[0] -= 512
            self.temp[1] -= 384
            self.count = 1
            return self.temp
        else:
            self.temp[0] -= self.cameraOffsetX
            self.temp[1] -= self.cameraOffsetY
            return self.temp



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and self.kickCounter <= 0:
            self.kickCounter = 30
            self.lateralSpeed += 12
            self.temp_X = player.direction.x
            self.temp_Y = player.direction.y
        if self.lateralSpeed < 1.5:
            self.lateralSpeed = 0
        self.cameraOffsetX = (self.lateralSpeed * self.temp_X)
        self.cameraOffsetY = (self.lateralSpeed * self.temp_Y)

        self.kickCounter -= 1
        self.lateralSpeed *= .95
        player.update()


