import pygame

def spriteSheetToList( sourceImage, numberColumns):
    imageList = []
    sourceRect = sourceImage.get_rect()
    spriteWidth = sourceRect.width / numberColumns
    spriteHeight = sourceRect.height

    for columns in range(numberColumns):
        subImage = sourceImage.subsurface(pygame.Rect((spriteWidth*columns,0),
                                                      (spriteWidth,spriteHeight)))
        imageList.append(subImage)

    return imageList
