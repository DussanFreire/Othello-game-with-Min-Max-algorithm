

class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, settings, computer):
        return len(computer.tokens_on_board)
