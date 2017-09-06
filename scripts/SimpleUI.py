import pygame
from Player import *
from Level import *

def uicreate(Level):
    #create a Font object from the system fonts
    newFont = pygame.font.Font("../font/Old_School_Adventures.ttf",20)
    newFont1 = pygame.font.Font("../font/Old_School_Adventures.ttf", 60)


    scoreSurface = newFont.render((u'Property Damage:'+ '$'), False, [255, 20, 20], None)
    numberSurface = newFont1.render(str(Level.MoneyDamage),False,[255,20,20],None) #render(text, antialias, color, background=None) -> Surface
                                                                #draw text on a new Surface, creates a new Surface with the specified text rendered on it
    return [scoreSurface,numberSurface]


