import pygame
import sys
import random as rn

import math

#==================================NOTES=========================
 #make a rectangle class
 #This is Mr. German's code from lab
 #currently reading documentation on pygame and rewatching labs
 #this problem is going to be nuts'
 #https://pygame.readthedocs.io/en/latest/rect/rect.html#a-self-moving-a-rectangle
 #reading some online documentation 
 
"""
import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Colors, ha ha... ")
        self.bg_color = (230, 230, 0)
        self.ship = Ship(self, 100, 150, 60)  
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # if we detect a key is pressed 
                    if event.key == pygame.K_RIGHT: # if it's the right arrow key  
                        self.ship.move(10, 0) # then tell the ship to move
            self.screen.fill(self.bg_color)                    
            self.ship.blitme()
            pygame.display.flip()

class Ship:
    def __init__(self, ai_game, x, y, radius):
        self.screen = ai_game.screen
        (self.x, self.y, self.radius) = (x, y, radius) 
    def blitme(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.radius)
    def move(self, dx, dy): # this is how we do it (move, that is) 
        (self.x, self.y) = (self.x + dx, self.y + dy)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
"""

#===================END OF NOTES==========================






BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = (  0, 255,   0)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
#v = [rn.randint(1, 5), rn.randint(1, 5)]



def main():
    
    rect_x = 50
    rect_y = 50
    
    rectxSpeed = rn.randint(1, 5)
    rectySpeed = rn.randint(1, 5)
    
    pygame.init()
    
    size = [300, 300]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("shakespeare")

    rect = [10, 10, 10, 10]
    rect = pygame.Rect(100, 50, 50, 50)
    
    clock = pygame.time.Clock()
    
    while True:
        pygame.time.wait(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)
        
    
        
        
        #find a way to make the rect colors change
        pygame.draw.rect(screen, RED, [rect_x, rect_y, 10, 10])
        

        #bouncy code

        rect_x += rectxSpeed
        rect_y += rectySpeed

        #the rectangles cords
        # 300screen - 10square = 290
        if rect_y > 290:
        if rect_y<0:
            rectySpeed=-rectySpeed

        if rect_x > 290 or rect_x<0:
            rectxSpeed=-rectxSpeed


        """
        if rect_y > 250 or rect_y < 0:
            rectySpeed = 5
            rect_y = rectySpeed *- (math.pi/2)
        if rect_x > 250 or rect_x < 0:
            rectxSpeed = 5
            rect_x = rectxSpeed *- (math.pi/2)
        """
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
       
       
        
    
"""         
        rect.move_ip(v) #set v up top
        
        if rect.left < -50:
            v[0] *= -1 # (similar to += but multiplies)
        if rect.right > 200: #i had to set this to 100 to get the rectangle to even move
            v[0] *= -1
        if rect.top < 50:
            v[1] *= -1
        if rect.bottom > -50:
            v[1] *= -1
"""        
        
        

       
if __name__ == "__main__":
    main()