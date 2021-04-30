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
    def __init__(self, name):
        self.name = name
        self.tokens = []
        self.moves = [] # each item: (column, row)
        #self.settings = settings

class Token:
    def __init__(self, value):
        self.value = value


class Cell(object):
    def __init__(self, token=Token("_")):
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
                print(cell.token.value, end="     ")
            print("",numbers[i] ,"\n")
            i = i + 1
        print(white, "\n")

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.game_moves = [] # List that contains all the moves made by each player
        self.recomended_moves = []
    
    def setup_players(self):
        print("Who will start?", "\n1) Player1 \n2) Player2 \nchoose one: ")
        selection = int(input())

        token1 = Token(settings.face_up) if selection == 1 else Token(settings.face_down)
        token2 = Token(settings.face_down) if selection == 1 else Token(settings.face_up)
        for i in range(32):
            player1.tokens.append(token1)
            player2.tokens.append(token2)
    
    def recomend_moves(self, player):
        for row in board.cells:
            for cell in row:
                print()
                #if has adyacent enemy token
                #if adyacent token has adyacent ally to flank with  ()
        print()

    def is_recomended_move(self, column, row):
        return (column, row) in self.recomended_moves

    def valid_move(self, column, row):
        valid = False
        valid = True if self.is_recomended_move(column, row) else False
        print("Enter valid move please!")
        return valid

    def make_move(self, player):
        print(player.name, "Select a cell to place your token")
        print("column: ", end="")
        column = int(input()) - 1
        print("row: ", end="")
        row = int(input()) - 1
        #accepted = self.valid_move(column, row)
        
        board.cells[row][column].token = player.tokens[0]
        player.tokens.pop()
        self.game_moves.append((player.tokens[0].value, column, row))
        print(len(player.tokens))


    def match(self):
        print("player 1 makes move and his tokens are reduced by 1")
        print("player 2 makes move and his tokens are reduced by 1")
        print("moves are registered in each player move list and in the general game_move list")
        
        print("if a move is invalid the player has to try another move")
        print("flanked tokens change their side (character face_up or face_down)")
        print("game registers and draws the board and all the moves made")
        print("game move recomendations will be added at the end")
        board.draw_board()
        while len(player1.tokens) > 0 and len(player2.tokens) > 0  or  len(recomend_moves) > 0:
            #self.recomend_moves(player1)
            self.make_move(player1)
            board.draw_board()
            game_moves = []
            
            #self.recomend_moves(player2)
            self.make_move(player2)
            board.draw_board()
            game_moves = []
            
            print(self.game_moves)

        
        

    def play(self):
        self.setup_players() # Distribute tokens
        #board.draw_board()
        self.match()

if __name__ == "__main__":
    settings = Settings()
    token1 = Token(settings.face_up)
    token2 = Token(settings.face_down)
    cells = np.array([[Cell(),  Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(token1),     Cell(token2),     Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(token2),     Cell(token1),     Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()],
                    [Cell(),    Cell(),     Cell(),     Cell(),           Cell(),           Cell(),     Cell(),     Cell()]])

    settings.heuristic = HeuristicFunction().heuristic1
    board = Board(cells)
    # os.system("cls")   NECESARIO.  Si los coclores no funcionan hay que hacer un cls

    player1 = Player("Diego")
    player2 = Player("Dussan")
    game = Game(board, player1, player2)
    game.play()

""" Colors:
        white = "\033[1;37m"
        green = "\033[0;32m"
        yellow = "\033[1;30m"
        brown = "\033[0;33m"
        """