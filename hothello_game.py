import numpy as np
import os

class Settings:
    face_up = 'O' #blancas
    face_down = 'X' #negras
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
        self.directions = ["UP", "UP-RIGHT", "RIGHT", "DOWN-RIGHT", "DOWN", "LEFT-DOWN", "LEFT", "LEFT-UP"]
        self.game_moves = [] # List that contains all the moves made by each player
        self.recomended_moves = [] # [((actual_pos), (flank_ally_position), (flanked_enemies_counter))]
    
    def setup_players(self):
        print("Who will start?", "\n1) Player1 \n2) Player2 \nchoose one: ")
        selection = int(input())

        token1 = Token(settings.face_up) if selection == 1 else Token(settings.face_down)
        token2 = Token(settings.face_down) if selection == 1 else Token(settings.face_up)
        for i in range(32):
            player1.tokens.append(token2)
            player2.tokens.append(token1)
        #input(player1.tokens[0].value)
        #input(player2.tokens[0].value)
    
    def next_position(self, direction, col, row):
        if direction == "UP":
            next_row = row - 1
            next_column = col
        if direction == "UP-RIGHT":
            next_row = row - 1
            next_column = col + 1
        if direction == "RIGHT":
            next_row = row
            next_column = col + 1
        if direction == "DOWN-RIGHT":
            next_row = row + 1
            next_column = col + 1
        if direction == "DOWN":
            next_row = row + 1
            next_column = col
        if direction == "LEFT-DOWN":
            next_row = row + 1
            next_column = col - 1
        if direction == "LEFT":
            next_row = row
            next_column = col - 1
        if direction == "LEFT-UP":
            next_row = row - 1
            next_column = col - 1
        return next_column, next_row

    def out_of_bounds(self, col, row):
        return col < 0 or row < 0  or col >= 8 or row >= 8

    def explore(self, direction, col, row, player):
        next_column, next_row = self.next_position(direction, col, row)
        ally_token_value = player.tokens[0].value
        enemy_token_value  = settings.face_up if  ally_token_value == settings.face_down else settings.face_down # Sera siempre opuesto al ally_token
        flank_count = 0
        
        if not self.out_of_bounds(next_column, next_row):  # VERIFICAR QUE NO SALGA DEL MAPA
            next_token = board.cells[next_row][next_column].token.value
            if next_token == enemy_token_value:
                while not self.out_of_bounds(next_column, next_row) and (next_token == enemy_token_value or next_token == ally_token_value): 
                    if board.cells[next_row][next_column].token.value == ally_token_value:
                        #data = ((col+1, row+1), (next_column+1, next_row+1), flank_count) #+1 to match the user interface positions
                        flank_pos = [next_column+1, next_row+1]# +1 to match the user interface positions
                        #self.recomended_moves.append(data)
                        return flank_pos, flank_count
                    else:
                        flank_count += 1
                        next_column, next_row = self.next_position(direction, next_column, next_row)
        return (-1, -1), -1


    def search_flanks(self, col, row, player):
        actual_col = col
        actual_row = row
        flanks = [] # Lista de tuplas de todos los flanks validos posibles de una celda "cell" con su numero de fichas a flankear (flank_count)
        for direction in self.directions:
            flank_pos, flank_count = self.explore(direction, col, row, player)
            if flank_count != -1:
                flanks.append([flank_pos, flank_count])
        if len(flanks) > 0:
            flanking_data = [(col+1, row+1), flanks]  # +1 to match the user interface positions
            self.recomended_moves.append(flanking_data)

    def recomend_moves(self, player):
        row_i = 0
        col_i = 0
        for row in board.cells:
            for cell in row:
                if cell.token.value == "_":
                    self.search_flanks(col_i, row_i, player)
                col_i += 1
                #if has adyacent enemy token
                #if adyacent token has adyacent ally to flank with  ()
            row_i += 1
            col_i = 0
        #print()

    def is_recomended_move(self, column, row):
        for r_move in self.recomended_moves:
            if column == r_move[0][0] and row == r_move[0][1]:
                flanks = r_move[1] # (flank_col, flank_row)
                return True, flanks
        return False, (0,0)#(column, row) in self.recomended_moves[0]

    def valid_move(self, column, row):
        valid = False
        validated, flanks = self.is_recomended_move(column, row)
        valid = True if  validated else False
        print("Enter valid move please!")
        return valid, flanks

    def do_flanks(self, col, row, flanks, player):
        f_col = 0
        f_row = 0
        for flank in flanks:
            f_col = int(flank[0][0]) # flank = [[flank_position], flank_count] => flank[0] = [flank_col, flank_row]
            f_row = int(flank[0][1])
            f_col -= 1
            f_row -= 1
            #print(f_col, f_row, col, row)  
            #input()
            while (f_col != col or f_row != row)  and not self.out_of_bounds(f_col, f_row):
                self.board.cells[f_row][f_col].token = player.tokens[0]
                
                f_row = f_row + 1 if row > f_row else f_row - 1 if row < f_row else f_row
                f_col = f_col + 1 if col > f_col else f_col - 1 if col < f_col else f_col

    def make_move(self, player):
        accepted = False
        flank = (0,0) # col, row
        while(accepted == False):
            print(player.name, "Select a cell to place your token")
            print("column: ", end="")
            column = int(input()) - 1
            print("row: ", end="")
            row = int(input()) - 1
            accepted, flanks = self.valid_move(column+1, row+1) # +1 to match the UI positions
        
        board.cells[row][column].token = player.tokens[0]
        player.tokens.pop()

        self.do_flanks(column, row, flanks, player)

        self.game_moves.append((player.tokens[0].value, column+1, row+1)) # +1 to match the UI positions
        print(len(player.tokens))


    def match(self):
        board.draw_board()
        while len(player1.tokens) > 0 and len(player2.tokens) > 0  or  len(recomend_moves) > 0:
            self.recomend_moves(player1)
            print(self.recomended_moves)
            self.make_move(player1)
            board.draw_board()
            game_moves = []
            self.recomended_moves = []
            
            self.recomend_moves(player2)
            print(self.recomended_moves)
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

