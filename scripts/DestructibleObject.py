import pygame, PyIgnition

class DestructibleObject(pygame.sprite.Sprite):

    def __init__(self, image, position, value, mass,screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self) #When subclassing the Sprite, be sure to call the base initializer before adding the Sprite to Groups
        self.image =  pygame.image.load("../images/" + image + ".png").convert_alpha()
        self.destroyed = pygame.image.load("../images/" + image + "Destroyed.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.mask = pygame.mask.from_surface(self.image)
        self.destroyedMask = pygame.mask.from_surface(self.destroyed)
        #self.switch  = False
        self.collided = False
        self.speed = 0
        self.value = value
        self.mass = mass

        self.SmashEffect = PyIgnition.ParticleEffect(screen, (0, 0), (800, 600))
        self.source = self.SmashEffect.CreateSource((self.rect.center), initspeed=3.0, initdirection=3.140, initspeedrandrange=0.3,initdirectionrandrange=0.3, particlesperframe=8, particlelife=50,drawtype=PyIgnition.DRAWTYPE_IMAGE, colour=(255, 255, 255), radius=3.0,imagepath="../images/BoxCollider3Destroyed.png")
        self.source.SetPos(self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.collided:
            self.SmashEffect.Update()
            self.SmashEffect.Redraw()

    def goesFlying(self, directionX, directionY, speed):
        self.speed = speed / self.mass
        self.direction = pygame.math.Vector2(directionX, directionY)


    def update(self):
        #if self.switch and not self.collided:
            #self.collided = True
        if self.collided:
            self.image = self.destroyed
            self.mask = self.destroyedMask
        if self.speed > 0:
            self.rect.x -= self.direction.x * self.speed * 2
            self.rect.y -= self.direction.y * self.speed * 2

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
        
        
        
        
        
