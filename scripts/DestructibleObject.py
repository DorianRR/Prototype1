import pygame

class DestructibleObject(pygame.sprite.Sprite):

    def __init__(self, image, position, value, mass, fallen, flipX = False, flipY = False):

        pygame.sprite.Sprite.__init__(self) #When subclassing the Sprite, be sure to call the base initializer before adding the Sprite to Groups
        self.image =  pygame.image.load("../ArtResource/" + image + ".png").convert_alpha()
        if flipY:
            self.image = pygame.transform.flip(self.image, False, True)
        if flipX:
            self.image = pygame.transform.flip(self.image, True, False)
        self.fallen = fallen
        if self.fallen:
            self.destroyed = pygame.image.load("../ArtResource/" + image + "Fallen.png").convert_alpha()
            if flipY:
                self.destroyed = pygame.transform.flip(self.destroyed, False, True)
            if flipX:
                self.destroyed = pygame.transform.flip(self.destroyed, False, True)
            self.destroyedMask = pygame.mask.from_surface(self.destroyed)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.mask = pygame.mask.from_surface(self.image)
        
        #self.switch  = False
        self.collided = False
        self.speed = 0
        self.value = value
        self.mass = mass
        self.hitCount = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def goesFlying(self, directionX, directionY, speed):
        self.speed = speed / self.mass
        self.direction = pygame.math.Vector2(directionX, directionY)


    def update(self, walls, player):
        if self.collided and self.fallen:
            self.image = self.destroyed
            self.mask = self.destroyedMask
        if self.speed > 0:
            self.rect.x -= self.direction.x * self.speed * 2
##            if player.rect.colliderect(self.rect) and not self.collided:
##                if self.direction.x > 0:
##                    self.rect.right = player.rect.left
##                elif self.direction.x < 0:
##                    self.rect.left = player.rect.right
            collidedWalls =  pygame.sprite.spritecollide(self, walls, False)
            if collidedWalls:
                if self.direction.x < 0:
                    self.rect.right = collidedWalls[0].rect.left
                elif self.direction.x > 0:
                    self.rect.left = collidedWalls[0].rect.right
                
            
            self.rect.y -= self.direction.y * self.speed * 2
##            if player.rect.colliderect(self.rect) and not self.collided:
##                if self.direction.y > 0:
##                    self.rect.bottom = player.rect.top
##                elif self.direction.y < 0:
##                    self.rect.top = player.rect.bottom
            collidedWalls =  pygame.sprite.spritecollide(self, walls, False)
            if collidedWalls:
                if self.direction.y < 0:
                    self.rect.bottom = collidedWalls[0].rect.top
                elif self.direction.y > 0:
                    self.rect.top = collidedWalls[0].rect.bottom

        if self.speed < .5:
            self.speed = 0
        
        self.speed *= .95

        
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > 1920:
            self.rect.right = 1920
        if self.rect.bottom > 1080:
            self.rect.bottom = 1080
        if self.rect.left < 0:
            self.rect.left = 0
        
        
        
        
        
