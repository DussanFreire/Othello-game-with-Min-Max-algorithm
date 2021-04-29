import numpy as np
from board import Board
from settings import Settings


class Player:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings


class Token:
    def __init__(self, face_side):
        self.face_side = face_side


class Cell(object):
    pass
    # token
    # def __init__(self, token):
    #    token = token


if __name__ == "__main__":
    settings = Settings()
    token1 = Token(settings.face_up)
    token2 = Token(settings.face_down)


    settings.heuristic = HeuristicFunction().heuristic1
    board = Board(cells)
