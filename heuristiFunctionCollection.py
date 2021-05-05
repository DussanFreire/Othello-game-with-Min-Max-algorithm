
class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, computer, possible_moves):
        return len(computer.tokens_on_board)

    @staticmethod
    def strategic_place_aux(state, possible_moves):
        row, col = possible_moves[0].final_pos
        final_pos = state.cells[row][col]
        if final_pos.value == 100:
            return 100
        if final_pos.value == 70:
            return 70
        return None

    @staticmethod
    def strategic_place_aux_2(state, possible_moves):
        row, col = possible_moves[0].final_pos
        final_pos = state.cells[row][col]
        if final_pos.value == 0:
            return 1
        return None

    @staticmethod
    def strategic_place(state, computer, possible_moves):
        row, col = possible_moves[0].final_pos
        final_pos = state.cells[row][col]
        if final_pos.value == 0:
            return 1
        return len(computer.tokens_on_board)
