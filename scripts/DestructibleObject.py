import pygame

class DestructibleObject(pygame.sprite.Sprite):

    def __init__(self, image, position, value, mass, fallen):

        pygame.sprite.Sprite.__init__(self) #When subclassing the Sprite, be sure to call the base initializer before adding the Sprite to Groups
        self.image =  pygame.image.load("../ArtResource/" + image + ".png").convert_alpha()
        self.fallen = fallen
        if self.fallen:
            self.destroyed = pygame.image.load("../ArtResource/" + image + "Fallen.png").convert_alpha()
            self.destroyedMask = pygame.mask.from_surface(self.destroyed)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.mask = pygame.mask.from_surface(self.image)
        
        #self.switch  = False
        self.collided = False
        self.speed = 0
        self.value = value
        self.mass = mass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def goesFlying(self, directionX, directionY, speed):
        self.speed = speed / self.mass
        self.direction = pygame.math.Vector2(directionX, directionY)


    def update(self, walls):
        #if self.switch and not self.collided:
            #self.collided = True
        if self.collided and self.fallen:
            self.image = self.destroyed
            self.mask = self.destroyedMask
        if self.speed > 0:
            self.rect.x -= self.direction.x * self.speed * 2
            collidedWalls =  pygame.sprite.spritecollide(self, walls, False)
            if collidedWalls:
                if self.direction.x < 0:
                    self.rect.right = collidedWalls[0].rect.left
                elif self.direction.x > 0:
                    self.rect.left = collidedWalls[0].rect.right
                    
            self.rect.y -= self.direction.y * self.speed * 2
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
        
        
        
        
        
