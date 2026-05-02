import pygame, sys
from settings import *
from board import Board

class Game:
    def __init__(self):
        # initialise pygame essentials
        pygame.init()
        pygame.display.set_caption("Chess")
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.board = Board()
        # track whose turn it is
        self.white_to_move = True
        # stack to store moves for undoing
        self.move_log = []

    def draw_game_window(self):
        self.window.fill((26, 26, 26))
        self.board.draw_board(self.window)
        self.board.draw_pieces(self.window)

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

            self.draw_game_window()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_loop()