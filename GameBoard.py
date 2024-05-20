import pyxel
import random
class Board:
    def __init__(self):
        self.tab = [[ [0] for i in range(20) ] for i in range(20)]
        self.tab[0][0] = 1
        self.walls = [[0, 1], [4, 1]]
        self.randomwall()
    
    def draw(self):
        for y in range(len(self.tab)):
            for x in range(len(self.tab[y])):
                
                if self.tab[y][x] == 0:
                    pyxel.rect(y*8, x*8, 8, 8, 0)
                    
                if self.tab[y][x] == 1:
                    pyxel.rect(y*8, x*8, 8, 8, 1)
                    
                
    
    def randomwall(self):
        for i in range(20):
            random_x = random.randint(0, 19)
            random_y = random.randint(0, 19)
            self.walls.append([random_x, random_y])
            self.tab[random_x][random_y] = 1