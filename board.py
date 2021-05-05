from cell import Cell
import numpy as np
from settings import Settings


class Board:
    def __init__(self):
        self.cells = None

    def display(self, turn_number, response_time, player_on_turn, player_enemy):
        i = 1
        print(Settings.index_color, "\n")
        for n in Settings.letters:
            print(n, end="     ")
        print("\n")

        for row in self.cells:
            for cell in row:
                color = Settings.p1_color if cell.token == Settings.p1_token else Settings.p2_color if cell.token == Settings.p2_token else Settings.new_option_color if cell.token == Settings.new_option_token else Settings.empty_token_color
                print(color, end="")
                print(cell.token, end="     ")
                print(Settings.index_color, end="")
            print("", i, "\n")
            i += 1
        print(Settings.letters_color)
        print(f"Turn: {turn_number}\t Response Time of adversary: {response_time} [seconds]")
        print("Tokens on the board:")
        print(f"{player_on_turn.token}: {len(player_on_turn.tokens_on_board)}")
        print(f"{player_enemy.token}: {len(player_enemy.tokens_on_board)}")

    def create_empty_board(self):
        self.cells = np.array([[Cell(Settings.empty_token, 100), Cell(Settings.empty_token,  0), Cell(Settings.empty_token, 70), Cell(Settings.empty_token), Cell(Settings.empty_token), Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 0) , Cell(Settings.empty_token, 100)],
                               [Cell(Settings.empty_token, 0)  , Cell(Settings.empty_token,  0), Cell(Settings.empty_token, 70), Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 0) , Cell(Settings.empty_token, 0)],
                               [Cell(Settings.empty_token, 70) , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 70), Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 70)],
                               [Cell(Settings.empty_token) , Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.p1_token)       , Cell(Settings.p2_token)       , Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token)],
                               [Cell(Settings.empty_token) , Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.p2_token)       , Cell(Settings.p1_token)       , Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token)],
                               [Cell(Settings.empty_token, 70) , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 70), Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 70)],
                               [Cell(Settings.empty_token,  0) , Cell(Settings.empty_token, 0 ), Cell(Settings.empty_token, 70), Cell(Settings.empty_token)    , Cell(Settings.empty_token)    , Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 0) , Cell(Settings.empty_token, 0)],
                               [Cell(Settings.empty_token, 100), Cell(Settings.empty_token, 0 ), Cell(Settings.empty_token, 70), Cell(Settings.empty_token), Cell(Settings.empty_token), Cell(Settings.empty_token, 70), Cell(Settings.empty_token, 0) , Cell(Settings.empty_token, 100)]])

    def place_token(self, row, col, token):
        pos = self.cells[row][col]
        pos.token = token
        if pos.value == 100:
            if col == row == 0:
                self.cells[1][1].value = 1
                self.cells[1][0].value = 1
                self.cells[0][1].value = 1
            if col == row == 7:
                self.cells[6][7].value = 1
                self.cells[6][6].value = 1
                self.cells[7][6].value = 1
            if col == 0 and row == 7:
                self.cells[6][0].value = 1
                self.cells[6][1].value = 1
                self.cells[7][1].value = 1
            if col == 7 and row == 0:
                self.cells[0][6].value = 1
                self.cells[1][6].value = 1
                self.cells[1][7].value = 1

            