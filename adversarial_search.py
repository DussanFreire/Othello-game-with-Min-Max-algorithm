from moves_helper import MoveHelper
from copy import deepcopy
from settings import Settings


class AdversarialSearch:
    computer = None
    beta = None
    alpha = None

    @staticmethod
    def min_max_with_depth(current_player, board, player_enemy, unique_values):
        AdversarialSearch.beta = Settings.highest_value
        AdversarialSearch.alpha = Settings.lowest_value
        index = 1
        AdversarialSearch.computer = deepcopy(current_player)
        p_moves = MoveHelper.get_possible_moves(AdversarialSearch.computer, deepcopy(board))

        if len(p_moves) > 1:
            heuristic_values = []
            for p_move in deepcopy(unique_values):
                new_board = deepcopy(board)
                new_move = deepcopy(p_move)
                new_enemy = deepcopy(player_enemy)

                adv_search = AdversarialSearch._max_value(0, new_board, new_move, deepcopy(AdversarialSearch.computer),
                                                          new_enemy, True)
                if adv_search == 100:
                    return index

                heuristic_values.append(adv_search)

                index += 1
            return heuristic_values.index(
                min(heuristic_values)) + 1 if 70 not in heuristic_values else heuristic_values.index(70) +1
        elif len(p_moves) == 1:
            return 1
        else:
            return None

    @staticmethod
    def _min_value(depth, board, possible_moves, current_player, player_enemy):
        # print("Board recibido------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        MoveHelper.apply_move(board, current_player, player_enemy, possible_moves)
        # print("Board final------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        if AdversarialSearch._cut_off(depth):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer, possible_moves)
        value = Settings.highest_value
        p_moves = MoveHelper.get_possible_moves(player_enemy, board)

        unique_opt, _ = MoveHelper.get_unique_final_pos(p_moves)
        for p_move in unique_opt:
            # print("profundidad",depth,"---------------------------------------------")
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(p_move)
            value = min(value, AdversarialSearch._max_value(depth + 1, new_board, new_possible_moves, copied_enemy,
                                                            copied_current_player))
            if value <= AdversarialSearch.alpha:
                return value
            AdversarialSearch.beta = min(AdversarialSearch.beta, value)
        return value

    @staticmethod
    def _max_value(depth, board, possible_moves, current_player, player_enemy, fist_ite=False):
        value = Settings.lowest_value

        if Settings.heuristic_aux is not None:
            result = Settings.heuristic_aux(board, possible_moves)
            if result is not None:
                value = max(value, result)
                if value >= AdversarialSearch.beta:
                    return value

        if Settings.heuristic_aux_2 is not None:
            result = Settings.heuristic_aux_2(board, possible_moves)
            if result is not None:
                return result

        # print("Board recibido------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        MoveHelper.apply_move(board, current_player, player_enemy, possible_moves)
        # print("Board final------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        if AdversarialSearch._cut_off(depth):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer, possible_moves)

        p_moves = MoveHelper.get_possible_moves(player_enemy, board)

        unique_opt, _ = deepcopy(MoveHelper.get_unique_final_pos(p_moves))

        for p_move in unique_opt:
            # print("profundidad",depth,"---------------------------------------------")
            new_enemy = deepcopy(player_enemy)
            new_c_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(p_move)
            value = max(value,
                        AdversarialSearch._min_value(depth + 1, new_board, new_possible_moves, new_enemy, new_c_player))
            if value >= AdversarialSearch.beta:
                return value
            AdversarialSearch.alpha = max(AdversarialSearch.alpha, value)
        return value

    @staticmethod
    def _eval(state, computer, possible_moves):
        return Settings.heuristic(state, computer, possible_moves)

    @staticmethod
    def _cut_off(depth):
        return depth == Settings.max_depth
