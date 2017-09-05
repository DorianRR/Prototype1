import pygame, math, random
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

        ### COMPUTERS #######
        
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                comp = DestructibleObject("Computer", (x, y + 75), 2000, 5, True)
                self.collidableSprites.add(comp)
                comp = DestructibleObject("Computer", (x - 150, y + 75), 2000, 5, True, True)
                self.collidableSprites.add(comp)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                comp = DestructibleObject("Computer", (x, y + 75), 2000, 5, True)
                self.collidableSprites.add(comp)
                comp = DestructibleObject("Computer", (x - 150, y + 75), 2000, 5, True, True)
                self.collidableSprites.add(comp)

        for x in range(1234, 1537, 101):
            for y in range(0, 851, 850):
                comp = DestructibleObject("ComputerR", (x + 75, y + 168), 2000, 5, True, False, True)
                self.collidableSprites.add(comp)
                comp = DestructibleObject("ComputerR", (x + 75, y + 25), 2000, 9, True)
                self.collidableSprites.add(comp)
                
        ### TABLES ############
        for x in range(1234, 1537, 101):
            for y in range(0, 851, 850):
                table = DestructibleObject("Table01", (x, y + 168), 70, 9, True, False, True)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table01", (x, y + 25), 70, 9, True)
                self.collidableSprites.add(table)
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                table = DestructibleObject("Table02", (x, y), 70, 9, True)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table02", (x - 150, y), 70, 9, True, True)
                self.collidableSprites.add(table)
        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                table = DestructibleObject("Table02", (x, y), 70, 9, True)
                self.collidableSprites.add(table)
                table = DestructibleObject("Table02", (x - 150, y), 70, 9, True, True)
                self.collidableSprites.add(table)

        #######################
        ### COMPUTER ADD ONS #########
        for x in range(1234, 1537, 101):
            for y in range(0, 851, 850):
                monitor = DestructibleObject("Monitor", (x, y + 25), 200, 2, True)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02", (x + 10, y + 45), 100, 1, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02", (x + 10, y + 173), 100, 1, True)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse01", (x + 50, y + 45), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse01", (x + 50, y + 183), 60, 1, False, True, True)
                self.collidableSprites.add(mouse)
                monitor = DestructibleObject("Monitor", (x, y + 198), 200, 2, True)
                self.collidableSprites.add(monitor)
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                monitor = DestructibleObject("MonitorR", (x + 30, y), 200, 2, True)
                self.collidableSprites.add(monitor)
                monitor = DestructibleObject("MonitorR", (x - 150, y), 200, 2, True)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 100, 1, True, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 100, 1, True, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 100, 1, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 100, 1, True)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse02R", (x - 140, y+50), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse02R", (x + 15, y+50), 60, 1, False, True, True)
                self.collidableSprites.add(mouse)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                monitor = DestructibleObject("MonitorR", (x + 30, y), 200, 2, True)
                self.collidableSprites.add(monitor)
                monitor = DestructibleObject("MonitorR", (x - 150, y), 200, 2, True)
                self.collidableSprites.add(monitor)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 100, 1, True, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x + 5, y+5), 100, 1, True, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 100, 1, True)
                self.collidableSprites.add(keyboard)
                keyboard = DestructibleObject("Keyboard02R", (x - 125, y+5), 100, 1, True)
                self.collidableSprites.add(keyboard)
                mouse = DestructibleObject("mouse02R", (x - 140, y+50), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse02R", (x + 15, y+50), 60, 1, False, True, True)
                self.collidableSprites.add(mouse)
        
    
        
        ### CHAIRS ############
        for x in range(1264, 1566, 101):
            for y in range(0, 851, 850):
                num = random.randint(1, 3)
                chair = DestructibleObject("Chair0" + str(num), (x, y + 127), 100, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair0" + str(num), (x, y + 80), 100, 4, True, False, True)
                self.collidableSprites.add(chair)

        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                num = random.randint(1, 3)
                chair = DestructibleObject("Chair0" + str(num) + "R", (x - 40, y), 100, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair0" + str(num) + "R", (x - 100, y), 100, 4, True, True)
                self.collidableSprites.add(chair)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                num = random.randint(1, 3)
                chair = DestructibleObject("Chair0" + str(num) + "R", (x - 40, y), 5, 4, True)
                self.collidableSprites.add(chair)
                chair = DestructibleObject("Chair0" + str(num) + "R", (x - 100, y), 5, 4, True, True)
                self.collidableSprites.add(chair)

        #### TRASH ############
        for x in range(206, 1107, 300):
            for y in range(312, 727, 414):
                trash = DestructibleObject("Trash", (x,y), 20, 4, True)
                self.collidableSprites.add(trash)
        #######################

        #### WHITEBOARDS ######
        for x in range(312, 651, 338):
            for y in range(415, 550, 128):
                board = DestructibleObject("Whiteboard", (x,y), 50, 6, True, True)
                self.collidableSprites.add(board)
        
        #### TV'S ##############
        for x in range(350, 1251, 300):
            tv  = DestructibleObject("TV", (x, 10), 500, 6, True)
            self.collidableSprites.add(tv)
            tv  = DestructibleObject("TV", (x, 1070), 500, 6, True, False, True)
            self.collidableSprites.add(tv)

        #### BOOKS & PAPERS ####################
        for x in range(1234, 1537, 202):
            for y in range(0, 851, 850):
                book = DestructibleObject("Book02", (x + 60,y + 35), 75, 1, True)
                self.collidableSprites.add(book)
        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                book = DestructibleObject("Book01", (x + 10,y + 70), 75, 1, True)
                self.collidableSprites.add(book)

        #### WATER BOTTLES ########
        for x in range(298, 899, 300):
            for y in range(190, 1000, 750):
                num = random.randint(1,3)
                bottle = DestructibleObject("Bottle0" + str(num), (x, y), 10, 1, True)
                self.collidableSprites.add(bottle)

        #@### VIDEO GAME CASE #######
        for x in range(250, 676, 423): 
            for y in range(415, 700, 150):
                game = DestructibleObject("GameCabinet01", (x,y), 300, 6, True, True)
                self.collidableSprites.add(game)
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
                    if not collidedObject.collided:
                        collidedObject.hitCount += 5
                        collidedObjectNormalVector = (pygame.math.Vector2(860-collidedObject.rect.x, 540-collidedObject.rect.y))
                        collidedObjectNormalVector = pygame.math.Vector2(collidedObjectNormalVector)
                        player.direction = pygame.math.Vector2.reflect(player.direction, collidedObjectNormalVector)
                        player.direction = pygame.math.Vector2.normalize(player.direction)
                        collidedObject.update(self.walls, player)
                        collidedObject.goesFlying(player.direction.x, player.direction.y, self.lateralSpeed)
                    if collidedObject.hitCount >= collidedObject.mass and not collidedObject.collided:
                        self.MoneyDamage += collidedObject.value
                        collidedObject.collided = True
                

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
        mouse = pygame.mouse.get_pressed()
        if mouse[0] and self.lateralSpeed == 0:
            player.direction = player.mouse_v
            player.modDelay = 15


