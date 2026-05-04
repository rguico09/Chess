import pygame, sys
from settings import *
from board import Board

class Game:
    def __init__(self):
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

    def draw_game_window(self):
        self.window.fill((26, 26, 26))
        self.board.draw_board(self.window)
        self.board.draw_pieces(self.window)

    def run_game(self):
        pass

    def move_pieces(self):
        coordinates = pygame.mouse.get_pos()
        col = coordinates[0] // SQUARE_SIZE
        row = coordinates[1] // SQUARE_SIZE
        if 0 <= row < 8 and 0 <= col < 8:
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
                    # Check if it's the correct turn
                    if (piece.colour == 'w' and self.white_to_move) or (piece.colour == 'b' and not self.white_to_move):
                        valid_moves = piece.get_valid_moves(self.board.board)
                        if (end_row, end_col) in valid_moves:
                            # Move the piece
                            piece.row = end_row
                            piece.col = end_col
                            self.board.board[end_row][end_col] = piece
                            self.board.board[start_row][start_col] = None
                            # Toggle turn
                            self.white_to_move = not self.white_to_move
                        else:
                            # Invalid move, reset selection but keep first click if player clicked another of their own pieces?
                            # For simplicity, just reset
                            pass
                print(self.white_to_move)
                
                self.square_selected = ()
                self.player_clicks = []

    def game_loop(self):
        while True:
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
                    self.move_pieces()

            self.run_game()
            self.draw_game_window()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
