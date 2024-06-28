import numpy as np
import pygame

BOARD_SIZE = 8
SQUARE_SIZE = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

WIDTH, HEIGHT = 8 * SQUARE_SIZE, 8 * SQUARE_SIZE

def create_board():
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    board[3][3], board[3][4] = 1, -1
    board[4][3], board[4][4] = -1, 1
    return board

def draw_board(screen, board, white_count, black_count):
    screen.fill(GREEN)
    font = pygame.font.Font(None, 36)
    
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[y][x] == 1:
                pygame.draw.circle(screen, WHITE, rect.center, SQUARE_SIZE // 2 - 2)
            elif board[y][x] == -1:
                pygame.draw.circle(screen, BLACK, rect.center, SQUARE_SIZE // 2 - 2)

    white_text = font.render(f'White: {white_count}', True, WHITE)
    black_text = font.render(f'Black: {black_count}', True, BLACK)
    screen.blit(white_text, (10, HEIGHT - 40))
    screen.blit(black_text, (WIDTH - 150, HEIGHT - 40))
    
    pygame.display.flip()

def count_pieces(board):
    white_count = np.sum(board == 1)
    black_count = np.sum(board == -1)
    return white_count, black_count
