import pygame
from settings import *
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board_layout = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.generate_board()

    def generate_board(self):
        piece_map = {
            'p': Pawn,
            'R': Rook,
            'N': Knight,
            'B': Bishop,
            'Q': Queen,
            'K': King
        }
        for row in range(8):
            for col in range(8):
                symbol = self.board_layout[row][col]
                if symbol != "--":
                    colour = symbol[0]
                    name = symbol[1]
                    piece_class = piece_map.get(name, Piece)
                    self.board[row][col] = piece_class(colour, name, row, col)

    def draw_board(self, window):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GREEN
                pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, window):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(window)
