from board import Board
from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Chess:
    """Represents a game of chess."""

    def __init__(self):
        self.game_board = Board()
        self.board = self.game_board.board
        self.turn = 'white'

    def move(self, row, col, new_row, new_col):
        piece = self.board[row][col]

        if piece.is_move_valid(new_row, new_col, self.board) is True:
            self.board[new_row][new_col] = piece
            self.board[row][col] = '_'
            piece.row = new_row
            piece.col = new_col
            return True
        else:
            return piece.is_move_valid(new_row, new_col, self.board)



a = Chess()
a.game_board.print_board()
print(a.move(7, 3, 6, 2))
a.game_board.print_board()
print(a.move(6, 2, 5, 3))
a.game_board.print_board()
print(a.move(5, 3, 3, 5))
a.game_board.print_board()
print(a.move(7, 4, 6, 4))
a.game_board.print_board()
print(a.move(6, 4, 5, 4))
a.game_board.print_board()
print(a.move(5, 4, 6, 6))
a.game_board.print_board()
print('hi!')