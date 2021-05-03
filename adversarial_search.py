from move_finder_helper import MoveFinderHelper


class AdversarialSearch:
    def __init__(self, settings, moves_manager):
        self.settings = settings
        self.board = None
        self.current_player = None

    def min_max_with_depth(self, focus, current_player, board, settings):
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        if len(states) > 1:
            if focus == self.settings.min:
                min(map(lambda s: self.max_value(self.settings.lowest_value, self.settings.highest_value,
                                                 self.settings.max_depth, s, current_player, settings), states))
            else:
                max(self.settings.heuristic())
        elif len(states) == 1:
            return states[0]
        else:
            return None

    def min_value(self, alpha, beta, depth, board, current_player, settings):
        if self.cut_off(depth):
            return - self.eval(board, settings, current_player)
        value = self.settings.highest_value
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        value = min(map(lambda s: self.max_value(alpha, beta, depth + 1, s, current_player, settings), states))
        if value >= alpha:
            return value
        beta = min(beta, value)
        return value

    def max_value(self, alpha, beta, depth, board, current_player, settings):
        if self.cut_off(depth):
            return self.eval(board, settings, current_player)
        value = self.settings.lowest_value
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        value = max(map(lambda s: self.min_value(alpha, beta, depth + 1, s, current_player, settings), states))
        if value >= beta:
            return value
        alpha = min(alpha, value)
        return value

    def eval(self, state, settings, current_player):
        return self.settings.heuristic(state, settings, current_player)

    def cut_off(self, depth):
        return depth == self.settings.max_depth

    def alpha_beta_prunning(self):
        pass
