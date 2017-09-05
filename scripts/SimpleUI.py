import pygame
from Player import *
from Level import *

def uicreate(Level):
    fuelFont = pygame.font.SysFont('comicsansms',30,True) #create a Font object from the system fonts
    scoreFont = pygame.font.SysFont('comicsansms',30,True)

    fuelSurface = fuelFont.render(u'Fuel Left: '+str(Level.fuelLevel),True,[20,20,20],None) #render(text, antialias, color, background=None) -> Surface
                                                                #draw text on a new Surface, creates a new Surface with the specified text rendered on it
    scoreSurface = scoreFont.render(u'Property Damage:'+ '$' + str(Level.MoneyDamage), True, [255, 20, 20], None)
    return [fuelSurface,scoreSurface]


