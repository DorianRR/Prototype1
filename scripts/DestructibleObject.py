import pygame

class DestructibleObject(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image =  pygame.image.load("../images/" + image + ".png").convert_alpha()
        self.destroyed = pygame.image.load("../images/" + image + "Destroyed.png").convert_alpha()
        
        self.rect  = self.image.get_rect()
        self.rect.topleft = position

        self.mask = pygame.mask.from_surface(self.image)
        self.destroyedMask = pygame.mask.from_surface(self.destroyed)
        self.switch  = False
        self.collided = False

    def update(self):
        if self.switch and not self.collided:
            self.collided = True
            self.image = self.destroyed
            self.mask = self.destroyedMask
        
        
        
        
        
        
