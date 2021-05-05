import numpy as np
from heuristiFunctionCollection import HeuristicFunctionCollection


class Settings:
    p1_token = 'o'
    p2_token = 'x'
    new_option_token = "."
    empty_token = '_'
    min = "min"
    max = "max"
    lowest_value = - np.inf
    highest_value = np.inf
    max_depth = 5
    heuristic = HeuristicFunctionCollection().movility_strategy
    token_color = "\033[0;37m"  # white
    p1_color = "\033[0;32m"  # green
    p2_color = "\033[0;31m"  # red
    empty_token_color = "\033[0;37m"  # white
    new_option_color = "\033[0;35m"  # purple
    index_color = "\033[1;37m\033[1m"  # white with bold
    letters_color = "\033[0;33m"  # dark yellow / brown
    board_size = 8
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    actions = ["UP", "UP-RIGHT", "RIGHT", "DOWN-RIGHT", "DOWN", "LEFT-DOWN", "LEFT", "LEFT-UP"]
