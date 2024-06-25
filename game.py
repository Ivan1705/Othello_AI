import pygame
import sys
from board import Board
from constants import *

class Game:
    def __init__(self):
        pygame.init() # Khoi tao class pygame
        # screen size: 480 x 480
        self.screen = pygame.display.set_mode((BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE)) # Width, height
        pygame.display.set_caption('Othello')
        self.board = Board()
        self.human = -1
        self.ai = 1
        self.current_player = self.human

    def run(self):
        running = True
        while running:
            self.board.draw_board(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_player == self.human:
                        x, y = event.pos
                        print(f"x: {x}, y: {y}")
                        row, col = y // SQUARE_SIZE, x // SQUARE_SIZE # Tim xem nhap chuot vao o nao
                        if self.board.valid_move(row, col, self.current_player):
                            self.board.make_move(row, col, self.current_player)
                            self.current_player = self.ai

            if self.current_player == self.ai:
                # minimax algorithm
                pass
                self.current_player = self.human
                
        
        pygame.quit()
        sys.exit()