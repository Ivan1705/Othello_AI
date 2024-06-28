import numpy as np

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
BOARD_SIZE = 8

def valid_move(board, row, col, player):
    if board[row][col] != 0:
        return False
    for direction in DIRECTIONS:
        for i in range(1, BOARD_SIZE):
            x, y = row + direction[0] * i, col + direction[1] * i
            if x < 0 or y < 0 or x >= BOARD_SIZE or y >= BOARD_SIZE:
                break
            if board[x][y] == 0:
                break
            if board[x][y] == player:
                if i > 1:
                    return True
                else:
                    break
    return False

def get_valid_moves(board, player):
    valid_moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if valid_move(board, row, col, player):
                valid_moves.append((row, col))
    return valid_moves

def make_move(board, row, col, player):
    board[row][col] = player
    for direction in DIRECTIONS:
        pieces_to_flip = []
        for i in range(1, BOARD_SIZE):
            x, y = row + direction[0] * i, col + direction[1] * i
            if x < 0 or y < 0 or x >= BOARD_SIZE or y >= BOARD_SIZE:
                break
            if board[x][y] == 0:
                break
            if board[x][y] == player:
                for flip_row, flip_col in pieces_to_flip:
                    board[flip_row][flip_col] = player
                break
            pieces_to_flip.append((x, y))
    return board
