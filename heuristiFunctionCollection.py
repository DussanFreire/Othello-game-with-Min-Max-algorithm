from move_finder_helper import MoveFinderHelper


class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, settings, current_player):
        # prepare
        possible_moves = MoveFinderHelper.get_possible_moves(current_player, state, settings)
        value_list = []

        # work
        values = list(map(lambda m: m.final_pos, possible_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)

        for index in range(0, len(unique_opt)):
            winnable_cells = 0
            for option in filter(lambda op: op.final_pos == unique_opt[index], possible_moves):
                winnable_cells += option.winnable_cells
            value_list.append(winnable_cells)
        return value_list.index(max(value_list))
