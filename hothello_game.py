import numpy as np

class Settings:
    face_up = 'O'
    face_down = 'X'
    heuristic = None

class HeuristicFunction:
    def heuristic1(self):
        print("Nice hothello heuristic")

class Player:
    def __init__(self, name, settings):
        name = name
        settings = settings

class Token:
    def __init__(self, face_side):
        face_side = face_side


class Cell(object):
    pass
    #token
    #def __init__(self, token):
    #    token = token

class Board:
    def __init__(self, cells, size=8):
        size = size
        cells = cells

if __name__ == "__main__":
    settings = Settings()
    token1 = Token(settings.face_up)
    token2 = Token(settings.face_down)
    cells = np.array([[Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
                    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]])

    
    settings.heuristic = HeuristicFunction().heuristic1
    board = Board(cells)
