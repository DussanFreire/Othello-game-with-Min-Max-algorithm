import numpy
import datetime


class Game:
    def __init__(self, board, player_1, player_2, settings):
        self.board = board
        self.player1 = player_1
        self.player2 = player_2
        self.settings = settings
        self.p1_time_in_each_move = []
        self.p2_time_in_each_move = []

    def append_time(self, player, time):
        if player == self.player1:
            self.p1_time_in_each_move.append(time)
        else:
            self.p2_time_in_each_move.append(time)

    def setup_players(self):
        self.player1.tokens_on_board.append((3, 3))
        self.player1.tokens_on_board.append((4, 4))
        self.player2.tokens_on_board.append((3, 4))
        self.player2.tokens_on_board.append((4, 3))

    def get_next_position(self, action, col, row):
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

    def is_out_of_bounds(self, col, row):
        return col < 0 or row < 0 or col >= self.settings.board_size or row >= self.settings.board_size or col >= self.settings.board_size

    def get_possible_moves(self, player):
        possible_moves = []
        enemy_token = self.player2.token if player.token == self.player1.token else self.player1.token
        for token_pos in player.tokens_on_board:
            for action in self.settings.actions:
                enemy_found = False
                first_iteration = True
                col, row = self.get_next_position(action, token_pos[1], token_pos[0])
                while True:

                    if self.is_out_of_bounds(col, row):
                        break

                    if first_iteration:
                        if self.board.cells[row][col].token != enemy_token:
                            break
                        first_iteration = False

                    if self.board.cells[row][col].token == self.settings.empty_token and enemy_found:
                        possible_moves.append([(row, col), (token_pos[0], token_pos[1]), action])
                        break

                    if self.board.cells[row][col].token == self.settings.empty_token:
                        break

                    if self.board.cells[row][col].token == player.token:
                        break

                    if self.board.cells[row][col].token == enemy_token:
                        enemy_found = True
                        col, row = self.get_next_position(action, col, row)
                        continue

                    col, row = self.get_next_position(action, col, row)
                    enemy_found = False
        return possible_moves

    def unique(self, list1):
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    def display_options(self, player, options):
        indice = 1

        print(player.name, "Select a cell to place your token", player.token)
        for opt in options:
            print(f"{indice}: row: {opt[0] + 1} col: {opt[1] + 1}")
            indice += 1

    def apply_move(self, player, possible_move, player_enemy):
        current_pos = possible_move[1]
        action = possible_move[2]
        while True:
            col, row = self.get_next_position(action, current_pos[1], current_pos[0])
            self.board.cells[row][col].token = player.token
            current_pos = (row, col)
            player.tokens_on_board.append(current_pos)
            if current_pos == possible_move[0]:
                player.tokens_on_board = self.unique(player.tokens_on_board)
                break
            player_enemy.tokens_on_board.remove(current_pos)

    def make_move(self, player, possible_moves, player_enemy):
        values = list(map(lambda p: p[0], possible_moves))
        unique_opt = self.unique(values)
        while True:
            self.display_options(player, unique_opt)
            # option_decided = int(input())

            option_decided = numpy.random.randint(1, len(unique_opt) + 1)

            print("random choice:", option_decided)

            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        for option in filter(lambda op: op[0] == unique_opt[option_decided - 1], possible_moves):
            self.apply_move(player, option, player_enemy)

    def match(self):
        turn_number = 1
        player_on_turn = self.player2
        player_enemy = self.player1
        no_more_moves = False
        response_time = None
        while True:
            start = datetime.datetime.now().microsecond

            possible_moves = self.get_possible_moves(player_on_turn)
            self.mark_possible_moves(possible_moves)
            self.board.draw_board(turn_number, response_time)

            if len(possible_moves) <= 0 and no_more_moves == False:
                # Stop Time
                now = datetime.datetime.now().microsecond
                response_time = now - start if now - start >= 0 else 0
                self.append_time(player_on_turn, response_time)

                # Change player
                player_enemy = player_on_turn
                player_on_turn = self.player1 if player_on_turn != self.player1 else self.player2

                no_more_moves = True
                turn_number += 1
                continue

            if len(possible_moves) <= 0 and no_more_moves:
                break

            self.make_move(player_on_turn, possible_moves, player_enemy)

            # Stop Time
            now = datetime.datetime.now().microsecond
            response_time = now - start if now - start >= 0 else 0
            self.append_time(player_on_turn, response_time)

            # Prepare board for the next turn
            self.uncheck_possible_moves(possible_moves)

            # Change player
            player_enemy = player_on_turn
            player_on_turn = self.player1 if player_on_turn != self.player1 else self.player2

            no_more_moves = False
            turn_number += 1

    def mark_possible_moves(self, possible_moves):
        for move in possible_moves:
            self.board.cells[move[0][0]][move[0][1]].token = self.settings.new_option_token

    def uncheck_possible_moves(self, possible_moves):
        for move in possible_moves:
            if self.board.cells[move[0][0]][move[0][1]].token == self.settings.new_option_token:
                self.board.cells[move[0][0]][move[0][1]].token = self.settings.empty_token

    def display_results(self):
        p1_score = len(self.player1.tokens_on_board)
        p2_score = len(self.player2.tokens_on_board)
        print("Scores:")
        print(
            f"Player: {self.player1.name}\t Score: {p1_score}\t Time response average: {sum(self.p1_time_in_each_move) / len(self.p1_time_in_each_move)} [microseconds]")
        # print(f"Player 1: Time in each turn: {self.p1_time_in_each_move}")

        print(
            f"Player: {self.player2.name}\t Score: {p2_score}\t Time response average: {sum(self.p2_time_in_each_move) / len(self.p2_time_in_each_move)} [microseconds]")
        # print(f"Player 2: Time in each turn: {self.p2_time_in_each_move}")

        print(
            f"-> WINNER: {self.player1.name if p1_score > p2_score else self.player2.name if p2_score > p1_score else 'TIE'} ")

    def play(self):
        self.setup_players()  # Distribute tokens
        self.match()
        self.display_results()
