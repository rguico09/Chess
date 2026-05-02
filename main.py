import pygame, sys, csv
from settings import *

class Game:
    def __init__(self):
        # initialise pygame essentials
        pygame.init()
        pygame.display.set_caption("Chess")
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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