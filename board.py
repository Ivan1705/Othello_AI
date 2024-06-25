import numpy as np
import pygame 
from constants import *


class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = np.zeros((BOARD_SIZE, BOARD_SIZE)) # 8 x 8
        board[3][3], board[3][4] = 1, -1 # white is 1, black is -1
        board[4][3], board[4][4] = -1, 1
        return board
    
    def draw_board(self, screen):
        screen.fill(GREEN)
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)
                # Draw chess
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, WHITE, rect.center, SQUARE_SIZE // 2 - 5)
                elif self.board[y][x] == -1:
                    pygame.draw.circle(screen, BLACK, rect.center, SQUARE_SIZE // 2 - 5)
        # Update screen
        pygame.display.flip() 

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def valid_move(self, row, col, player):
        # Neu khong phai o trong
        if self.board[row][col] != 0:
            return False
        for direction in DIRECTIONS:
            for i in range(1, BOARD_SIZE):
                # x, y la cac huong xung quanh vi tri neu dat quan co
                x, y = row + direction[0] * i, col + direction[1] * i
                # Neu direction do ra ngoai ban co
                if x < 0 or y < 0 or x >= BOARD_SIZE or y >= BOARD_SIZE:
                    break
                # Neu direction do la o trong
                if self.board[x][y] == 0:
                    break
                if self.board[x][y] == player:
                    if i > 1:
                        return True
                    else:
                        break
        return False
       
