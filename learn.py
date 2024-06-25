import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Định nghĩa màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Kích thước của mỗi ô vuông
SQUARE_SIZE = 60

# Số lượng ô vuông trên mỗi hàng và cột
NUM_SQUARES_X = 8
NUM_SQUARES_Y = 8

# Vòng lặp chính của trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ nền trắng
    screen.fill(WHITE)

    # Vẽ lưới ô vuông
    for y in range(NUM_SQUARES_Y):
        for x in range(NUM_SQUARES_X):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            pygame.draw.circle(screen, BLACK, rect.center, SQUARE_SIZE // 2)

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát Pygame
pygame.quit()
sys.exit()