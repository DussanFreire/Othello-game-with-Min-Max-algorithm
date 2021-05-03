import numpy as np
from heuristiFunctionCollection import HeuristicFunctionCollection


class Settings:
    def __init__(self):
        self.p1_token = 'O'
        self.p2_token = 'X'
        self.new_option_token = "*"
        self.empty_token = '_'
        self.min = "min"
        self.max = "max"
        self.lowest_value = - np.inf
        self.highest_value = np.inf
        self.max_depth = 3
        self.heuristic = HeuristicFunctionCollection().highest_score
        self.token_color = "\033[0;37m"  # white
        self.p1_color = "\033[0;32m"  # green
        self.p2_color = "\033[0;31m"  # red
        self.empty_token_color = "\033[0;37m"  # white
        self.new_option_color = "\033[0;35m"  # purple
        self.index_color = "\033[1;37m\033[1m"  # white with bold
        self.letters_color = "\033[0;33m"  # dark yellow / brown
        self.board_size = 8
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.actions = ["UP", "UP-RIGHT", "RIGHT", "DOWN-RIGHT", "DOWN", "LEFT-DOWN", "LEFT", "LEFT-UP"]
