from settings import Settings
from player import Player
from board import Board
from game import Game

if __name__ == "__main__":
    board = Board()
    board.create_empty_board()

    player1 = Player("Computer", Settings.p1_token)
    player2 = Player("Dussan", Settings.p2_token)
    game = Game(board, player1, player2)
    game.play()

