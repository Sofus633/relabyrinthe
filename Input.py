import pyxel


def checkinputs():
    """ take input and return as [[keys pressed], [mousepos]]"""
    keypress = [[], []]
    if pyxel.btn(pyxel.KEY_D):
        keypress[0].append("d") 
        
    if pyxel.btn(pyxel.KEY_Q):
        keypress[0].append("q") 
        
    if pyxel.btn(pyxel.KEY_Z):
        keypress[0].append("z") 
        
    if pyxel.btn(pyxel.KEY_S):
        keypress[0].append("s") 
        
    keypress[1] = pyxel.mouse_x, pyxel.mouse_y
    
    return keypress