import pygame
from Player import *
from Level import *

def uicreate(Level):
    #create a Font object from the system fonts
    scoreFont = pygame.font.SysFont('comicsansms',32,True)
    numberFont = pygame.font.SysFont('comicsansms', 125, True)

    scoreSurface = scoreFont.render((u'Property Damage:'+ '$'), True, [255, 20, 20], None)
    numberSurface = numberFont.render(str(Level.MoneyDamage),True,[255,20,20],None) #render(text, antialias, color, background=None) -> Surface
                                                                #draw text on a new Surface, creates a new Surface with the specified text rendered on it
    return [numberSurface,scoreSurface]


