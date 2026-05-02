from settings import IMAGES, SQUARE_SIZE

class Piece:
    def __init__(self, colour, name, row, col):
        self.colour = colour
        self.name = name
        self.row = row
        self.col = col
        self.id = colour + name

    def draw(self, window):
        padding = SQUARE_SIZE * 0.1
        x = self.col * SQUARE_SIZE + padding
        y = self.row * SQUARE_SIZE + padding
        window.blit(IMAGES[self.id], (x, y))