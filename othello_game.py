from settings import Settings
from heuristiFunctionCollection import HeuristicFunctionCollection
from player import Player
from board import Board
from game import Game

if __name__ == "__main__":
    settings = Settings()
    token1 = settings.p1_token
    token2 = settings.p2_token

    board = Board(settings)
    board.create_empty_board()
    # os.system("cls")   NECESARIO.  Si los colors no funcionan hay que hacer un cls

    player1 = Player("Diego", settings.p1_token)
    player2 = Player("Dussan", settings.p2_token)
    game = Game(board, player1, player2, settings)
    game.play()

""" Colors:
        white = "\033[1;37m"
        green = "\033[0;32m"
        yellow = "\033[1;30m"
        brown = "\033[0;33m"
"""
