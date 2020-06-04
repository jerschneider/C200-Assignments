class Ship:
    def __init__(self, game, x, y, radius):

        (self.x, self.y, self.radius) = (x, y, radius)
    

if __name__ == '__main__':
    one = Ship(None, 20, 30, 5)
    two = Ship(None, 120, -30, 50) 
    print(one.radius)
    print(two)