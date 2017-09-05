import pygame, math
from Player import *
from DestructibleObject import *
from Wall import *

pygame.init()
player = Player("../images/PlayerCharacterTemp.png")

class Level:
    def __init__(self):

        self.lateralSpeed = 0

        self.MoneyDamage = 0
        self.Maxfuel = 5000
        self.fuelLevel = 5000

        self.temp_X = 0
        self.temp_Y = 0

        self.MoneyDamage = 0
        self.cameraOffsetX = 0
        self.cameraOffsetY = 0
        
        ### COLLIDABLE OBJECTS ##############################################################
        ###  (image, position, value($), mass, fallen(if it has a destroyed state), flipX, flipY ###
        self.collidableSprites = pygame.sprite.LayeredUpdates()
        
        ### TABLES ############
        for x in range(1234, 1537, 101):
            table = DestructibleObject("Table01", (x, 168), 5, 9, False, False, True)
            self.collidableSprites.add(table)
            table = DestructibleObject("Table01", (x, 25), 5, 9, False)
            self.collidableSprites.add(table)
        for y in range(8, 120, 101):
            table = DestructibleObject("Table02", (1040, y), 5, 9, False)
            self.collidableSprites.add(table)
            table = DestructibleObject("Table02", (890, y), 5, 9, False, True)
            self.collidableSprites.add(table)
        #######################
        ### COMPUTERS #########
        for x in range(1234, 1537, 101):
            monitor = DestructibleObject("Monitor", (x, 25), 5, 2, True)
            self.collidableSprites.add(monitor)
            keyboard = DestructibleObject("Keyboard02", (x + 10, 45), 5, 1, False)
            self.collidableSprites.add(keyboard)
            keyboard = DestructibleObject("Keyboard02", (x + 10, 173), 5, 1, False)
            self.collidableSprites.add(keyboard)
            mouse = DestructibleObject("mouse01", (x + 50, 45), 5, 1, False)
            self.collidableSprites.add(mouse)
            monitor = DestructibleObject("Monitor", (x, 168 + 30), 5, 2, True)
            self.collidableSprites.add(monitor)
            
        
        ### CHAIRS ############
        for x in range(1264, 1566, 101):
            chair = DestructibleObject("Chair03", (x, 127), 5, 4, True)
            self.collidableSprites.add(chair)
            chair = DestructibleObject("Chair02", (x, 80), 5, 4, True, False, True)
            self.collidableSprites.add(chair)
        #######################
        
        ####################################################################################

        ### WALLS ##########################################################################
        self.walls = pygame.sprite.Group()
        for x in range(189, 1390, 300):
            wall = Wall((x, 229), (80,80))
            self.walls.add(wall)
            wall = Wall((x, 772), (80,80))
            self.walls.add(wall)

        wall = Wall((898, 413), (785, 255))
        self.walls.add(wall)
        wall = Wall((1593, 787), (145, 293))
        self.walls.add(wall)
        wall = Wall((1593, 0), (320, 294))
        self.walls.add(wall)
        ###################################################################################

        self.map = pygame.image.load("../images/background.png").convert()
        self.mapRect = self.map.get_rect()

    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)

    def FuelBar(self,screen,color,posX,posY,value,maxvalue):
        healthBar = pygame.image.load("../images/FuelBar01.png").convert_alpha()
        healthBar = pygame.transform.scale(healthBar, (600, 50))
        screen.blit(healthBar,(100,20))
        pygame.draw.rect(screen,[10,10,10],[posX-25, posY+17, 425, 22],5) # Draw a rect outline
        pygame.draw.rect(screen, color,[posX-22, posY+17, 420*value/maxvalue, 18]) # Draw a solid rect


    def update(self):

        player.update()

        self.collidableSprites.update(self.walls, player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            self.lateralSpeed += .55
            self.fuelLevel -= 10
        if self.lateralSpeed < .4:
            player.momentum = (self.lateralSpeed/7)
            self.lateralSpeed = 0
        collidedList = pygame.sprite.spritecollide(player, self.collidableSprites, False)
        if collidedList:          
            for collidedObject in collidedList:
                if self.lateralSpeed > 1:
                    if collidedObject.hitCount >= collidedObject.mass and not collidedObject.collided:
                        self.MoneyDamage += collidedObject.value
                        collidedObject.collided = True
                    if not collidedObject.collided:
                        collidedObject.hitCount += 5
                        player.direction.x = -(player.direction.x) * 1.1
                        player.direction.y = -(player.direction.y) * 1.1
                        collidedObject.update(self.walls, player)
                        collidedObject.goesFlying(player.direction.x, player.direction.y, self.lateralSpeed)
                
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)
        
        player.rect.x += self.cameraOffsetX

        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:
            if self.cameraOffsetX > 0:
                player.rect.right = collidedWalls[0].rect.left
            else:
                player.rect.left = collidedWalls[0].rect.right
        
        player.rect.y += self.cameraOffsetY
        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:
            if self.cameraOffsetY > 0:
                player.rect.bottom = collidedWalls[0].rect.top
            else:
                player.rect.top = collidedWalls[0].rect.bottom
        self.lateralSpeed *= .95

        


