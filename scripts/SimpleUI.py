import pygame
from Player import *
def uicreate(Player):
    fuelFont = pygame.font.SysFont('comicsansms',30,True) #create a Font object from the system fonts
    scoreFont = pygame.font.SysFont('comicsansms',30,True)

    fuelSurface = fuelFont.render(u'Fuel Left: '+str(Player.fuelLevel),True,[220,220,220],None) #render(text, antialias, color, background=None) -> Surface
                                                                #draw text on a new Surface, creates a new Surface with the specified text rendered on it
    scoreSurface = scoreFont.render(u'EAE money lost:'+str(Player.MoneyDamage)+'$', True, [220, 220, 220], None)
    return [fuelSurface,scoreSurface]