import pygame, sys
from settings import *
from board import Board
from piece import Piece

class Game:
    def __init__(self):
        # initialise pygame essentials
        pygame.init()
        pygame.display.set_caption("Chess")
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.board = Board()
        self.white_pieces = [pygame.transform.scale(pygame.image.load("assets/white_pawn.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/white_rook.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/white_knight.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/white_bishop.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/white_queen.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/white_king.png"), (50, 50))]
        self.black_pieces = [pygame.transform.scale(pygame.image.load("assets/black_pawn.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/black_rook.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/black_knight.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/black_bishop.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/black_queen.png"), (50, 50)),
                             pygame.transform.scale(pygame.image.load("assets/black_king.png"), (50, 50))]

    def draw_game_window(self):
        self.window.fill((0, 0, 0))

    def run_game(self):
        pass

    def game_loop(self):
        while True:
            # fps = 60
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_loop()