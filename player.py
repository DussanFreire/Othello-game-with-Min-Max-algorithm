class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.tokens = []
        self.tokens_on_board = []
    # self.moves = [] # each item: (column, row)
        self.score = None
