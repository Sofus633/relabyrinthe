import pyxel
import Input

class Player:
    
    def __init__(self, pos):
        self.position = pos
        
    def update(self, board):
        input = Input.checkinputs()
        print(self.position, input)

        if "d" in input[0] or "q" in input[0] :
            self.position[0] += 1 if "d" in input[0] else -1
            if self.position in board.walls:
                self.position[0] += -1 if "d" in input[0] else 1
            
        if "z" in input[0]  or "s" in input[0]:
            self.position[1] += 1 if "s" in input[0] else -1
            if self.position in board.walls:
                self.position[1] += -1 if "s" in input[0] else 1

            
                    
    def draw(self):
        pyxel.rect(self.position[0]*8, self.position[1]*8, 8, 8, 6)