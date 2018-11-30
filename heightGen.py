__Authors__ = "Jakub, Bryn"
__version__ = "0.4"
__lastEdit__ = "30/11/2018 09:23"

import pygame
import random

#
#                USAGE
#       
#    mapArray = genHeightMap(array);
#
#   /currently limited only to 39x39,/
#   /   dunno if I will scale it     /
#

def mapx():
        mapx = 40 # rows for each 10x10 block
        return mapx

def mapy():
        mapy =  40 # columns for each 10x10 block
        return mapy

def genHeightMap():

    throwawayVariable = 0 # Don't worry bout it.
    # lets face it this ^ is a temp variable ~Bryn
    tileHeight = 0
    tileAbove = [[]]
    tileLeft = [[]]

    coords = []

    manipX = 0 # manipulates x without affecting the x variable
    manipY = 0 # manipulates y without affecting the y variable

# takes the extra 10x10 block off, the counting starts from 0 instead of 1
    mapX = mapx()
    mapY = mapy()
    
    mapX -= 1
    mapY -= 1

# generates the list for the coordinates and height map (x, y, height)
    for y in range(mapY, -1, -1):

        if y != 0:
            manipY = y
            manipY = str(manipY) + "0"
            manipY = int(manipY)
        else:
            pass

        for x in range(mapX, -1, -1):

            if x != 0:
                manipX = x
                manipX = str(manipX) + "0"
                manipX = int(manipX)
                
                if y == 0:
                    coords.insert([0][0], [manipX,y])
                else:
                    coords.insert([0][0], [manipX,manipY])

            else:
                if y == 0:
                    coords.insert([0][0], [x,y])
                else:
                    coords.insert([0][0], [x,manipY])

    for xy in range(0, ((mapX+1)*(mapY+1))):         # For every row...     # For every column...
            #print(coords[xy])

            # Height generation code starts here.
            # -----------------------------------
            # This next block of code checks if the tile is the top-left-most tile. If so, generate a random height.

            tileLeft = coords[xy-1]

            tileAbove = coords[xy-mapY]

            if coords[xy][0] == 0:
                if coords[xy][1] != 0:
                    coords[xy].append(tileAbove[2] + random.randrange(-5,5))

            if coords[xy][1] == 0:
                if coords[xy][0] != 0:
                    coords[xy].append(tileLeft[2] + random.randrange(-5,5))
                else:
                    coords[xy].append(random.randrange(-10, 25))
            elif coords[xy][0] != 0 and coords[xy][1] != 0:
                coords[xy].append(((tileAbove[2]+tileLeft[2])/2) + random.randrange(-5,5))
                

    return coords

print("Map array module loaded")