class BoardMarker:
    @staticmethod
    def mark_possible_moves(board, possible_moves, settings):
        for move in possible_moves:
            board.cells[move.final_pos[0]][move.final_pos[1]].token = settings.new_option_token

    @staticmethod
    def uncheck_possible_moves(board, possible_moves, settings):
        for move in possible_moves:
            if board.cells[move.final_pos[0]][move.final_pos[1]].token == settings.new_option_token:
                board.cells[move.final_pos[0]][move.final_pos[1]].token = settings.empty_token
