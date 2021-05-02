

class Settings:
    def __init__(self):
        self.p1_token = 'O'
        self.p2_token = 'X'
        self.new_option_token = "*"
        self.empty_token = '_'
        self.min = "min"
        self.max = "max"
        self.depth = 10
        self.heuristic = None
        self.token_color = "\033[0;37m" # white
        self.p1_color = "\033[0;32m" # green
        self.p2_color = "\033[0;31m" # red
        self.empty_token_color = "\033[0;37m" # white
        self.letters_color = "\033[0;33m" # dark yellow
        self.board_size = 8
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.actions = ["UP", "UP-RIGHT", "RIGHT", "DOWN-RIGHT", "DOWN", "LEFT-DOWN", "LEFT", "LEFT-UP"]

