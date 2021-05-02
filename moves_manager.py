import numpy


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


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def display_options(player, options):
    indice = 1

    print(player.name, "Select a cell to place your token", player.token)
    for opt in options:
        print(f"{indice}: row: {opt[0] + 1} col: {opt[1] + 1}")
        indice += 1


class MovesManager:
    def __init__(self, settings, board):
        self.player1 = None
        self.player2 = None
        self.settings = settings
        self.board = board

    def _is_out_of_bounds(self, col, row):
        return col < 0 or row < 0 or col >= self.settings.board_size or row >= self.settings.board_size or col >= self.settings.board_size

    def get_possible_moves(self, player):
        possible_moves = []
        enemy_token = self.player2.token if player.token == self.player1.token else self.player1.token
        for token_pos in player.tokens_on_board:
            for action in self.settings.actions:
                enemy_found = False
                first_iteration = True
                won_cells = 0
                col, row = get_next_position(action, token_pos[1], token_pos[0])
                while True:

                    if self._is_out_of_bounds(col, row):
                        break

                    if first_iteration:
                        if self.board.cells[row][col].token != enemy_token:
                            break
                        first_iteration = False

                    if self.board.cells[row][col].token == self.settings.empty_token and enemy_found:
                        possible_moves.append([(row, col), (token_pos[0], token_pos[1]), action, won_cells])
                        break

                    if self.board.cells[row][col].token == self.settings.empty_token:
                        break

                    if self.board.cells[row][col].token == player.token:
                        break

                    if self.board.cells[row][col].token == enemy_token:
                        enemy_found = True
                        won_cells += 1
                        col, row = get_next_position(action, col, row)
                        continue

                    col, row = get_next_position(action, col, row)
                    enemy_found = False
        return possible_moves

    def _apply_move(self, player, possible_move, player_enemy):
        current_pos = possible_move[1]
        action = possible_move[2]
        while True:
            col, row = get_next_position(action, current_pos[1], current_pos[0])
            self.board.cells[row][col].token = player.token
            current_pos = (row, col)
            player.tokens_on_board.append(current_pos)
            if current_pos == possible_move[0]:
                player.tokens_on_board = unique(player.tokens_on_board)
                break
            player_enemy.tokens_on_board.remove(current_pos)

    def make_move(self, player, possible_moves, player_enemy):
        values = list(map(lambda p: p[0], possible_moves))
        unique_opt = unique(values)
        while True:
            display_options(player, unique_opt)
            # option_decided = int(input())

            option_decided = numpy.random.randint(1, len(unique_opt) + 1)

            print("random choice:", option_decided)

            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        for option in filter(lambda op: op[0] == unique_opt[option_decided - 1], possible_moves):
            self._apply_move(player, option, player_enemy)