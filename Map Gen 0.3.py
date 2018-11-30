__Author__ = "Bryn, Jakub"
__version__ = "0.3"
__lastEdit__ = "27/11/2018"

# The while loop will crash if left for too long.  Trying to make sure that doesn't happen by removing display update from the main loop, but it either opens then closes the window really quick or won't display.

import pygame
import random
import math
from heightGen import genHeightMap

# TYPE . VALUE . RGB COLOUR
# Snow = 20 -> (242, 242, 242)
# Rocky = 18 -> (173, 173, 173)
# Muddy = 15 -> (178, 167, 141)
# Grass = 10 -> (164, 214, 132)
# Sand = 1 -> (247, 252, 209)
# Sea = 0 -> (173, 234, 255)
# Ocean = -5 -> (92, 158, 181)
mapX = 10 # rows for each 10x10 block
mapY =  10
screen = pygame.display.set_mode(((mapX*10), (mapY*10)))

coords = genHeightMap()

mapLoop = True

while mapLoop:
    for xy in range(0, ((mapX+1)*(mapY+1))):

        posX = coords[xy][0]
        posY = coords[xy][1]
        height = coords[xy][2]

        height = math.floor(height)


        if height == 20:
            colour = (242, 242, 242)
        elif height >= 18 and height < 20:
            colour = (173, 173, 173)
        elif height >= 15 and height < 18:
            colour = (178, 167, 141)
        elif height >= 10 and height < 15:
            colour= (164, 214, 132)
        elif height >= 1 and height < 10:
            colour= (247, 252, 209)
        elif height >= 0 and height < 1:
            colour= (173, 234, 255)
        elif height <= -5:
            colour= (92, 158, 181)

        pygame.draw.rect((screen, colour), (posX, posY, 10, 10), 0) #(output, colour, (pos x, pos y, width, height), outline '0' = solid)
        pygame.display.update()