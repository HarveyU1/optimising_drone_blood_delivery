import pygame
import time
import math
import numpy as np

screenSize = [1000,1000] #The size in pixels of the screen width and height
screenCentre = [screenSize[0]/2,screenSize[1]/2] #The centre point on the screen at which to reference drawing from

#Initialise screen drawing
pygame.init() #Initialising screen
screen = pygame.display.set_mode((screenSize[0],screenSize[1]),pygame.SRCALPHA,32) #Setting size of window
surface = pygame.Surface((screenSize[0],screenSize[1]), pygame.SRCALPHA)
pygame.display.set_caption('Hospital Map') #Setting title of window
screen.fill((145, 199, 177))#Make Background White
font = pygame.font.SysFont("helvetica", 20)
font2 = pygame.font.SysFont("comicsansms", 20)

#Drawing variables 
hospitalScaleFact = 0.0001
launchPadScaleFact = 0.00002


def drawbuildings(hospitals,airports,droneRange):
    #Draw hospitals
    for h in hospitals:
        surface.fill((255,255,255,0)) #Fill the screen with transparent pixels
        pygame.draw.circle(surface,(227,208,129,255),(int(screenCentre[0]+(int(h[0]))),int(screenCentre[1]+(int(h[1])))),10)
        screen.blit(surface, (0,0))
        text = font.render(str(h[2]), True, (255,255,255))
        screen.blit(text,((int(screenCentre[0]+(int(h[0])))+20,int(screenCentre[1]+(int(h[1])))-10)))


   #Draw airport ranges
    for a in airports:
        surface.fill((255,255,255,0)) #Fill the screen with transparent pixels
        pygame.draw.circle(surface,(145,199,177,60),(int(screenCentre[0]+(int(a[0]))),int(screenCentre[1]+(int(a[1])))),droneRange)
        screen.blit(surface, (0,0))

    #Draw airports
    for a in airports:
        surface.fill((255,255,255,0)) #Fill the screen with transparent pixels
        pygame.draw.circle(surface,(145,199,177,255),(int(screenCentre[0]+(int(a[0]))),int(screenCentre[1]+(int(a[1])))),10)
        screen.blit(surface, (0,0))
        text = font.render(str(a[2]), True, (145,199,177))
        screen.blit(text,((int(screenCentre[0]+(int(a[0])))+30,int(screenCentre[1]+(int(a[1])))-10)))
   
        
def drawGrid(utility):
    #Draw major axis
    surface.fill((255,255,255,0)) #Fill the screen with transparent pixels
    pygame.draw.line(surface, (255, 255, 255, 100), (screenCentre[0],screenSize[1]), (screenCentre[0],0), 3)
    pygame.draw.line(surface, (255, 255, 255, 100), (0,screenCentre[1]), (screenSize[0],screenCentre[1]), 3)

    #Draw minor axis
    for i in range(100,500,100):
        pygame.draw.line(surface, (255, 255, 255, 50), (screenCentre[0]+i,screenSize[1]), (screenCentre[0]+i,0), 1)
        pygame.draw.line(surface, (255, 255, 255, 50), (screenCentre[0]-i,screenSize[1]), (screenCentre[0]-i,0), 1)

        pygame.draw.line(surface, (255, 255, 255, 50), (0,screenCentre[1]+i), (screenSize[0],screenCentre[1]+i), 1)
        pygame.draw.line(surface, (255, 255, 255, 50), (0,screenCentre[1]-i), (screenSize[0],screenCentre[1]-i), 1)
    screen.blit(surface, (0,0))
    
    #Write Utility
    if utility != None:
        text = font.render("Utility = {}".format(utility), True, (255,255,255))
        screen.blit(text,(10,10))


def dispUtilityMap(objVals,sF):
    print("Displaying Utility Map")
    minVal = np.amin(objVals)
    if minVal == 0:
        minVal = 1
        print("minVal is 0")

    print("maxVal is {}".format(minVal))
    for r in range (len(objVals)):
        for c in range (len(objVals[r])):
            brightness = (objVals[r][c]/minVal)**1#this is a number between 0 and 1 We want a small change in x higher up to have a greter effect on y thn lower down
            brightness = brightness *255
            if brightness > 254:
                color = (0,255,255,int(np.clip(brightness, 0,255)))
            else:
                color = (brightness, 0 , 255-brightness, int(np.clip(brightness, 0,255)))
            pygame.draw.circle(surface, color, (c*sF, r*sF), int(sF/2))
    screen.blit(surface, (0,0))



#Given an array of hospital, airports and droneRange draw the map
def drawMap(hospitals,airports,droneRange,utility = None,objVals = None, sF = 1):
    #while (True==True): 
    screen.fill((0, 0, 0))
    drawGrid(utility)

    if objVals is None:
        print("not displaying utility map")
    else:
        dispUtilityMap(objVals,sF)

    drawbuildings(hospitals,airports,droneRange)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #time.sleep(0.1)