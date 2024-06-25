import unittest
import numpy as np
from board import Board  # Import lớp Board từ module board (đã định nghĩa ở file board.py)

# Định nghĩa kích thước của bảng Othello
BOARD_SIZE = 8

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_create_board_size(self):
        # Kiểm tra kích thước của bảng được tạo
        self.assertEqual(self.board.board.shape, (BOARD_SIZE, BOARD_SIZE))

    def test_initial_positions(self):
        # Kiểm tra các giá trị ban đầu của bảng Othello
        self.assertEqual(self.board.board[3][3], 1)   # Quân trắng ở vị trí (3, 3)
        self.assertEqual(self.board.board[3][4], -1)  # Quân đen ở vị trí (3, 4)
        self.assertEqual(self.board.board[4][3], -1)  # Quân đen ở vị trí (4, 3)
        self.assertEqual(self.board.board[4][4], 1)   # Quân trắng ở vị trí (4, 4)

    def test_other_positions(self):
        # Kiểm tra các vị trí khác trên bảng có giá trị 0 (không có quân cờ)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if (i, j) not in [(3, 3), (3, 4), (4, 3), (4, 4)]:
                    self.assertEqual(self.board.board[i][j], 0)

if __name__ == '__main__':
    unittest.main()
