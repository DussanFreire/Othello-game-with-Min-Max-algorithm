

class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, computer):
        return len(computer.tokens_on_board)

    ""

    @staticmethod
    def movility_strategy(state, computer):
        value = 0
        if state.turns_number <= 22:
            value = len(computer.possible_moves)
        else:
            value = len(computer.tokens_on_board)
        return value
