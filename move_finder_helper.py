from move import Move
from copy import deepcopy


class MoveFinderHelper:

    @staticmethod
    def get_unique_values(list_with_duplicated_values):
        unique_list = []
        for x in list_with_duplicated_values:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    @staticmethod
    def get_unique_final_pos(unique_pos, list_with_duplicated_values):
        unique_list = []
        for x in unique_pos:
            for pos in list_with_duplicated_values:
                if x == pos.final_pos:
                    unique_list.append(pos)
                    break
        return unique_list

    @staticmethod
    def get_next_position(action, col, row):
        next_column = None
        next_row = None
        if action == "UP":
            next_row = row - 1
            next_column = col
        if action == "UP-RIGHT":
            next_row = row - 1
            next_column = col + 1
        if action == "RIGHT":
            next_row = row
            next_column = col + 1
        if action == "DOWN-RIGHT":
            next_row = row + 1
            next_column = col + 1
        if action == "DOWN":
            next_row = row + 1
            next_column = col
        if action == "LEFT-DOWN":
            next_row = row + 1
            next_column = col - 1
        if action == "LEFT":
            next_row = row
            next_column = col - 1
        if action == "LEFT-UP":
            next_row = row - 1
            next_column = col - 1
        return next_column, next_row

    @staticmethod
    def _is_out_of_bounds(col, row, settings):
        return col < 0 or row < 0 or col >= settings.board_size or row >= settings.board_size or col >= settings.board_size

    @staticmethod
    def get_possible_moves(player, board, settings):
        possible_moves = []
        enemy_token = settings.p2_token if player.token == settings.p1_token else settings.p1_token
        for token_pos in player.tokens_on_board:
            for action in settings.actions:
                enemy_found = False
                first_iteration = True
                winnable_cells = 0
                col, row = MoveFinderHelper.get_next_position(action, token_pos[1], token_pos[0])
                while True:

                    if MoveFinderHelper._is_out_of_bounds(col, row, settings):
                        break

                    if first_iteration:
                        if board.cells[row][col].token != enemy_token:
                            break
                        first_iteration = False

                    if board.cells[row][col].token == settings.empty_token and enemy_found:
                        possible_moves.append(Move((row, col), (token_pos[0], token_pos[1]), action, winnable_cells))
                        break

                    if board.cells[row][col].token == settings.empty_token:
                        break

                    if board.cells[row][col].token == player.token:
                        break

                    if board.cells[row][col].token == enemy_token:
                        enemy_found = True
                        winnable_cells += 1
                        col, row = MoveFinderHelper.get_next_position(action, col, row)
                        continue

                    col, row = MoveFinderHelper.get_next_position(action, col, row)
                    enemy_found = False
        return possible_moves

    @staticmethod
    def apply_move(board, player, possible_move, player_enemy):
        current_pos = possible_move.initial_pos
        while True:
            col, row = MoveFinderHelper.get_next_position(possible_move.action, current_pos[1], current_pos[0])
            board.cells[row][col].token = player.token
            current_pos = (row, col)
            player.tokens_on_board.append(current_pos)
            if current_pos == possible_move.final_pos:
                player.tokens_on_board = MoveFinderHelper.get_unique_values(player.tokens_on_board)
                break
            player_enemy.tokens_on_board.remove(current_pos)
        return deepcopy(board)
