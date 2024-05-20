import pyxel
import Display
import GameBoard
import Player
import Enemy

board = GameBoard.Board()
player = Player.Player([0, 0])
actinput = None

enemy1 = Enemy.Enemy([0, 1], player, board)

class App:
    def __init__(self):
        pyxel.init(160, 160)
        pyxel.run(self.update, self.draw)

    def update(self):
        player.update(board)
        

    def draw(self):
        pyxel.cls(0)
        Display.draw(board, player)
        
        
App()