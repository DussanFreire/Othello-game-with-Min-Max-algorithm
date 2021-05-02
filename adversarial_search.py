import numpy as np
from moves_manager import MovesManager
# import copy


class AdversarialSearch:
    def __init__(self, settings):
        self.settings = settings

    def min_max_with_depth(self, states, focus):
        if len(states) > 1:
            if focus == self.settings.min:
                min(map(lambda state: self.max_value(- np.inf, np.inf, self.settings.depth, state), states))
            else:
                max(self.settings.heuristic())
        elif len(states) == 1:
            return states[0]
        else:
            return None

    def min_value(self, alpha, beta, depth):
        pass

    def max_value(self, alpha, beta, depth, state):
        moves_manager = MovesManager(self.settings, state)
        return 1

    def eval(self, state):
        pass

    def cut_off(self, state, depth):
        pass

    def alpha_beta_prunning(self):
        pass
