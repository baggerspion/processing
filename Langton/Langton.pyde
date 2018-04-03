from random import randint

class Dir: up, right, down, left = range(4)
class Turn: left, right = True, False

class Ant():
    def __init__(self, ant_x, ant_y, dir):
        self.ant_x = ant_x
        self.ant_y = ant_y
        self.dir = dir

    def location(self):
        return self.ant_x + self.ant_y * width        
    
    def move(self, turn):
        self.dir = (4 + self.dir + (1 if turn else -1)) % 4
        self.dir = [Dir.up, Dir.right, Dir.down, Dir.left][self.dir]
        if self.dir == Dir.up: self.ant_y -= 1
        elif self.dir == Dir.right: self.ant_x -= 1
        elif self.dir == Dir.down: self.ant_y += 1
        elif self.dir == Dir.left: self.ant_x += 1
        else: 
            print(self.dir)
            assert False
    
        # Wrap around if needed
        if self.ant_x > width - 1: self.ant_x = 0
        elif self.ant_x < 0: self.ant_x = width - 1
        if self.ant_y > height - 1: self.ant_y = 0
        elif self.ant_y < 0: self.ant_y = height - 1

def setup():
    global ant1, ant2, grid
    
    size(1024, 768)
    
    # Create the inital white image
    grid = createImage(width, height, RGB)
    grid.loadPixels()
    for i in range(len(grid.pixels)):
        grid.pixels[i] = color(255)
    grid.updatePixels()
    
    # Create 2 Ants
    ant1 = Ant(randint(0, width - 1), randint(0, height - 1), [Dir.up, Dir.right, Dir.down, Dir.left][randint(0, 3)])
    ant2 = Ant(randint(0, width - 1), randint(0, height - 1), [Dir.up, Dir.right, Dir.down, Dir.left][randint(0, 3)])

def draw():
    global ant1, ant2, grid
    
    background(255)
    grid.loadPixels()
    
    for n in range(2000):
        for ant in [ant1, ant2]:
            # Find the current pixel location
            pix = ant.location()
        
            # Decide what to do next and then color the square
            turn = Turn.right if grid.pixels[pix] == color(255) else Turn.left
            grid.pixels[pix] = color(0) if grid.pixels[pix] == color(255) else color(255)
            
            # Move forward
            ant.move(turn)
    
    grid.updatePixels()
    image(grid, 0, 0)
