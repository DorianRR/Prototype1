import pygame, math
from Vector import *
from Player import *
from DestructibleObject import *

player = Player("PlayerCharacterTemp.png")
#box = DestructibleObject("BoxCollider", (100, 100))

class Level:
    def __init__(self, map):
        """
        Count and temp are used in the shift level method, where count makes
        the map start in the appropriate place, and then use the temp list
        to move the map when the player presses left shift.
        """
        self.count = 0
        self.temp = []


        self.lateralSpeed = 0
        self.direction = Vector(0, -1)
        self.temp_X = 0
        self.temp_Y = 0

        self.kickCounter = 0
        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0


        """
        Timer information used to make the player spool up their rotation
        """
        self.delayTimer = 0
        self.delay = 6

        #collidableSprites = pygame.sprite.Group()
        #collidableSprites.add(box)
        map = pygame.image.load(map)


    """
    Shift level is called in main and moves the screen with the player. Will also
    be used to move all other colliding objectrs. Called each frame.
    """
    def shiftLevel(self):
        if self.count == 0:
            self.temp = [512, 380]
            self.temp[0] -= 512
            self.temp[1] -= 384
            self.count = 1
        else:
            self.temp[0] -= self.cameraOffsetX
            self.temp[1] -= self.cameraOffsetY
        return self.temp


    """
    Logic that makes the player kick off and move, reads in direction from the  player
    class. Camera offset is set in the update method and that information will be
    used to move all of the colliding objects.
    """
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


