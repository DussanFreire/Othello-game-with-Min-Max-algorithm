

class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, computer):
        return len(computer.tokens_on_board)
