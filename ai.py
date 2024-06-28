import numpy as np
from game import get_valid_moves, make_move

def minimax(board, depth, maximizing, player):
    opponent = -player
    valid_moves = get_valid_moves(board, player)
    if depth == 0 or not valid_moves:
        return np.sum(board) * player, None

    best_move = None
    if maximizing:
        max_eval = float('-inf')
        for move in valid_moves:
            new_board = board.copy()
            new_board = make_move(new_board, move[0], move[1], player)
            evaluation, _ = minimax(new_board, depth - 1, False, opponent)
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in valid_moves:
            new_board = board.copy()
            new_board = make_move(new_board, move[0], move[1], player)
            evaluation, _ = minimax(new_board, depth - 1, True, opponent)
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
        return min_eval, best_move
