import numpy as np


class AdversarialSearch:
    def __init__(self, settings):
        self.settings = settings

    def min_max_with_depth(self, states, focus):
        if len(states) > 1:
            if focus == self.settings.min:
                min(map(self.max_value(- np.inf, np.inf, self.settings.depth), states))
            else:
                max(self.settings.heuristic())
        elif len(states) == 1:
            return states[0]
        else:
            return None


    def min_value(self, alpha, beta, depth):
        pass

    def max_value(self, alpha, beta, depth):
        pass

    def eval(self, state):
        pass

    def cut_off(self, state, depth):
        pass

    def alpha_beta_prunning(self):
        pass
