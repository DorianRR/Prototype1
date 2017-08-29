import pygame

class DestructibleObject(pygame.sprite.Sprite):

    def __init__(self, image, position):

        pygame.sprite.Sprite.__init__(self) #When subclassing the Sprite, be sure to call the base initializer before adding the Sprite to Groups
        self.image =  pygame.image.load("../images/" + image + ".png").convert_alpha()
        #elf.destroyed = pygame.image.load("../images/" + image + "Destroyed.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.mask = pygame.mask.from_surface(self.image)
        #self.destroyedMask = pygame.mask.from_surface(self.destroyed)
        self.switch  = False
        self.collided = False

    def update(self):
        if self.switch and not self.collided:
            self.collided = True
            self.image = self.destroyed
            self.mask = self.destroyedMask
        
        
        
        
        
        
