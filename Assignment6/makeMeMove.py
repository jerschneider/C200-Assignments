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




def main():

    pygame.init()
        
    size = [700, 700]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("a magical rectangle")

    rect = [10, 10, 10, 10]
    rect = pygame.Rect(100, 50, 50, 50)
    v = [2, 2]
    while True:
        pygame.time.wait(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, rect)
        pygame.display.flip()
        
    
                
        rect.move_ip(v) #set v up top
        
        if rect.left < -50:
            v[0] *= -1 # (similar to += but multiplies)
        if rect.right > 200: #i had to set this to 100 to get the rectangle to even move
            v[0] *= -1
        if rect.top < 50:
            v[1] *= -1
        if rect.bottom > -50:
            v[1] *= -1
                
        
    
    #pygame.quit()

       
if __name__ == "__main__":
    main()