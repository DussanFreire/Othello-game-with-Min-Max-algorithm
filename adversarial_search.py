from move_finder_helper import MoveFinderHelper


class AdversarialSearch:
    @staticmethod
    def min_max_with_depth(current_player, board, settings):
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        if len(states) > 1:
                min(list(map(lambda s: AdversarialSearch._max_value(settings.lowest_value, settings.highest_value, settings.max_depth, s, current_player, settings),states)))
        elif len(states) == 1:
            return states[0]
        else:
            return None

    @staticmethod
    def _min_value(alpha, beta, depth, board, current_player, settings):
        if AdversarialSearch._cut_off(depth, settings):
            return - AdversarialSearch._eval(board, settings, current_player)
        value = settings.highest_value
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        value = min(
            map(lambda s: AdversarialSearch._max_value(alpha, beta, depth + 1, s, current_player, settings), states))
        if value >= alpha:
            return value
        beta = min(beta, value)
        return value

    @staticmethod
    def _max_value(alpha, beta, depth, board, current_player, settings):
        if AdversarialSearch._cut_off(depth, settings):
            return AdversarialSearch._eval(board, settings, current_player)
        value = settings.lowest_value
        states = MoveFinderHelper.get_possible_moves(current_player, board, settings)
        value = max(
            map(lambda s: AdversarialSearch._min_value(alpha, beta, depth + 1, s, current_player, settings), states))
        if value >= beta:
            return value
        alpha = min(alpha, value)
        return value

    @staticmethod
    def _eval(state, settings, current_player):
        return settings.heuristic(state, settings, current_player)

    @staticmethod
    def _cut_off(depth, settings):
        return depth == settings.max_depth

