from cell import Cell


class Board:
    def __init__(self, settings):
        self.content = []
        self.settings = settings
        self.create_empty_board()

    def create_empty_board(self):
        for row in range(0, self.settings.dimension):
            empty_row = []
            for col in range(0, self.settings.dimension):
                empty_row.append(Cell())
            self.content.append(empty_row)


