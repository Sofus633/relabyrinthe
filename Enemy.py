import Pathfinding

class Enemy:
    def __init__(self, pos,target, board):
        self.position = pos 
        self.target = target
        self.board =board
    def update(self):
        self.position = Pathfinding.path(self.position, self.target.position, self.board)
    
        