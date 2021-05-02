class Game:
    def __init__(self, board, player_1, player_2, settings):
        self.board = board
        self.player1 = player_1
        self.player2 = player_2
        self.settings = settings
        self.game_moves = []  # List that contains all the moves made by each player
        self.recommended_moves = []  # [((actual_pos), (flank_ally_position), (flanked_enemies_counter))]

    def setup_players(self):
        # print("Who will start?", "\n1) Player1 \n2) Player2 \nchoose one: ")
        # selection = int(input())

        # token1 = self.settings.p1_token if selection == 1 else self.settings.p2_token
        # token2 = self.settings.p2_token if selection == 1 else self.settings.p1_token
        self.player1.tokens_on_board.append((3, 3))
        self.player1.tokens_on_board.append((4, 4))
        self.player2.tokens_on_board.append((3, 4))
        self.player2.tokens_on_board.append((4, 3))
        for i in range(32):
            self.player1.tokens.append(self.settings.p1_token)
            self.player2.tokens.append(self.settings.p2_token)

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
        return col < 0 or row < 0 or col >= self.settings.board_size or row >= col >= self.settings.board_size

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

        print(player.name, "Select a cell to place your token",player.token)
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
            option_decided = int(input())
            if option_decided in range(1, len(unique_opt) + 1):
                break
            print("Choose one of the options please!")
        for option in filter(lambda op: op[0] == unique_opt[option_decided - 1], possible_moves):
            self.apply_move(player, option, player_enemy)

    def match(self):
        player_on_turn = self.player2
        player_enemy = self.player1
        while len(player_on_turn.tokens) > 0:
            possible_moves = self.get_possible_moves(player_on_turn)
            self.mark_possible_moves(possible_moves)
            self.board.draw_board()
            if len(possible_moves) <= 0:
                break
            self.make_move(player_on_turn, possible_moves, player_enemy)
            # self.board.draw_board()
            self.uncheck_possible_moves(possible_moves)
            # self.board.draw_board()
            player_enemy = player_on_turn
            player_on_turn = self.player1 if player_on_turn != self.player1 else self.player2

    def mark_possible_moves(self, possible_moves):
        for move in possible_moves:
            self.board.cells[move[0][0]][move[0][1]].token = self.settings.new_option_token

    def uncheck_possible_moves(self, possible_moves):
        for move in possible_moves:
            if self.board.cells[move[0][0]][move[0][1]].token == self.settings.new_option_token:
                self.board.cells[move[0][0]][move[0][1]].token = self.settings.empty_token

    def display_results(self):
        print("Scores:")
        print(f"Player 1: {self.player1.name}/t Score: {len(self.player1.tokens_on_board)}")
        print(f"Player 2: {self.player2.name}/t Score: {len(self.player2.tokens_on_board)}")

    def play(self):
        self.setup_players()  # Distribute tokens
        self.match()
        self.display_results()
