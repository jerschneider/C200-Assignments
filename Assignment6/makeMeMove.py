import pygame
import sys
import random as rn

 
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