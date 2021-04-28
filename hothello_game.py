import numpy as np
import os

class Settings:
    face_up = 'O'
    face_down = 'X'
    heuristic = None

class HeuristicFunction:
    def heuristic1(self):
        print("Nice hothello heuristic")

class Player:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings

class Token:
    def __init__(self, face_side):
        self.face_side = face_side


class Cell(object):
    def __init__(self, token="_"):
        self.token = token

class Board:
    def __init__(self, cells, size=8):
        self.size = size
        self.cells = cells
    
    def draw_board(self, fmt="g"):
        white = "\033[1;37m"
        color = "\033[0;33m"
        numbers = range(1,9)
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        i = 0
        print(color,"\n")
        
        for n in numbers:
            print(n, end="     ")
        print("\n")

        for row in cells:
            for cell in row:
                print(cell.token, end="     ")
            print("",numbers[i] ,"\n")
            i = i + 1
        print(white, "\n")


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
    
    # os.system("cls")   NECESARIO.  Si los coclores no funcionan hay que hacer un cls
    board.draw_board()


""" Colors:
        white = "\033[1;37m"
        green = "\033[0;32m"
        yellow = "\033[1;30m"
        brown = "\033[0;33m"
        """