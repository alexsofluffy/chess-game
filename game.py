from board import Board
from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Chess:
    """Represents a game of chess."""

    def __init__(self):
        self.game_board = Board()
        self.board = self.game_board.board
        self.turn = 'w'
        self.state = 'UNFINISHED'

    def is_in_check(self, player):
        """Checks whether or not the specified player is in check."""
        if player == 'w':
            for row in range(8):
                for col in range(8):
                    test_piece = self.board[row][col]
                    if test_piece != '_':
                        if isinstance(test_piece, King) is True and \
                                test_piece.color == 'w':
                            king_pos = [test_piece.row, test_piece.col]
            for row2 in range(8):
                for col2 in range(8):
                    test_piece2 = self.board[row2][col2]
                    if test_piece2 != '_':
                        if test_piece2.color == 'b':
                            if test_piece2.is_move_valid(king_pos[0],
                                                         king_pos[1],
                                                         self.board) is True:
                                return True
        if player == 'b':
            for row in range(8):
                for col in range(8):
                    test_piece = self.board[row][col]
                    if test_piece != '_':
                        if isinstance(test_piece, King) is True and \
                                test_piece.color == 'b':
                            king_pos = [test_piece.row, test_piece.col]
            for row2 in range(8):
                for col2 in range(8):
                    test_piece2 = self.board[row2][col2]
                    if test_piece2 != '_':
                        if test_piece2.color == 'w':
                            if test_piece2.is_move_valid(king_pos[0],
                                                         king_pos[1],
                                                         self.board) is True:
                                return True
            return False

    def move(self, row, col, new_row, new_col):
        """Moves specified piece to the specified location on board if valid.

        Keyword arguments:
        row -- the row on the game board that piece is located
        col -- the column on the game board that piece is located
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        """
        # Returns False if game is already finished.
        if self.state != 'UNFINISHED':
            return False

        # Returns False if the arguments passed are out of range.
        if row not in range(8) or col not in range(8) or \
                new_row not in range(8) or new_col not in range(8):
            return False

        # Returns False if starting position contains no piece to move.
        if self.board[row][col] == '_':
            return False

        # Returns False if starting and ending positions are the same.
        if new_row == row and new_col == col:
            return False

        # Returns False if player tries to move opponent's piece or capture one
        # of its own pieces.
        if self.turn == 'w':
            if self.board[row][col].color == 'b':
                return False
            if self.board[new_row][new_col] != '_':
                if self.board[new_row][new_col].color == 'w':
                    return False
        if self.turn == 'b':
            if self.board[row][col].color == 'w':
                return False
            if self.board[new_row][new_col] != '_':
                if self.board[new_row][new_col].color == 'b':
                    return False

        # Returns False if move is invalid per that piece type's rules.
        piece = self.board[row][col]
        taken_piece = self.board[new_row][new_col]
        if piece.is_move_valid(new_row, new_col, self.board) is False:
            return False

        # Updates the position of the piece.
        self.board[new_row][new_col] = piece
        self.board[row][col] = '_'
        piece.row = new_row
        piece.col = new_col

        # Reverses move and returns False if move puts own king in check.
        if self.turn == 'w':
            if self.is_in_check('w') is True:
                self.board[new_row][new_col] = taken_piece
                self.board[row][col] = piece
                piece.row = row
                piece.col = col
                return False
        if self.turn == 'b':
            if self.is_in_check('b') is True:
                self.board[new_row][new_col] = taken_piece
                self.board[row][col] = piece
                piece.row = row
                piece.col = col
                return False

        # Updates the turn tracker.
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'
        return True


a = Chess()
a.game_board.print_board()
print(a.move(6, 3, 4, 3))
a.game_board.print_board()
print(a.move(1, 3, 3, 3))
a.game_board.print_board()
print(a.move(7, 2, 3, 6))
a.game_board.print_board()
print(a.move(0, 3, 2, 3))
a.game_board.print_board()
print(a.move(6, 4, 5, 4))
a.game_board.print_board()
print(a.move(0, 4, 0, 3))
a.game_board.print_board()
print(a.move(6, 6, 4, 6))
a.game_board.print_board()
print(a.move(1, 4, 2, 4))
a.game_board.print_board()