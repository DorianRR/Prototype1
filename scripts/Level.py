import pygame, math
from Player import *
from DestructibleObject import *

player = Player("../images/PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        self.lateralSpeed = 0

        self.MoneyDamage = 0
        self.Maxfuel = 3000
        self.fuelLevel = 3000

        self.temp_X = 0
        self.temp_Y = 0

        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0

        self.collidableSprites = pygame.sprite.Group()
        box = DestructibleObject("../images/BoxCollider", (100, 100), 5, 1)
        box2 = DestructibleObject("../images/BoxCollider2", (400, 400), 10, 3)
        box3 = DestructibleObject("../images/BoxCollider3", (600, 600), 15, 5)
        self.collidableSprites.add(box)
        self.collidableSprites.add(box2)
        self.collidableSprites.add(box3)

        self.map = pygame.image.load("../images/MapBlockout.png").convert()
        self.map = pygame.transform.scale(self.map, (1920,1080))
        self.mapRect = self.map.get_rect()

    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)

    def FuelBar(self,screen,color,posX,posY,value,maxvalue):
        pygame.draw.rect(screen,[10,10,10],[posX-2, posY-2, 502, 22],5) # Draw a rect outline
        pygame.draw.rect(screen, color,[posX, posY, 500*value/maxvalue, 18]) # Draw a solid rect


    def update(self):

        player.update()

        self.collidableSprites.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.lateralSpeed += .5
            self.fuelLevel -= 10
        if self.lateralSpeed < .4:
            self.lateralSpeed = 0
        collidedList = pygame.sprite.spritecollide(player, self.collidableSprites, False)
        if collidedList:
            player.direction.x = -(player.direction.x)
            player.direction.y = -(player.direction.y)
            for collidedObject in collidedList:
                if self.lateralSpeed > 1:
                    if not collidedObject.collided:
                        self.MoneyDamage += collidedObject.value
                    collidedObject.collided = True
                    collidedObject.update()
                    collidedObject.goesFlying(player.direction.x, player.direction.y, self.lateralSpeed)
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)
        player.rect.x += self.cameraOffsetX
        player.rect.y += self.cameraOffsetY
        self.lateralSpeed *= .95
        
        #self.shiftLevel()
        


