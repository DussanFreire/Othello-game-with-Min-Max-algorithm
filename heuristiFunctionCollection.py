def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


class HeuristicFunctionCollection:

    @staticmethod
    def highest_score(state, moves_manager, current_player):
        # prepare
        enemy_player = moves_manager.player1 if moves_manager.player1 != current_player else moves_manager.player2
        moves_manager.board = state
        possible_moves = moves_manager.get_possible_moves(current_player)
        value_list = []

        # work
        values = list(map(lambda m: m.final_pos, possible_moves))
        unique_opt = unique(values)

        for index in range(0, len(unique_opt)):
            winnable_cells = 0
            for option in filter(lambda op: op.final_pos == unique_opt[index], possible_moves):
                winnable_cells += option.winnable_cells
            value_list.append(winnable_cells)
        return value_list.index(max(value_list))
