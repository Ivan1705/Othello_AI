import pygame
import sys
from board import create_board, draw_board, count_pieces
from game import get_valid_moves, make_move, valid_move
from ai import minimax

# Constants
SQUARE_SIZE = 60
WIDTH, HEIGHT = 8 * SQUARE_SIZE, 8 * SQUARE_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Othello')

    board = create_board()
    human_player = -1  # Human player is black (-1)
    ai_player = 1      # AI player is white (1)
    current_player = human_player

    running = True
    game_over = False

    while running:
        white_count, black_count = count_pieces(board)
        draw_board(screen, board, white_count, black_count)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if current_player == human_player:  # Human player
                    x, y = event.pos
                    row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                    if valid_move(board, row, col, current_player):
                        board = make_move(board, row, col, current_player)
                        current_player = ai_player

        if current_player == ai_player and not game_over:  # AI player
            _, move = minimax(board, 3, True, ai_player)
            if move:
                board = make_move(board, move[0], move[1], ai_player)
                current_player = human_player

        if not get_valid_moves(board, current_player):
            current_player = -current_player
            if not get_valid_moves(board, current_player):
                game_over = True

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
