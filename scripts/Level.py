import pygame, math
from Vector import *
from Player import *

class Level:
    def __init__(self):

        self.count = 0
        self.temp = []



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
