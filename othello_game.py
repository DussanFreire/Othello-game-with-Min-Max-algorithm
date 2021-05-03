from settings import Settings
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

