import pygame

FPS = 60
WINDOW_WIDTH = 810
WINDOW_HEIGHT = 800
SQUARE_SIZE = 75

GREEN = (0, 153, 51)
WHITE = (255, 255, 255)

IMAGES = {}

pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
for piece in pieces:
    if piece.startswith('w'):
        img = pygame.image.load(f"assets/sprites/white/{piece}.png")
    else:
        img = pygame.image.load(f"assets/sprites/black/{piece}.png")
    # Scale them to fit the square (e.g., 80% of square size)
    IMAGES[piece] = pygame.transform.scale(img, (int(SQUARE_SIZE * 0.8), int(SQUARE_SIZE * 0.8)))