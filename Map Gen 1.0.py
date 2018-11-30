__Author__ = "Bryn, Jakub"
__version__ = "1.0"
__lastEdit__ = "30/11/2018 13:05"

# The while loop will crash if left for too long.  Trying to make sure that doesn't happen by removing display update from the main loop, but it either opens then closes the window really quick or won't display.

import pygame
import random
import math
from heightGen import genHeightMap, mapx, mapy

# TYPE . VALUE . RGB COLOUR
# Snow = 20 -> (242, 242, 242)
# Rocky = 18 -> (173, 173, 173)
# Muddy = 15 -> (178, 167, 141)
# Grass = 10 -> (164, 214, 132)
# Sand = 1 -> (247, 252, 209)
# Sea = 0 -> (173, 234, 255)
# Ocean = -5 -> (92, 158, 181)

screen = pygame.display.set_mode(((mapx()*10), (mapy()*10)))

inActColour = (255, 0, 0)
actColour = (0, 255, 0)

#print(pygame.font.get_fonts())


def button(msg, x, y, bWidth, bHeight, inActColour, actColour):

    mouse = pygame.mouse.get_pos()

    if x+bWidth > mouse[0] > x and y+bHeight > mouse[1] > y:

        pygame.draw.rect(screen, actColour,(x,y,bWidth,bHeight))
    else:

        pygame.draw.rect(screen, inActColour,(x,y,bWidth,bHeight))

    smallText = pygame.font.Font("D:\Fonts\asimov\Asimov.otf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(bWidth/2)), (y+(bHeight/2)) )
    screen.blit(textSurf, textRect)


coords = genHeightMap()

mapLoop = True

while mapLoop:

    button("Jacob", 200, 200, 100, 50, (255, 0, 0), (0, 255, 0))

    for xy in range(0, ((mapx())*(mapy()))):

        posX = coords[xy][0]
        posY = coords[xy][1]
        height = coords[xy][2]

        height = math.floor(height)
        colour = 0

        if height >= 20:
            colour = (242, 242, 242)
        elif height >= 18 and height < 20:
            colour = (173, 173, 173)
        elif height >= 15 and height < 18:
            colour = (178, 167, 141)
        elif height >= 10 and height < 15:
            colour = (164, 214, 132)
        elif height >= 1 and height < 10:
            colour = (247, 252, 209)
        elif height >= 0 and height < 1:
            colour = (173, 234, 255)
        else:
            colour = (92, 158, 181)

        pygame.draw.rect(screen, colour, (posX, posY, 10, 10), 0) #(output, colour, (pos x, pos y, width, height), outline '0' = solid)
        pygame.display.update()

    mapLoop = False
    pygame.display.update()
