from settings import Settings
from heuristiFunctionCollection import HeuristicFunctionCollection
from player import Player
from board import Board
from game import Game


if __name__ == "__main__":
    settings = Settings()
    token1 = settings.p1_token
    token2 = settings.p2_token

    settings.heuristic = HeuristicFunctionCollection().heuristic_1()
    board = Board(settings)
    board.create_empty_board()
    # os.system("cls")   NECESARIO.  Si los colors no funcionan hay que hacer un cls

    player1 = Player("Diego", settings.p1_token)
    player2 = Player("Dussan", settings.p2_token)
    game = Game(board, player1, player2, settings)
    game.play()

# HACER QUE LOS TURNOS DE CADA JUGADOR SE JUEGUEN CORRESPONDIENTEMENTE SEGUN EL QUE TENGA FICHAS NEGRAS.(actualmente
# empieza el jugador 1 sin importar nada) MEJORAR WHILE DE LA FUNCION "MATCH()", PARA QUE CONTROLE BIEN SI ACABO EL
# JUEGO O NO.

""" Colors:
        white = "\033[1;37m"
        green = "\033[0;32m"
        yellow = "\033[1;30m"
        brown = "\033[0;33m"
        """
