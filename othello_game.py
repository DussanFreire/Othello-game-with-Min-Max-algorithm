from board import Board
from game import Game

if __name__ == "__main__":
    board = Board()
    board.create_empty_board()
    print("Who will start?")
    print("1. computer")
    print("2. human")
    answer = int(input())
    human_starts = True
    if answer == 1:
        human_starts = False

    game = Game(board, human_starts)
    game.play()

