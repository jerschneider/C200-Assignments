import pygame
import sys
import random as rn

 #make a rectangle class
 #This is Mr. German's code from lab
 #currently reading documentation on pygame and rewatching labs
 #this problem is going to be nuts'
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
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = (  0, 255,   0)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)



def main():
    pygame.init()
        
    size = [300, 300]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("C200 CHANGE")

    r = [10, 10, 10, 10]

    while True:
        
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
        screen.fill(WHITE)
    
        pygame.draw.rect(screen, RED, r)

        pygame.display.flip()

if __name__ == "__main__":
    main()