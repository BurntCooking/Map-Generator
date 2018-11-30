import pygame
import random

# TYPE . VALUE . RGB COLOUR
# Snow = 20 -> (242, 242, 242)
# Rocky = 18 -> (173, 173, 173)
# Muddy = 15 -> (178, 167, 141)
# Grass = 10 -> (164, 214, 132)
# Sand = 1 -> (247, 252, 209)
# Sea = 0 -> (173, 234, 255)
# Ocean = -5 -> (92, 158, 181)

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))

#Map coordinates list.  Coordinates are the top left of each 10x10 square
coords = [[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0],[60,0],[70,0],[80,0],[90,0],[100,0],[110,0],[120,0],[130,0],[140,0],[150,0],[160,0],[170,0],[180,0],[190,0],[200,0],[210,0],[220,0],[230,0],[240,0],[250,0],[260,0],[270,0],[280,0],[290,0],[300,0],[310,0],[320,0],[330,0],[340,0],[350,0],[360,0],[370,0],[380,0],[390,0]], 
[[0,10],[10,10],[20,10],[30,10],[40,10],[50,10],[60,10],[70,10],[80,10],[90,10],[100,10],[110,10],[120,10],[130,10],[140,10],[150,10],[160,10],[170,10],[180,10],[190,10],[200,10],[210,10],[220,10],[230,10],[240,10],[250,10],[260,10],[270,10],[280,10],[290,10],[300,10],[310,10],[320,10],[330,10],[340,10],[350,10],[360,10],[370,10],[380,10],[390,10]], 
[[0,20],[10,20],[20,20],[30,20],[40,20],[50,20],[60,20],[70,20],[80,20],[90,20],[100,20],[110,20],[120,20],[130,20],[140,20],[150,20],[160,20],[170,20],[180,20],[190,20],[200,20],[210,20],[220,20],[230,20],[240,20],[250,20],[260,20],[270,20],[280,20],[290,20],[300,20],[310,20],[320,20],[330,20],[340,20],[350,20],[360,20],[370,20],[380,20],[390,20]], 
[[0,30],[10,30],[20,30],[30,30],[40,30],[50,30],[60,30],[70,30],[80,30],[90,30],[100,30],[110,30],[120,30],[130,30],[140,30],[150,30],[160,30],[170,30],[180,30],[190,30],[200,30],[210,30],[220,30],[230,30],[240,30],[250,30],[260,30],[270,30],[280,30],[290,30],[300,30],[310,30],[320,30],[330,30],[340,30],[350,30],[360,30],[370,30],[380,30],[390,30]], 
[[0,40],[10,40],[20,40],[30,40],[40,40],[50,40],[60,40],[70,40],[80,40],[90,40],[100,40],[110,40],[120,40],[130,40],[140,40],[150,40],[160,40],[170,40],[180,40],[190,40],[200,40],[210,40],[220,40],[230,40],[240,40],[250,40],[260,40],[270,40],[280,40],[290,40],[300,40],[310,40],[320,40],[330,40],[340,40],[350,40],[360,40],[370,40],[380,40],[390,40]], 
[[0,50],[10,50],[20,50],[30,50],[40,50],[50,50],[60,50],[70,50],[80,50],[90,50],[100,50],[110,50],[120,50],[130,50],[140,50],[150,50],[160,50],[170,50],[180,50],[190,50],[200,50],[210,50],[220,50],[230,50],[240,50],[250,50],[260,50],[270,50],[280,50],[290,50],[300,50],[310,50],[320,50],[330,50],[340,50],[350,50],[360,50],[370,50],[380,50],[390,50]], 
[[0,60],[10,60],[20,60],[30,60],[40,60],[50,60],[60,60],[70,60],[80,60],[90,60],[100,60],[110,60],[120,60],[130,60],[140,60],[150,60],[160,60],[170,60],[180,60],[190,60],[200,60],[210,60],[220,60],[230,60],[240,60],[250,60],[260,60],[270,60],[280,60],[290,60],[300,60],[310,60],[320,60],[330,60],[340,60],[350,60],[360,60],[370,60],[380,60],[390,60]], 
[[0,70],[10,70],[20,70],[30,70],[40,70],[50,70],[60,70],[70,70],[80,70],[90,70],[100,70],[110,70],[120,70],[130,70],[140,70],[150,70],[160,70],[170,70],[180,70],[190,70],[200,70],[210,70],[220,70],[230,70],[240,70],[250,70],[260,70],[270,70],[280,70],[290,70],[300,70],[310,70],[320,70],[330,70],[340,70],[350,70],[360,70],[370,70],[380,70],[390,70]], 
[[0,80],[10,80],[20,80],[30,80],[40,80],[50,80],[60,80],[70,80],[80,80],[90,80],[100,80],[110,80],[120,80],[130,80],[140,80],[150,80],[160,80],[170,80],[180,80],[190,80],[200,80],[210,80],[220,80],[230,80],[240,80],[250,80],[260,80],[270,80],[280,80],[290,80],[300,80],[310,80],[320,80],[330,80],[340,80],[350,80],[360,80],[370,80],[380,80],[390,80]], 
[[0,90],[10,90],[20,90],[30,90],[40,90],[50,90],[60,90],[70,90],[80,90],[90,90],[100,90],[110,90],[120,90],[130,90],[140,90],[150,90],[160,90],[170,90],[180,90],[190,90],[200,90],[210,90],[220,90],[230,90],[240,90],[250,90],[260,90],[270,90],[280,90],[290,90],[300,90],[310,90],[320,90],[330,90],[340,90],[350,90],[360,90],[370,90],[380,90],[390,90]], 
[[0,100],[10,100],[20,100],[30,100],[40,100],[50,100],[60,100],[70,100],[80,100],[90,100],[100,100],[110,100],[120,100],[130,100],[140,100],[150,100],[160,100],[170,100],[180,100],[190,100],[200,100],[210,100],[220,100],[230,100],[240,100],[250,100],[260,100],[270,100],[280,100],[290,100],[300,100],[310,100],[320,100],[330,100],[340,100],[350,100],[360,100],[370,100],[380,100],[390,100]], 
[[0,110],[10,110],[20,110],[30,110],[40,110],[50,110],[60,110],[70,110],[80,110],[90,110],[100,110],[110,110],[120,110],[130,110],[140,110],[150,110],[160,110],[170,110],[180,110],[190,110],[200,110],[210,110],[220,110],[230,110],[240,110],[250,110],[260,110],[270,110],[280,110],[290,110],[300,110],[310,110],[320,110],[330,110],[340,110],[350,110],[360,110],[370,110],[380,110],[390,110]], 
[[0,120],[10,120],[20,120],[30,120],[40,120],[50,120],[60,120],[70,120],[80,120],[90,120],[100,120],[110,120],[120,120],[130,120],[140,120],[150,120],[160,120],[170,120],[180,120],[190,120],[200,120],[210,120],[220,120],[230,120],[240,120],[250,120],[260,120],[270,120],[280,120],[290,120],[300,120],[310,120],[320,120],[330,120],[340,120],[350,120],[360,120],[370,120],[380,120],[390,120]], 
[[0,130],[10,130],[20,130],[30,130],[40,130],[50,130],[60,130],[70,130],[80,130],[90,130],[100,130],[110,130],[120,130],[130,130],[140,130],[150,130],[160,130],[170,130],[180,130],[190,130],[200,130],[210,130],[220,130],[230,130],[240,130],[250,130],[260,130],[270,130],[280,130],[290,130],[300,130],[310,130],[320,130],[330,130],[340,130],[350,130],[360,130],[370,130],[380,130],[390,130]], 
[[0,140],[10,140],[20,140],[30,140],[40,140],[50,140],[60,140],[70,140],[80,140],[90,140],[100,140],[110,140],[120,140],[130,140],[140,140],[150,140],[160,140],[170,140],[180,140],[190,140],[200,140],[210,140],[220,140],[230,140],[240,140],[250,140],[260,140],[270,140],[280,140],[290,140],[300,140],[310,140],[320,140],[330,140],[340,140],[350,140],[360,140],[370,140],[380,140],[390,140]], 
[[0,150],[10,150],[20,150],[30,150],[40,150],[50,150],[60,150],[70,150],[80,150],[90,150],[100,150],[110,150],[120,150],[130,150],[140,150],[150,150],[160,150],[170,150],[180,150],[190,150],[200,150],[210,150],[220,150],[230,150],[240,150],[250,150],[260,150],[270,150],[280,150],[290,150],[300,150],[310,150],[320,150],[330,150],[340,150],[350,150],[360,150],[370,150],[380,150],[390,150]], 
[[0,160],[10,160],[20,160],[30,160],[40,160],[50,160],[60,160],[70,160],[80,160],[90,160],[100,160],[110,160],[120,160],[130,160],[140,160],[150,160],[160,160],[170,160],[180,160],[190,160],[200,160],[210,160],[220,160],[230,160],[240,160],[250,160],[260,160],[270,160],[280,160],[290,160],[300,160],[310,160],[320,160],[330,160],[340,160],[350,160],[360,160],[370,160],[380,160],[390,160]], 
[[0,170],[10,170],[20,170],[30,170],[40,170],[50,170],[60,170],[70,170],[80,170],[90,170],[100,170],[110,170],[120,170],[130,170],[140,170],[150,170],[160,170],[170,170],[180,170],[190,170],[200,170],[210,170],[220,170],[230,170],[240,170],[250,170],[260,170],[270,170],[280,170],[290,170],[300,170],[310,170],[320,170],[330,170],[340,170],[350,170],[360,170],[370,170],[380,170],[390,170]], 
[[0,180],[10,180],[20,180],[30,180],[40,180],[50,180],[60,180],[70,180],[80,180],[90,180],[100,180],[110,180],[120,180],[130,180],[140,180],[150,180],[160,180],[170,180],[180,180],[190,180],[200,180],[210,180],[220,180],[230,180],[240,180],[250,180],[260,180],[270,180],[280,180],[290,180],[300,180],[310,180],[320,180],[330,180],[340,180],[350,180],[360,180],[370,180],[380,180],[390,180]], 
[[0,190],[10,190],[20,190],[30,190],[40,190],[50,190],[60,190],[70,190],[80,190],[90,190],[100,190],[110,190],[120,190],[130,190],[140,190],[150,190],[160,190],[170,190],[180,190],[190,190],[200,190],[210,190],[220,190],[230,190],[240,190],[250,190],[260,190],[270,190],[280,190],[290,190],[300,190],[310,190],[320,190],[330,190],[340,190],[350,190],[360,190],[370,190],[380,190],[390,190]], 
[[0,200],[10,200],[20,200],[30,200],[40,200],[50,200],[60,200],[70,200],[80,200],[90,200],[100,200],[110,200],[120,200],[130,200],[140,200],[150,200],[160,200],[170,200],[180,200],[190,200],[200,200],[210,200],[220,200],[230,200],[240,200],[250,200],[260,200],[270,200],[280,200],[290,200],[300,200],[310,200],[320,200],[330,200],[340,200],[350,200],[360,200],[370,200],[380,200],[390,200]], 
[[0,210],[10,210],[20,210],[30,210],[40,210],[50,210],[60,210],[70,210],[80,210],[90,210],[100,210],[110,210],[120,210],[130,210],[140,210],[150,210],[160,210],[170,210],[180,210],[190,210],[200,210],[210,210],[220,210],[230,210],[240,210],[250,210],[260,210],[270,210],[280,210],[290,210],[300,210],[310,210],[320,210],[330,210],[340,210],[350,210],[360,210],[370,210],[380,210],[390,210]], 
[[0,220],[10,220],[20,220],[30,220],[40,220],[50,220],[60,220],[70,220],[80,220],[90,220],[100,220],[110,220],[120,220],[130,220],[140,220],[150,220],[160,220],[170,220],[180,220],[190,220],[200,220],[210,220],[220,220],[230,220],[240,220],[250,220],[260,220],[270,220],[280,220],[290,220],[300,220],[310,220],[320,220],[330,220],[340,220],[350,220],[360,220],[370,220],[380,220],[390,220]], 
[[0,230],[10,230],[20,230],[30,230],[40,230],[50,230],[60,230],[70,230],[80,230],[90,230],[100,230],[110,230],[120,230],[130,230],[140,230],[150,230],[160,230],[170,230],[180,230],[190,230],[200,230],[210,230],[220,230],[230,230],[240,230],[250,230],[260,230],[270,230],[280,230],[290,230],[300,230],[310,230],[320,230],[330,230],[340,230],[350,230],[360,230],[370,230],[380,230],[390,230]], 
[[0,240],[10,240],[20,240],[30,240],[40,240],[50,240],[60,240],[70,240],[80,240],[90,240],[100,240],[110,240],[120,240],[130,240],[140,240],[150,240],[160,240],[170,240],[180,240],[190,240],[200,240],[210,240],[220,240],[230,240],[240,240],[250,240],[260,240],[270,240],[280,240],[290,240],[300,240],[310,240],[320,240],[330,240],[340,240],[350,240],[360,240],[370,240],[380,240],[390,240]], 
[[0,250],[10,250],[20,250],[30,250],[40,250],[50,250],[60,250],[70,250],[80,250],[90,250],[100,250],[110,250],[120,250],[130,250],[140,250],[150,250],[160,250],[170,250],[180,250],[190,250],[200,250],[210,250],[220,250],[230,250],[240,250],[250,250],[260,250],[270,250],[280,250],[290,250],[300,250],[310,250],[320,250],[330,250],[340,250],[350,250],[360,250],[370,250],[380,250],[390,250]], 
[[0,260],[10,260],[20,260],[30,260],[40,260],[50,260],[60,260],[70,260],[80,260],[90,260],[100,260],[110,260],[120,260],[130,260],[140,260],[150,260],[160,260],[170,260],[180,260],[190,260],[200,260],[210,260],[220,260],[230,260],[240,260],[250,260],[260,260],[270,260],[280,260],[290,260],[300,260],[310,260],[320,260],[330,260],[340,260],[350,260],[360,260],[370,260],[380,260],[390,260]], 
[[0,270],[10,270],[20,270],[30,270],[40,270],[50,270],[60,270],[70,270],[80,270],[90,270],[100,270],[110,270],[120,270],[130,270],[140,270],[150,270],[160,270],[170,270],[180,270],[190,270],[200,270],[210,270],[220,270],[230,270],[240,270],[250,270],[260,270],[270,270],[280,270],[290,270],[300,270],[310,270],[320,270],[330,270],[340,270],[350,270],[360,270],[370,270],[380,270],[390,270]], 
[[0,280],[10,280],[20,280],[30,280],[40,280],[50,280],[60,280],[70,280],[80,280],[90,280],[100,280],[110,280],[120,280],[130,280],[140,280],[150,280],[160,280],[170,280],[180,280],[190,280],[200,280],[210,280],[220,280],[230,280],[240,280],[250,280],[260,280],[270,280],[280,280],[290,280],[300,280],[310,280],[320,280],[330,280],[340,280],[350,280],[360,280],[370,280],[380,280],[390,280]], 
[[0,290],[10,290],[20,290],[30,290],[40,290],[50,290],[60,290],[70,290],[80,290],[90,290],[100,290],[110,290],[120,290],[130,290],[140,290],[150,290],[160,290],[170,290],[180,290],[190,290],[200,290],[210,290],[220,290],[230,290],[240,290],[250,290],[260,290],[270,290],[280,290],[290,290],[300,290],[310,290],[320,290],[330,290],[340,290],[350,290],[360,290],[370,290],[380,290],[390,290]], 
[[0,300],[10,300],[20,300],[30,300],[40,300],[50,300],[60,300],[70,300],[80,300],[90,300],[100,300],[110,300],[120,300],[130,300],[140,300],[150,300],[160,300],[170,300],[180,300],[190,300],[200,300],[210,300],[220,300],[230,300],[240,300],[250,300],[260,300],[270,300],[280,300],[290,300],[300,300],[310,300],[320,300],[330,300],[340,300],[350,300],[360,300],[370,300],[380,300],[390,300]], 
[[0,310],[10,310],[20,310],[30,310],[40,310],[50,310],[60,310],[70,310],[80,310],[90,310],[100,310],[110,310],[120,310],[130,310],[140,310],[150,310],[160,310],[170,310],[180,310],[190,310],[200,310],[210,310],[220,310],[230,310],[240,310],[250,310],[260,310],[270,310],[280,310],[290,310],[300,310],[310,310],[320,310],[330,310],[340,310],[350,310],[360,310],[370,310],[380,310],[390,310]], 
[[0,320],[10,320],[20,320],[30,320],[40,320],[50,320],[60,320],[70,320],[80,320],[90,320],[100,320],[110,320],[120,320],[130,320],[140,320],[150,320],[160,320],[170,320],[180,320],[190,320],[200,320],[210,320],[220,320],[230,320],[240,320],[250,320],[260,320],[270,320],[280,320],[290,320],[300,320],[310,320],[320,320],[330,320],[340,320],[350,320],[360,320],[370,320],[380,320],[390,320]], 
[[0,330],[10,330],[20,330],[30,330],[40,330],[50,330],[60,330],[70,330],[80,330],[90,330],[100,330],[110,330],[120,330],[130,330],[140,330],[150,330],[160,330],[170,330],[180,330],[190,330],[200,330],[210,330],[220,330],[230,330],[240,330],[250,330],[260,330],[270,330],[280,330],[290,330],[300,330],[310,330],[320,330],[330,330],[340,330],[350,330],[360,330],[370,330],[380,330],[390,330]], 
[[0,340],[10,340],[20,340],[30,340],[40,340],[50,340],[60,340],[70,340],[80,340],[90,340],[100,340],[110,340],[120,340],[130,340],[140,340],[150,340],[160,340],[170,340],[180,340],[190,340],[200,340],[210,340],[220,340],[230,340],[240,340],[250,340],[260,340],[270,340],[280,340],[290,340],[300,340],[310,340],[320,340],[330,340],[340,340],[350,340],[360,340],[370,340],[380,340],[390,340]], 
[[0,350],[10,350],[20,350],[30,350],[40,350],[50,350],[60,350],[70,350],[80,350],[90,350],[100,350],[110,350],[120,350],[130,350],[140,350],[150,350],[160,350],[170,350],[180,350],[190,350],[200,350],[210,350],[220,350],[230,350],[240,350],[250,350],[260,350],[270,350],[280,350],[290,350],[300,350],[310,350],[320,350],[330,350],[340,350],[350,350],[360,350],[370,350],[380,350],[390,350]], 
[[0,360],[10,360],[20,360],[30,360],[40,360],[50,360],[60,360],[70,360],[80,360],[90,360],[100,360],[110,360],[120,360],[130,360],[140,360],[150,360],[160,360],[170,360],[180,360],[190,360],[200,360],[210,360],[220,360],[230,360],[240,360],[250,360],[260,360],[270,360],[280,360],[290,360],[300,360],[310,360],[320,360],[330,360],[340,360],[350,360],[360,360],[370,360],[380,360],[390,360]], 
[[0,370],[10,370],[20,370],[30,370],[40,370],[50,370],[60,370],[70,370],[80,370],[90,370],[100,370],[110,370],[120,370],[130,370],[140,370],[150,370],[160,370],[170,370],[180,370],[190,370],[200,370],[210,370],[220,370],[230,370],[240,370],[250,370],[260,370],[270,370],[280,370],[290,370],[300,370],[310,370],[320,370],[330,370],[340,370],[350,370],[360,370],[370,370],[380,370],[390,370]], 
[[0,380],[10,380],[20,380],[30,380],[40,380],[50,380],[60,380],[70,380],[80,380],[90,380],[100,380],[110,380],[120,380],[130,380],[140,380],[150,380],[160,380],[170,380],[180,380],[190,380],[200,380],[210,380],[220,380],[230,380],[240,380],[250,380],[260,380],[270,380],[280,380],[290,380],[300,380],[310,380],[320,380],[330,380],[340,380],[350,380],[360,380],[370,380],[380,380],[390,380]], 
[[0,390],[10,390],[20,390],[30,390],[40,390],[50,390],[60,390],[70,390],[80,390],[90,390],[100,390],[110,390],[120,390],[130,390],[140,390],[150,390],[160,390],[170,390],[180,390],[190,390],[200,390],[210,390],[220,390],[230,390],[240,390],[250,390],[260,390],[270,390],[280,390],[290,390],[300,390],[310,390],[320,390],[330,390],[340,390],[350,390],[360,390],[370,390],[380,390],[390,390]]]


loop = True

while loop == True:
    for x in range(40):
        for y in range(40):
            getCo = coords[x][y]
            getCo = str(getCo)

            getCo = getCo.lstrip("[")
            getCo = getCo.rstrip("]")

            posX = ""
            posY = ""

            for i in getCo:
                if i != ",":
                    posX = posX + i
                else:
                    getCo = getCo.lstrip(posX)
                    getCo = getCo.lstrip(",")
                    getCo = getCo.lstrip(" ")
                    break
        
            for i in getCo:
                if i != " ":
                    posY = posY + i
                else:
                    break

            posX = int(posX)
            posY = int(posY)

            pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (posX, posY, 10, 10), 0) #(output, colour, (pos x, pos y, width, height), outline '0' = solid)
            pygame.display.update()