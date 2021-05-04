from adversarial_search import AdversarialSearch
from move_finder_helper import MoveFinderHelper
from copy import deepcopy
import numpy


class MovesManager:
    def __init__(self, settings, board):
        self.player1 = None
        self.player2 = None
        self.settings = settings
        self.board = board

    def display_options(self, player, options):
        indice = 1
        print(player.name, "Choose one option:", player.token)
        for opt in options:
            print(f"{indice}: {self.settings.letters[opt[1]]} {opt[0] + 1}")
            indice += 1

    def _is_out_of_bounds(self, col, row):
        return col < 0 or row < 0 or col >= self.settings.board_size or row >= self.settings.board_size or col >= self.settings.board_size

    def get_possible_moves(self, player):
        return MoveFinderHelper.get_possible_moves(player, self.board, self.settings)

    def make_move(self, player, possible_moves, player_enemy, computer_turn):
        values = list(map(lambda m: m.final_pos, possible_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)
        while True:
            self.display_options(player, unique_opt)
            if computer_turn:
                option_decided = AdversarialSearch.min_max_with_depth(player, deepcopy(self.board), self.settings,
                                                                      player_enemy)
            else:
                # option_decided = int(input())
                option_decided = numpy.random.randint(1, len(unique_opt) + 1)
            print("choice:", option_decided)

            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        for option in filter(lambda op: op.final_pos == unique_opt[option_decided - 1], possible_moves):
            MoveFinderHelper.apply_move(self.board, player, option, player_enemy)
