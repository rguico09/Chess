import pygame, sys
from settings import *
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Chess")
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        # instantiate Board object
        self.board = Board()
        # track whose turn it is
        self.white_to_move = True
        # stack to store moves for undoing
        self.move_log = []
        # square selected
        self.square_selected = ()
        # where to move selected piece
        self.player_clicks = []
        # valid moves for selected piece
        self.valid_moves = []
        # captured pieces
        self.captured_white = []
        self.captured_black = []

    # for drawing necessary objects onto the window
    def draw_game_window(self):
        self.window.fill((26, 26, 26))
        pygame.draw.rect(self.window, (0, 0, 0), (600, 0, 210, 600))
        self.board.draw_board(self.window)
        self.board.draw_pieces(self.window)
        self.highlight_squares()
        
        # rendering some messages
        reset_message = self.font.render("Press 'R' to restart game.", True, (255, 255, 255))
        self.window.blit(reset_message, (25, 675))

        if self.white_to_move:
            turn = self.font.render("White to move", True, (255, 255, 255))
            self.window.blit(turn, (25, 625))
        else:
            turn = self.font.render("Black to move", True, (255, 255, 255))
            self.window.blit(turn, (25, 625))

    # highlights valid moves for selected piece
    def highlight_squares(self):
        if self.square_selected != ():
            r, c = self.square_selected
            piece = self.board.board[r][c]
            if piece and ((piece.colour == 'w' and self.white_to_move) or (piece.colour == 'b' and not self.white_to_move)):
                # highlight selected square
                s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                s.set_alpha(SELECT_COLOR[3]) # transparency from alpha value
                s.fill(SELECT_COLOR[:3]) # RGB values
                self.window.blit(s, (c * SQUARE_SIZE, r * SQUARE_SIZE))
                
                # highlight valid moves
                s.fill(HIGHLIGHT[:3]) # red for valid moves
                s.set_alpha(HIGHLIGHT[3])
                for move in self.valid_moves:
                    self.window.blit(s, (move[1] * SQUARE_SIZE, move[0] * SQUARE_SIZE))

    # handles piece movement
    def move_pieces(self):
        coordinates = pygame.mouse.get_pos()
        col = coordinates[0] // SQUARE_SIZE
        row = coordinates[1] // SQUARE_SIZE
        if 0 <= row < 8 and 0 <= col < 8:
            if self.square_selected == (row, col): # player seleted same square twice
                self.square_selected = ()
                self.player_clicks = []
                self.valid_moves = []
            else:
                self.square_selected = (row, col)
                self.player_clicks.append(self.square_selected)
    
            if len(self.player_clicks) == 1:
                r, c = self.player_clicks[0]
                piece = self.board.board[r][c]
                if piece and ((piece.colour == 'w' and self.white_to_move) or (piece.colour == 'b' and not self.white_to_move)):
                    self.valid_moves = piece.get_valid_moves(self.board.board)
                else:
                    self.valid_moves = []

            if len(self.player_clicks) == 2:
                start_row, start_col = self.player_clicks[0]
                end_row, end_col = self.player_clicks[1]

                piece = self.board.board[start_row][start_col]
                
                if piece:
                    # check if it's the correct turn
                    if (piece.colour == 'w' and self.white_to_move) or (piece.colour == 'b' and not self.white_to_move):
                        if (end_row, end_col) in self.valid_moves:
                            # handle capture
                            captured_piece = self.board.board[end_row][end_col]
                            if captured_piece:
                                if captured_piece.colour == 'w':
                                    self.captured_white.append(captured_piece)
                                else:
                                    self.captured_black.append(captured_piece)
                            
                            # move the piece
                            piece.row = end_row
                            piece.col = end_col
                            self.board.board[end_row][end_col] = piece
                            self.board.board[start_row][start_col] = None
                            # toggle turn
                            self.white_to_move = not self.white_to_move
                        else:
                            # invalid move
                            pass
                
                self.square_selected = ()
                self.player_clicks = []
                self.valid_moves = []

    # handles game rules
    # check, checkmate, en passant, castling, pawn promotion, etc.
    def run_game(self):
        pass

    # reset game
    def reset_game(self):
        self.board = Board()
        self.white_to_move = True
        self.move_log = []
        self.square_selected = ()
        self.player_clicks = []
        self.valid_moves = []
        self.captured_white = []
        self.captured_black = []

    # main game loop
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
                    if event.key == pygame.K_r:
                        self.reset_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move_pieces()

            self.run_game()
            self.draw_game_window()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