"""    agregar (posicion aliado, posicion del "_" en cuestion, contador)
    luego verificar si en el siguiente movimiento en misma direccion hay otro aliado
    si al final nos topamos con un aliado, 
    REVISAR MIS APUNTES DE IDEAS.  ME DIO SUENIO Y NO SE SI ESTOS PASOS ESCRITOS ESTAN BIEN"""

"""
    def explore(self, direction, col, row, player):
        next_column, next_row = self.next_position(direction, col, row)
        ally_token_value = player.tokens[0].value
        enemy_token_value  = settings.face_up if  ally_token_value == settings.face_down else settings.face_down # Sera siempre opuesto al ally_token
        flank_count = 0
        
        if next_column > 0 and next_row > 0   and next_column < 8 and next_row < 8:  # VERIFICAR QUE NO SALGA DEL MAPA
            print(board.cells[next_row][next_column].token.value)
            if board.cells[next_row][next_column].token.value == enemy_token_value:
                while board.cells[next_row][next_column].token.value == enemy_token_value or board.cells[next_row][next_column].token.value == ally_token_value: 
                    if board.cells[next_row][next_column].token.value == ally_token_value:
                        data = ((col, row), (next_column, next_row), flank_count)
                        self.recomended_moves.append(data)
                        return True
                    else:
                        flank_count += 1
                        next_column, next_row = next_position(direction, col, row)
        return False
        """

"""

        print("player 1 makes move and his tokens are reduced by 1")
        print("player 2 makes move and his tokens are reduced by 1")
        print("moves are registered in each player move list and in the general game_move list")
        
        print("if a move is invalid the player has to try another move")
        print("flanked tokens change their side (character face_up or face_down)")
        print("game registers and draws the board and all the moves made")
        print("game move recomendations will be added at the end")
        """

""" Recursivo no funciona porque es dificil o mas bien sucio, mantener el col y row  que teniamos al inicio de la busqueda
    
    def explore(self, direction, col, row, player):
        next_column, next_row = self.next_position(direction, col, row)
        ally_token_value = player.tokens[0].value
        enemy_token_value  = settings.face_up if  ally_token_value == settings.face_down else settings.face_down # Sera siempre opuesto al ally_token
        flank_count = 0
        #print(next_row,next_column)
        if next_column >= 0 and next_row >= 0   and next_column < 8 and next_row < 8:  # VERIFICAR QUE NO SALGA DEL MAPA
            #print(board.cells[next_row][next_column].token.value)
            if board.cells[next_row][next_column].token.value == enemy_token_value:
                flank_count += 1
                #next_column, next_row = self.next_position(direction, col, row)
                self.explore(direction, next_column, next_row, player)
            elif board.cells[next_row][next_column].token.value == ally_token_value:
                data = ((col, row), (next_column, next_row), flank_count)
                self.recomended_moves.append(data)
                return True
                    
        return False
"""