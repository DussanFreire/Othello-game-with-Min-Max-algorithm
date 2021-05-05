class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.tokens_on_board = []
        self.possible_moves =[]
        self.score = None
