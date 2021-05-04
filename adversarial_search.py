from move_finder_helper import MoveFinderHelper
from copy import deepcopy
import numpy as np


class AdversarialSearch:
    computer = None
    beta = - np.inf
    alpha = - np.inf

    @staticmethod
    def min_max_with_depth(current_player, board, settings, player_enemy):
        AdversarialSearch.beta = - np.inf
        AdversarialSearch.alpha = - np.inf
        AdversarialSearch.computer = deepcopy(current_player)
        p_moves = MoveFinderHelper.get_possible_moves(AdversarialSearch.computer, deepcopy(board), settings)
        values = list(map(lambda m: m.final_pos, p_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)
        unique_opt = MoveFinderHelper.get_unique_final_pos(unique_opt, p_moves)
        if len(p_moves) > 1:
            heuristic_values = []
            for p_move in unique_opt:
                heuristic_values.append(AdversarialSearch._max_value(0, deepcopy(board), p_move, AdversarialSearch.computer, settings, deepcopy(player_enemy)))
            return heuristic_values.index(min(heuristic_values)) + 1
        elif len(p_moves) == 1:
            return 1
        else:
            return None

    @staticmethod
    def _min_value(depth, board, possible_move, current_player, settings, player_enemy):
        new_board = MoveFinderHelper.apply_move(board, current_player, possible_move, player_enemy)
        if AdversarialSearch._cut_off(depth, settings):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(new_board, settings, computer)
        value = settings.highest_value
        p_moves = MoveFinderHelper.get_possible_moves(player_enemy, new_board, settings)
        values = list(map(lambda m: m.final_pos, p_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)
        unique_opt = MoveFinderHelper.get_unique_final_pos(unique_opt, p_moves)
        for p_move in unique_opt:
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            value = min(value, AdversarialSearch._max_value(depth + 1, deepcopy(new_board), p_move, copied_enemy, settings, copied_current_player))
            if value <= AdversarialSearch.alpha:
                return value
            AdversarialSearch.beta = min(AdversarialSearch.beta, value)
        return value

    @staticmethod
    def _max_value(depth, board, possible_move, current_player, settings, player_enemy):
        new_board = MoveFinderHelper.apply_move(board, current_player, possible_move, player_enemy)
        if AdversarialSearch._cut_off(depth, settings):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(new_board, settings, computer)
        value = settings.lowest_value
        p_moves = MoveFinderHelper.get_possible_moves(player_enemy, new_board, settings)
        values = list(map(lambda m: m.final_pos, p_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)
        unique_opt = MoveFinderHelper.get_unique_final_pos(unique_opt, p_moves)
        for p_move in unique_opt:
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            value = max(value, AdversarialSearch._min_value(depth + 1, deepcopy(new_board), p_move, copied_enemy, settings, copied_current_player))
            if value >= AdversarialSearch.beta:
                return value
            AdversarialSearch.alpha = max(AdversarialSearch.alpha, value)
        return value

    @staticmethod
    def _eval(state, settings, computer):
        return settings.heuristic(state, settings, computer)

    @staticmethod
    def _cut_off(depth, settings):
        return depth == settings.max_depth
