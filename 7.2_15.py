def rootAlphaBeta(self, board, rules, ply, player):
    """ Makes a call to the alphaBeta function. Returns the optimal move for a player at given ply. """
    best_move = None
    max_eval = float('-infinity')

    move_list = board.generateMoves(rules, player)
    alpha = float('infinity')
    for move in move_list:
        board.makeMove(move, player)
        alpha = -self.alphaBeta(board, rules, float('-infinity'), alpha, ply - 1, board.getOtherPlayer(player))
        board.unmakeMove(move, player)

        if alpha > max_eval:
            max_eval = alpha
            best_move = move

    return best_move