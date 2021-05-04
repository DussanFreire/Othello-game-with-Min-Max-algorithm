import datetime
from moves_manager import MovesManager
from board_marker import BoardMarker


class Game:
    def __init__(self, board, player_1, player_2, settings):
        self.board = board
        self.player1 = player_1
        self.player2 = player_2
        self.settings = settings
        self.p1_time_in_each_move = []
        self.p2_time_in_each_move = []
        self.moves_manager = MovesManager(settings, board)
        self.adversarial_search = None

    def append_time(self, player, stop, start):
        response_time = stop - start if stop - start >= 0 else 0
        if player == self.player1:
            self.p1_time_in_each_move.append(response_time)
        else:
            self.p2_time_in_each_move.append(response_time)
        return response_time

    def setup_players(self):
        self.player1.tokens_on_board.append((3, 3))
        self.player1.tokens_on_board.append((4, 4))
        self.player2.tokens_on_board.append((3, 4))
        self.player2.tokens_on_board.append((4, 3))

    def change_turn_player(self, player_on_turn):
        return (self.player1, self.player2) if player_on_turn != self.player1 else (self.player2, self.player1)

    def match(self):
        turn_number = 1
        player_on_turn = self.player2
        player_enemy = self.player1
        no_more_moves = False
        response_time = None
        computer_turn = False
        while True:
            start = datetime.datetime.now().second

            possible_moves = self.moves_manager.get_possible_moves(player_on_turn)
            self.display_possible_moves(possible_moves, turn_number, response_time, player_on_turn, player_enemy)

            if len(possible_moves) <= 0 and no_more_moves == False:
                # Stop Time
                response_time = self.append_time(player_on_turn, datetime.datetime.now().second, start)

                # Change player
                player_on_turn, player_enemy = self.change_turn_player(player_on_turn)

                no_more_moves = True
                turn_number += 1
                computer_turn = not computer_turn
                continue

            if len(possible_moves) <= 0 and no_more_moves:
                break
            # make move
            self.moves_manager.make_move(player_on_turn, possible_moves, player_enemy, computer_turn)

            # Stop Time
            response_time = self.append_time(player_on_turn, datetime.datetime.now().second, start)

            # Prepare board for the next turn

            # Change player
            player_on_turn, player_enemy = self.change_turn_player(player_on_turn)
            computer_turn = not computer_turn
            no_more_moves = False
            turn_number += 1

    def display_possible_moves(self, possible_moves, turn_number, response_time, player_on_turn, player_enemy):
        BoardMarker.mark_possible_moves(self.board, possible_moves, self.settings)
        self.board.display(turn_number, response_time, player_on_turn, player_enemy)
        BoardMarker.uncheck_possible_moves(self.board, possible_moves, self.settings)

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
        self.moves_manager.player1 = self.player1
        self.moves_manager.player2 = self.player2

        self.match()
        self.display_results()
