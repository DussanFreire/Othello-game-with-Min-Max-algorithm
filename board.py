from cell import Cell
import numpy as np


class Board:
    def __init__(self, settings):
        self.settings = settings
        self.cells = None

    def display(self, turn_number, response_time, player_on_turn, player_enemy):
        i = 1
        print(self.settings.index_color, "\n")
        for n in self.settings.letters:
            print(n, end="     ")
        print("\n")

        for row in self.cells:
            for cell in row:
                color = self.settings.p1_color if cell.token == self.settings.p1_token else self.settings.p2_color if cell.token == self.settings.p2_token else self.settings.new_option_color if cell.token == self.settings.new_option_token else self.settings.empty_token_color
                print(color, end="")
                print(cell.token, end="     ")
                print(self.settings.index_color, end="")
            print("", i, "\n")
            i += 1
        print(self.settings.letters_color)
        print(f"Turn: {turn_number}\t Response Time of adversary: {response_time} [seconds]")
        print("Tokens on the board:")
        print(f"{player_on_turn.token}: {len(player_on_turn.tokens_on_board)}")
        print(f"{player_enemy.token}: {len(player_enemy.tokens_on_board)}")


    def create_empty_board(self):
        self.cells = np.array([[Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.p1_token),
                                Cell(self.settings.p2_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.p2_token),
                                Cell(self.settings.p1_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)],
                               [Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token),
                                Cell(self.settings.empty_token), Cell(self.settings.empty_token)]])
