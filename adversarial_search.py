

class AdversarialSearch:
    def __init__(self, settings, moves_manager):
        self.settings = settings
        self.current_player = None
        self.moves_manager = moves_manager

    def min_max_with_depth(self, state, focus, current_player):
        states = self.moves_manager.get_possible_moves(current_player)
        if len(states) > 1:
            if focus == self.settings.min:
                min(map(lambda s: self.max_value(self.settings.lowest_value, self.settings.highest_value, self.settings.max_depth, s), states))
            else:
                max(self.settings.heuristic())
        elif len(states) == 1:
            return states[0]
        else:
            return None

    def min_value(self, alpha, beta, depth, state, current_player):
        if self.cut_off(depth):
            return - self.eval(state, current_player)
        value = self.settings.highest_value
        states = self.moves_manager.get_possible_moves(current_player)
        value = min(map(lambda s: self.max_value(alpha, beta, depth+1, s, current_player), states))
        if value >= alpha:
            return value
        beta = min(beta, value)
        return value

    def max_value(self, alpha, beta, depth, state, current_player):
        if self.cut_off(depth):
            return self.eval(state, current_player)
        value = self.settings.lowest_value
        states = self.moves_manager.get_possible_moves(current_player)
        value = max(map(lambda s: self.min_value(alpha, beta, depth+1, s, current_player), states))
        if value >= beta:
            return value
        alpha = min(alpha, value)
        return value

    def eval(self, state, current_player):
        return self.settings.heuristic(state, self.moves_manager, current_player)

    def cut_off(self, depth):
        return depth == self.settings.max_depth

    def alpha_beta_prunning(self):
        pass
