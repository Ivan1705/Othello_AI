BOARD_SIZE = 8
SQUARE_SIZE = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
"""
(0, 1): Di chuyển sang phải (tăng cột)
(1, 0): Di chuyển xuống dưới (tăng hàng)
(0, -1): Di chuyển sang trái (giảm cột)
(-1, 0): Di chuyển lên trên (giảm hàng)
(1, 1): Di chuyển theo đường chéo xuống dưới bên phải (tăng hàng và cột)
(-1, -1): Di chuyển theo đường chéo lên trên bên trái (giảm hàng và cột)
(1, -1): Di chuyển theo đường chéo xuống dưới bên trái (tăng hàng và giảm cột)
(-1, 1): Di chuyển theo đường chéo lên trên bên phải (giảm hàng và tăng cột)
"""
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1,), (-1, -1), (1, -1), (-1, 1)]