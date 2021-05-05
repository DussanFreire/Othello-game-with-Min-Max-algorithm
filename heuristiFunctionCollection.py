import numpy

class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, computer, possible_moves):
        return len(computer.tokens_on_board)


    @staticmethod
    def strategic_place(state, computer, possible_moves):
        row, col = possible_moves[0].final_pos
        final_pos = state.cells[row][col]
        if final_pos.value == 1:
            return len(computer.tokens_on_board) + 60
        if final_pos.value == 0:
            return 1
        return 1000

    @staticmethod
    def movility_strategy(state, computer):
        value = 0
        if state.turns_number <= 22:
            value = len(computer.possible_moves)
        else:
            value = len(computer.tokens_on_board)
        return value
