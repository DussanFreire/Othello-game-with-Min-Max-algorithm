from adversarial_search import AdversarialSearch
from move_finder_helper import MoveFinderHelper


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
        return MoveFinderHelper.get_possible_moves(player, self.board, self.settings)

    def _apply_move(self, player, possible_move, player_enemy):
        current_pos = possible_move.initial_pos
        while True:
            col, row = MoveFinderHelper.get_next_position(possible_move.action, current_pos[1], current_pos[0])
            self.board.cells[row][col].token = player.token
            current_pos = (row, col)
            player.tokens_on_board.append(current_pos)
            if current_pos == possible_move.final_pos:
                player.tokens_on_board = MoveFinderHelper.get_unique_values(player.tokens_on_board)
                break
            player_enemy.tokens_on_board.remove(current_pos)

    def make_move(self, player, possible_moves, player_enemy, computer_turn):
        values = list(map(lambda m: m.final_pos, possible_moves))
        unique_opt = MoveFinderHelper.get_unique_values(values)
        while True:
            display_options(player, unique_opt)
            if computer_turn:
                # option_decided = numpy.random.randint(1, len(unique_opt) + 1)
                option_decided = AdversarialSearch.min_max_with_depth(player, self.board, self.settings)
            else:
                option_decided = int(input())

            print("choice:", option_decided)

            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        for option in filter(lambda op: op.final_pos == unique_opt[option_decided - 1], possible_moves):
            self._apply_move(player, option, player_enemy)
