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
        self.Maxfuel = 3000
        self.fuelLevel = 3000

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
            for y in range(0, 851, 850):
                table = DestructibleObject("Table01", (x, y + 168), 5, 9, False, False, True)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table01", (x, y + 25), 5, 9, False)
                self.collidableSprites.add(table)
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                table = DestructibleObject("Table02", (x, y), 5, 9, False)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table02", (x - 150, y), 5, 9, False, True)
                self.collidableSprites.add(table)
        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                table = DestructibleObject("Table02", (x, y), 5, 9, False)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table02", (x - 150, y), 5, 9, False, True)
                self.collidableSprites.add(table)
        #######################
        ### COMPUTERS #########
        for x in range(1234, 1537, 101):
            for y in range(0, 851, 850):
                monitor = DestructibleObject("Monitor", (x, y + 25), 5, 2, True)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02", (x + 10, y + 45), 5, 1, False)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02", (x + 10, y + 173), 5, 1, False)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse01", (x + 50, y + 45), 5, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse01", (x + 50, y + 183), 5, 1, False, True, True)
                self.collidableSprites.add(mouse)
                monitor = DestructibleObject("Monitor", (x, y + 198), 5, 2, True)
                self.collidableSprites.add(monitor)
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                monitor = DestructibleObject("MonitorR", (x + 30, y), 5, 2, False)
                self.collidableSprites.add(monitor)
                monitor = DestructibleObject("MonitorR", (x - 150, y), 5, 2, False)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 5, 1, False, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 5, 1, False, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 5, 1, False)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 5, 1, False)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse02R", (x - 140, y+50), 5, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse02R", (x + 15, y+50), 5, 1, False, True, True)
                self.collidableSprites.add(mouse)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                monitor = DestructibleObject("MonitorR", (x + 30, y), 5, 2, False)
                self.collidableSprites.add(monitor)
                monitor = DestructibleObject("MonitorR", (x - 150, y), 5, 2, False)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 5, 1, False, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 5, 1, False, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 5, 1, False)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 5, 1, False)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse02R", (x - 140, y+50), 5, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse02R", (x + 15, y+50), 5, 1, False, True, True)
                self.collidableSprites.add(mouse)
        
    
        
        ### CHAIRS ############
        for x in range(1264, 1566, 101):
            for y in range(0, 851, 850):
                chair = DestructibleObject("Chair03", (x, y + 127), 5, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair02", (x, y + 80), 5, 4, True, False, True)
                self.collidableSprites.add(chair)

        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                chair = DestructibleObject("Chair01R", (x - 40, y), 5, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair01R", (x - 100, y), 5, 4, True, True)
                self.collidableSprites.add(chair)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                chair = DestructibleObject("Chair01R", (x - 40, y), 5, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair01R", (x - 100, y), 5, 4, True, True)
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
        screen.blit(healthBar,(posX,posY))
        #pygame.draw.rect(screen,[10,10,10],[posX+20, posY+17, 425, 22],5) # Draw a rect outline
        pygame.draw.rect(screen, color,[posX+28, posY+20, 420*value/maxvalue, 15]) # Draw a solid rect


    def update(self):

        player.update()

        self.collidableSprites.update(self.walls, player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            self.lateralSpeed += .55
            self.fuelLevel -= 3
        if self.lateralSpeed < .4:
            player.momentum = (self.lateralSpeed/7)
            self.lateralSpeed = 0
        collidedList = pygame.sprite.spritecollide(player, self.collidableSprites, False)
        if collidedList:
            if player.modDelay > 1:
                player.modDelay -= 1
            for collidedObject in collidedList:
                if self.lateralSpeed > 1:
                    if collidedObject.hitCount >= collidedObject.mass and not collidedObject.collided:
                        self.MoneyDamage += collidedObject.value
                        collidedObject.collided = True
                    if not collidedObject.collided:
                        collidedObject.hitCount += 5
                        collidedObjectNormalVector = (pygame.math.Vector2(860-collidedObject.rect.x, 540-collidedObject.rect.y))
                        collidedObjectNormalVector = pygame.math.Vector2(collidedObjectNormalVector)
                        player.direction = pygame.math.Vector2.reflect(player.direction, collidedObjectNormalVector)
                        player.direction = pygame.math.Vector2.normalize(player.direction)
                        #player.direction.x = -(player.direction.x)
                        #player.direction.y = -(player.direction.y)
                        collidedObject.update(self.walls, player)
                        collidedObject.goesFlying(player.direction.x, player.direction.y, self.lateralSpeed)

        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)
        
        player.rect.x += self.cameraOffsetX

        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:

            if self.cameraOffsetX > 0:
                player.rect.right = collidedWalls[0].rect.left
                player.direction.x = -(player.direction.x)

            else:
                player.rect.left = collidedWalls[0].rect.right
                player.direction.x = -(player.direction.x)

        player.rect.y += self.cameraOffsetY
        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:
            if self.cameraOffsetY > 0:
                player.rect.bottom = collidedWalls[0].rect.top
                player.direction.y = -(player.direction.y)

            else:
                player.rect.top = collidedWalls[0].rect.bottom
                player.direction.y = -(player  .direction.y)

        self.lateralSpeed *= .95

        


