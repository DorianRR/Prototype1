import pygame, math, random
from Player import *
from DestructibleObject import *
from Wall import *
from Fire import *

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

        self.fireList = pygame.sprite.Group()

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
        table = DestructibleObject("Table02", (1700, 440), 70, 9, True)
        self.collidableSprites.add(table)
        table = DestructibleObject("Table02", (1700, 540), 70, 9, True, True)
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
                num = random.randint(1,2)
                mouse = DestructibleObject("mouse0" + str(num), (x + 50, y + 45), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse0" + str(num), (x + 50, y + 183), 60, 1, False, True, True)
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
                num = random.randint(1,2)
                mouse = DestructibleObject("mouse0" + str(num) + "R", (x - 140, y+50), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse0" + str(num) + "R", (x + 15, y+50), 60, 1, False, True, True)
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
                num = random.randint(1,2)
                mouse = DestructibleObject("mouse0" + str(num) + "R", (x - 140, y+50), 60, 1, False)
                self.collidableSprites.add(mouse)
                mouse = DestructibleObject("mouse0" + str(num) + "R", (x + 15, y+50), 60, 1, False, True, True)
                self.collidableSprites.add(mouse)
        
    
        
        ### CHAIRS ############
        for x in range(1264, 1566, 101):
            for y in range(0, 851, 850):
                num = random.randint(1, 3)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num), (x, y + 127), 100, 4, True)
                self.collidableSprites.add(chair)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num), (x, y + 80), 100, 4, True, False, True)
                self.collidableSprites.add(chair)

        for y in range(8, 120, 101):
            for x in range(440, 1041, 300):
                num = random.randint(1, 3)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num) + "R", (x - 40, y + 25), 100, 4, True)
                self.collidableSprites.add(chair)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num) + "R", (x - 100, y + 25), 100, 4, True, True)
                self.collidableSprites.add(chair)

        for y in range(860, 962, 101):
            for x in range(440, 1041, 300):
                num = random.randint(1, 3)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num) + "R", (x - 40, y + 25), 75, 4, True)
                self.collidableSprites.add(chair)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num) + "R", (x - 100, y + 25), 75, 4, True, True)
                self.collidableSprites.add(chair)

        for x in range(77, 210, 44):
            for y in range(419, 628, 52):
                num = random.randint(1, 3)
                isTall = ""
                if random.randint(1,2) == 1:
                    isTall = "Tall"
                chair = DestructibleObject(isTall + "Chair0" + str(num) + "R", (x, y), 75, 4, True, True)
                self.collidableSprites.add(chair)

        #### TRASH ############
        for x in range(206, 1407, 300):
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
        for y in range(426, 577, 150):
            tv  = DestructibleObject("TVR", (10, y), 500, 6, True)
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
        for x in range(298, 899, 300):
            for y in range(190, 1000, 750):
                num = random.randint(1,3)
                paper = DestructibleObject("Papersheet0" + str(num), (x + 15, y - 15), 10, 1, True)
                self.collidableSprites.add(paper)
        #### WATER BOTTLES ########
        for x in range(298, 899, 300):
            for y in range(190, 1000, 750):
                num = random.randint(1,3)
                bottle = DestructibleObject("Bottle0" + str(num), (x, y), 10, 1, True)
                self.collidableSprites.add(bottle)

        for x in range(1706, 1737, 15):
            for y in range(442, 619, 35):
                num = random.randint(1,3)
                bottle = DestructibleObject("Bottle0" + str(num), (x, y), 10, 1, True)
                self.collidableSprites.add(bottle)
                watercup = DestructibleObject("WaterCup", (x, y + 15), 5, 1, True)
                self.collidableSprites.add(watercup)

        #@### VIDEO GAME CASE #######
        for x in range(250, 676, 423): 
            for y in range(415, 700, 150):
                game = DestructibleObject("GameCabinet01", (x,y), 300, 6, True, True)
                self.collidableSprites.add(game)

        for x in range(1595, 1811, 72):
            for y in range(876, 1016, 70):
                game = DestructibleObject("GameCabinet01", (x - 25,y + 25), 300, 6, True, True)
                self.collidableSprites.add(game)

        for x in range(68, 284, 72):
            for y in range(40, 180, 70):
                game = DestructibleObject("GameCabinet01", (x - 25,y + 25), 300, 6, True, True)
                self.collidableSprites.add(game)

        for x in range(68, 284, 72):
            for y in range(880, 1020, 70):
                game = DestructibleObject("GameCabinet01", (x - 25,y + 25), 300, 6, True, True)
                self.collidableSprites.add(game)

        #### HEADPHONES #####        
        for x in range(304, 905, 300):
            for y in range(81, 1036, 954):
                num  = random.randint(1, 9)
                headphones = DestructibleObject("Headphone0" + str(num), (x,y), 100, 1, False)
                self.collidableSprites.add(headphones)
        
        #### WACOM TABLETS #########
        for x in range(455, 1056, 300):
            for y in range(934, 1035, 100):
                wacom = DestructibleObject("WacomTablet", (x,y), 350, 2, True)
                self.collidableSprites.add(wacom)
                pen = DestructibleObject("WacomPen", (x - 10,y), 70, 1, True)
                self.collidableSprites.add(pen)

        ### MISC ###################
        watercup = DestructibleObject("WaterCup", (1307, 1033), 5, 1, True)
        self.collidableSprites.add(watercup)
        watercup = DestructibleObject("WaterCup", (1408, 892), 5, 1, True)
        self.collidableSprites.add(watercup)
        num  = random.randint(1, 9)
        headphones = DestructibleObject("Headphone0" + str(num), (1405,1033), 100, 1, False)
        self.collidableSprites.add(headphones)
        wacom = DestructibleObject("WacomTablet", (1508,1033), 350, 2, True)
        self.collidableSprites.add(wacom)
        pen = DestructibleObject("WacomPen", (1498,1033), 70, 1, True)
        self.collidableSprites.add(pen)
        for x in range(1307, 1508, 200):
            wacom = DestructibleObject("WacomTablet", (x,179), 350, 2, True)
            self.collidableSprites.add(wacom)
            pen = DestructibleObject("WacomPen", (x - 10,179), 70, 1, True)
            self.collidableSprites.add(pen)
        watercup = DestructibleObject("WaterCup", (1408, 44), 5, 1, True)
        self.collidableSprites.add(watercup)
        watercup = DestructibleObject("WaterCup", (1408, 186), 5, 1, True)
        self.collidableSprites.add(watercup)
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
        wall = Wall((1593, 0), (320, 294))
        self.walls.add(wall)
        wall = Wall((1790, 287), (120, 788))
        self.walls.add(wall)
        ###################################################################################
        self.map = pygame.image.load("../images/background.png").convert()
        self.mapRect = self.map.get_rect()

    def draw(self, screen):
        screen.blit(self.map, self.mapRect)
        self.collidableSprites.draw(screen)
        #self.fireList.draw(screen)

    def spawnFire(self, collidedObject):
        if collidedObject.mass <= 2:
            randomNum = random.randint(1, 10)
            if randomNum < 3:
                game = Fire((collidedObject.rect.topleft), "Flame01")
                self.fireList.add(game)
        elif collidedObject.mass <= 5 and collidedObject.mass > 2:
            randomNum = random.randint(1, 10)
            if randomNum < 2:
                game = Fire((collidedObject.rect.topleft), "Flame02")
                self.fireList.add(game)
        elif collidedObject.mass > 5:
            randomNum = random.randint(1, 10)
            if randomNum < 2:
                game = Fire((collidedObject.rect.topleft), "Flame03")
                self.fireList.add(game)


    def FuelBar(self,screen,color,posX,posY,value,maxvalue):
        healthBarSqueeze1 = pygame.image.load("../images/FuelBar.png").convert_alpha()
        healthBar1 = pygame.transform.scale(healthBarSqueeze1, (200, 600))
        screen.blit(healthBar1,(posX+1700,posY+300))
        pygame.draw.rect(screen, color,[posX+1790, posY+440, 25, 440*value/maxvalue]) # Draw a solid rect


    def update(self):

        player.update()
        random.seed
        self.collidableSprites.update(self.walls, player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.lateralSpeed += .65
            self.fuelLevel -= 3
        if self.lateralSpeed < .5: #Because of how we move, this pevents us from sliding for a long time.
            self.lateralSpeed = 0
        collidedList = pygame.sprite.spritecollide(player, self.collidableSprites, False)
        if collidedList:

            #The following three lines are what make the player spin faster and faster when we hit objects.
            player.spinning = True
            if player.modDelay > 1:
                player.modDelay -= 1

            for collidedObject in collidedList:
                if self.lateralSpeed > 1: #Determines what the speed needs to be to destroy stuff
                    self.lateralSpeed *= .99 #Running into stuff slows you down here
                    if not collidedObject.collided:
                        self.spawnFire(collidedObject) #Calls a flame spawning method
                        collidedObject.hitCount += 5 #Some objects take multiple hits, this is where they take "Damage"
                        #The following four lines reflect the player on collisions when it's going under a certain speed

                        if self.lateralSpeed < 9:
                            collidedObjectNormalVector = (pygame.math.Vector2(860 - collidedObject.rect.x, 540 - collidedObject.rect.y))
                            collidedObjectNormalVector = pygame.math.Vector2(collidedObjectNormalVector)
                            player.direction = pygame.math.Vector2.reflect(player.direction, collidedObjectNormalVector)
                            player.direction = pygame.math.Vector2.normalize(player.direction)

                        collidedObject.update(self.walls, player)
                        #The following line sends collided objects flying based on player speed and object mass
                        collidedObject.goesFlying(player.direction.x, player.direction.y, self.lateralSpeed)

                    if collidedObject.hitCount >= collidedObject.mass and not collidedObject.collided:
                        self.MoneyDamage += collidedObject.value
                        collidedObject.collided = True
        #The following two lines move the player
        self.cameraOffsetX = (self.lateralSpeed * player.direction.x)
        self.cameraOffsetY = (self.lateralSpeed * player.direction.y)
        
        player.rect.x += self.cameraOffsetX

        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:
            if self.cameraOffsetX > 0:
                player.rect.right = collidedWalls[0].rect.left
            else:
                player.rect.left = collidedWalls[0].rect.right
            player.direction.x = -(player.direction.x)
        
        player.rect.y += self.cameraOffsetY
        collidedWalls =  pygame.sprite.spritecollide(player, self.walls, False)
        if collidedWalls:
            if self.cameraOffsetY > 0:
                player.rect.bottom = collidedWalls[0].rect.top
            else:
                player.rect.top = collidedWalls[0].rect.bottom
            player.direction.y = -(player.direction.y)
        self.lateralSpeed *= .95
        mouse = pygame.mouse.get_pressed()

        # Rob, this is probably where the logic for a pointer indicator should go
        if mouse[0] and self.lateralSpeed < .5:
            player.direction = player.mouse_v
            player.modDelay = 15
            player.spinning = False




