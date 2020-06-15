import pygame, sys
import math
from pygame.locals import *
import random as rn

pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')


def triangle(loc,width):
    """
    Takes in a location to draw the triangle, and width of each side of the 
    the equilateral triangle. 

    Follow the image presented in the documentation. 

    Return a tuple of 3 points, representing the triangle. 
    """
    #pass # TODO: Implement function
    points = math.sqrt((3/4) * (width**2) )
    bot, left, right = (loc[0] + width / 2, loc[1] + points), (loc), (loc[0] + width, loc[1])
    return (bot, left, right)
    
    #(x, y) = loc
    #return ((1, 2), (2, 3), (3, 4))

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, BLUE , (triangle(loc,w)),1)
#INPUT location and width
#RETURN nothing -- follows algorithm

def s(loc,width):
    """
    Given the starting drawing location, and width of each side of the triangle.

    Complete the recursive function.
    """
    #pass # TODO: Implement Function
    x, y = loc
    if width > 1:
        draw_triangle(loc, width)
        points = manth.sqrt((3/4) * width**2)
        s((loc[0] + width/4, loc[1] + points/2), width/2)
        s(loc, width/2)


#s((10,10),440)

while True:
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [0, 0, 500, 400], 2) # Used to show the bounds
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
	