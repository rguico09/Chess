from settings import IMAGES, SQUARE_SIZE

class Piece:
    def __init__(self, colour, name, row, col):
        self.colour = colour
        self.name = name
        self.row = row
        self.col = col
        self.id = colour + name

    # to render the piece
    def draw(self, window):
        padding = SQUARE_SIZE * 0.1
        x = self.col * SQUARE_SIZE + padding
        y = self.row * SQUARE_SIZE + padding
        window.blit(IMAGES[self.id], (x, y))
    
    # determine valid moves
    def get_valid_moves(self, board):
        return []
    
    # determine if next possible move is within board dimensions
    def is_on_board(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8)


class Pawn(Piece):
    def get_valid_moves(self, board):
        moves = []
        direction = -1 if self.colour == "w" else 1

        # move one square
        if self.is_on_board(self.row + direction, self.col):
            if board[self.row + direction][self.col] is None:
                moves.append((self.row + direction, self.col))
                # initial couble move
                if (self.colour == "w" and self.row == 6) or (self.colour == "b" and self.row == 1):
                    if self.is_on_board(self.row + 2 * direction, self.col) and board[self.row + 2 * direction][self.col] is None:
                        moves.append((self.row + 2 * direction, self.col))

        for dc in [-1, 1]:
            nr, nc = self.row + direction, self.col + dc
            if self.is_on_board(nr, nc):
                target = board[nr][nc]
                if target is not None and target.colour != self.colour:
                    moves.append((nr, nc))
        
        return moves

class Rook(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                nr, nc = self.row + dr * i, self.col + dc * i
                if not self.is_on_board(nr, nc):
                    break
                target = board[nr][nc]
                if target is None:
                    moves.append((nr, nc))
                elif target.colour != self.colour:
                    moves.append((nr, nc))
                    break
                else:
                    break
        return moves

class Knight(Piece):
    def get_valid_moves(self, board):
        moves = []
        steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        for dr, dc in steps:
            nr, nc = self.row + dr, self.col + dc
            if self.is_on_board(nr, nc):
                target = board[nr][nc]
                if target is None or target.colour != self.colour:
                    moves.append((nr, nc))

        return moves

class Bishop(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            for i in range(1, 8):
                nr, nc = self.row + dr * i, self.col + dc * i
                if not self.is_on_board(nr, nc):
                    break
                target = board[nr][nc]
                if target is None:
                    moves.append((nr, nc))
                elif target.colour != self.colour:
                    moves.append((nr, nc))
                    break
                else:
                    break
        
        return moves

class Queen(Piece):
    def get_valid_moves(self, board):
        rook_moves = Rook.get_valid_moves(self, board)
        bishop_moves = Bishop.get_valid_moves(self, board)
        return rook_moves + bishop_moves

class King(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            nr, nc = self.row + dr, self.col + dc
            if self.is_on_board(nr, nc):
                target = board[nr][nc]
                if target is None or target.colour != self.colour:
                    moves.append((nr, nc))
        return moves
