import pygame
import sys
import random as rn

#==================================NOTES=========================
 #make a rectangle class
 #This is Mr. German's code from lab
 #currently reading documentation on pygame and rewatching labs
 #this problem is going to be nuts'
 #https://pygame.readthedocs.io/en/latest/rect/rect.html#a-self-moving-a-rectangle
 #reading some online documentation 

BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = (  0, 255,   0)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
##additional colors
DARKGREEN = (5, 179, 40)
DARKYELLOW = (209, 198, 48)
LIGHTBLUE = (121, 142, 229)
ORANGE = (255, 147, 51)

def main():
    ##
    #these guys placed here because they need to be referenced before assignment later in the code
    recColors = RED
    rect_x = 50
    rect_y = 50
    rectxSpeed = rn.randint(1, 5)
    rectySpeed = rn.randint(1, 5)
    ##

    pygame.init()
    
    size = [300, 300]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("shakespeare")

    #rect = [10, 10, 10, 10] ##didnt need this
        
    while True:
        pygame.time.wait(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)

        #find a way to make the rect colors change
        #this is my rec code
        pygame.draw.rect(screen, recColors, [rect_x, rect_y, 10, 10])
        

        #bouncy code

        rect_x += rectxSpeed
        rect_y += rectySpeed

        #the rectangles cords
        # 300screen - 10rec = 290
        #split this up to perform color switch method
        if rect_y > 290: # bottom of screen
            #negative needed to be here to change direction
            rectySpeed = rn.randint(-5, -1) #lol had to switch the range
            recColors = ORANGE
            #a orange
            #pygame.draw.rect(screen, recColors, [rect_x, rect_y, 10, 10])

        if rect_y < 0: # top of screen
            rectySpeed = rn.randint(1, 5)
            recColors = DARKGREEN
            #A dark green
            #pygame.draw.rect(screen, recColors, [rect_x, rect_y, 10, 10])

        if rect_x > 290: #right of screen
            rectxSpeed = rn.randint(-5, -1)
            recColors = LIGHTBLUE
            #a light blue
            #pygame.draw.rect(screen, recColors, [rect_x, rect_y, 10, 10])
        if rect_x < 0: #left of screen
            rectxSpeed = rn.randint(1, 5)
            recColors = DARKYELLOW
            # a dark yellow
            #pygame.draw.rect(screen, recColors, [rect_x, rect_y, 10, 10])

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()