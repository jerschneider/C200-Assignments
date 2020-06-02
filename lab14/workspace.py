import sys
import pygame

class oedipusRex: #changed class name (AlienVasion to beep), make sure to keep this consistant                                   # this is the basic setup
    def __init__(self):                       # notice the blank spaces ... 
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800)) #must be a tuple 
        pygame.display.set_caption("a blind oedipus")
        self.bg_color = (230, 230, 0)
        self.count = 0


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.count += 1
            print(self.ship, self.count)

            self.screen.fill(self.bg.color)
            pygame.display.flip()

class ship:
    def __init__(self, ai_game, x, y, radius):
        self.screen = ai_game.screen
        (self.x, self.y, self.radius) = (x, y, radius)





if __name__ == '__main__':
    ai = oedipusRex()      # create game object, invoke its instance method
    ai.run_game()
