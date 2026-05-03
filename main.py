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
        # square selected
        self.square_selected = ()
        # where to move selected piece
        self.player_clicks = []
        # piece selected by user

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coordinates = pygame.mouse.get_pos()
                    col = coordinates[0] // SQUARE_SIZE
                    row = coordinates[1] // SQUARE_SIZE
                    if self.square_selected == (row, col): # player seleted same square twice
                        self.square_selected = ()
                        self.player_clicks = []
                    else:
                        self.square_selected = (row, col)
                        self.player_clicks.append(self.square_selected)
                    
                    if len(self.player_clicks) == 2:
                        start_row, start_col = self.player_clicks[0]
                        end_row, end_col = self.player_clicks[1]

                        piece = self.board.board[start_row][start_col]

                        if piece:
                            piece.row = end_row
                            piece.col = end_col

                            self.board.board[end_row][end_col] = piece
                            self.board.board[start_row][start_col] = None
            
                        self.square_selected = ()
                        self.player_clicks = []

            self.run_game()
            self.draw_game_window()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_loop()