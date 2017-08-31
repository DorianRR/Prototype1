import pygame, math
from Vector import *
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")


class Level:
    def __init__(self):
        box = DestructibleObject("BoxCollider", (100, 100))
<<<<<<< HEAD
class Level:
    def __init__(self, map):
        """
        Count and temp are used in the shift level method, where count makes
        the map start in the appropriate place, and then use the temp list
        to move the map when the player presses left shift.
        """
=======
>>>>>>> 4c5817def192865c9fc2d80c2db237b0f19c7033
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

        self.collidableSprites = pygame.sprite.Group()
        self.collidableSprites.add(box)
        self.map = pygame.image.load("BgForTest.png").convert()

    def shiftLevel(self):
        if self.count == 0:
            self.temp = [544, 352]
            self.temp[0] -= 512
            self.temp[1] -= 384
            self.count = 1
        else:
            self.temp[0] -= self.cameraOffsetX
            self.temp[1] -= self.cameraOffsetY

        for item in self.collidableSprites:
            item.rect.x -= self.cameraOffsetX
            item.rect.y -= self.cameraOffsetY
        return self.temp

<<<<<<< HEAD
    def shift(self)
        return self.temp
=======
    def shiftWorld(self):
        pass
>>>>>>> 4c5817def192865c9fc2d80c2db237b0f19c7033

    def draw(self, screen):
        screen.blit(self.map, self.shiftLevel())
        self.collidableSprites.draw(screen)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] and self.kickCounter <= 0:
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
        self.collidableSprites.update()


