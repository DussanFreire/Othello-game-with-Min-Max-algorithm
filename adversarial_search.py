from move_finder_helper import MoveFinderHelper
from copy import deepcopy
from settings import Settings

class AdversarialSearch:
    computer = None
    beta = None
    alpha = None

    @staticmethod
    def min_max_with_depth(current_player, board,  player_enemy):
        AdversarialSearch.beta = Settings.highest_value
        AdversarialSearch.alpha = Settings.lowest_value

        AdversarialSearch.computer = deepcopy(current_player)
        p_moves = MoveFinderHelper.get_possible_moves(AdversarialSearch.computer, deepcopy(board))

        unique_opt = MoveFinderHelper.get_unique_final_pos(p_moves)
        if len(p_moves) > 1:
            heuristic_values = []
            for p_move in unique_opt:
                heuristic_values.append(AdversarialSearch._max_value(0, deepcopy(board), p_move, AdversarialSearch.computer, deepcopy(player_enemy)))
            return heuristic_values.index(min(heuristic_values)) + 1
        elif len(p_moves) == 1:
            return 1
        else:
            return None

    @staticmethod
    def _min_value(depth, board, possible_move, current_player, player_enemy):
        MoveFinderHelper.apply_move(board, current_player, possible_move, player_enemy)
        if AdversarialSearch._cut_off(depth):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer)
        value = Settings.highest_value
        p_moves = MoveFinderHelper.get_possible_moves(player_enemy, board)

        unique_opt = MoveFinderHelper.get_unique_final_pos(p_moves)
        for p_move in unique_opt:
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            new_board = deepcopy(board)
            value = min(value, AdversarialSearch._max_value(depth + 1, new_board, p_move, copied_enemy, copied_current_player))
            if value <= AdversarialSearch.alpha:
                return value
            AdversarialSearch.beta = min(AdversarialSearch.beta, value)
        return value

    @staticmethod
    def _max_value(depth, board, possible_move, current_player, player_enemy):
        MoveFinderHelper.apply_move(board, current_player, possible_move, player_enemy)
        if AdversarialSearch._cut_off(depth):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer)

        value = Settings.lowest_value
        p_moves = MoveFinderHelper.get_possible_moves(player_enemy, board)

        unique_opt = MoveFinderHelper.get_unique_final_pos(p_moves)

        for p_move in unique_opt:
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            new_board = deepcopy(board)
            value = max(value, AdversarialSearch._min_value(depth + 1, new_board, p_move, copied_enemy, copied_current_player))
            if value >= AdversarialSearch.beta:
                return value
            AdversarialSearch.alpha = max(AdversarialSearch.alpha, value)
        return value

    @staticmethod
    def _eval(state, computer):
        return Settings.heuristic(state, computer)

    @staticmethod
    def _cut_off(depth):
        return depth == Settings.max_depth
