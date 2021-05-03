class Move:
    def __init__(self, final_pos, initial_pos, action, number_of_positions_won):
        self.final_pos = final_pos
        self.initial_pos = initial_pos
        self.action = action
        self.winnable_cells = number_of_positions_won

