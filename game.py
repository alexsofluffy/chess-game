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
        king_pos = []
        if player == 'w':
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if isinstance(piece, King) is True and piece.color == 'w':
                        king_pos.append(row)
                        king_pos.append(col)
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if piece != '_' and piece.color == 'b':
                        if piece.is_move_valid(king_pos[0], king_pos[1],
                                               self.board) is True:
                            return True
        if player == 'b':
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if isinstance(piece, King) is True and piece.color == 'b':
                        king_pos.append(row)
                        king_pos.append(col)
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if piece != '_' and piece.color == 'w':
                        if piece.is_move_valid(king_pos[0], king_pos[1],
                                               self.board) is True:
                            return True
        return False

    def is_in_mate(self, player):
        """Checks whether the specified player is in checkmate or stalemate."""
        if player == 'w':
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if piece != '_' and piece.color == 'w':
                        for row2 in range(8):
                            for col2 in range(8):
                                taken_piece = self.board[row2][col2]
                                if piece.is_move_valid(row2, col2,
                                                       self.board) is True:
                                    self.board[row2][col2] = piece
                                    self.board[row][col] = '_'
                                    piece.row = row2
                                    piece.col = col2
                                    if self.is_in_check('w') is False:
                                        self.board[row2][col2] = taken_piece
                                        self.board[row][col] = piece
                                        piece.row = row
                                        piece.col = col
                                        return False
                                    else:
                                        self.board[row2][col2] = taken_piece
                                        self.board[row][col] = piece
                                        piece.row = row
                                        piece.col = col
        if player == 'b':
            for row in range(8):
                for col in range(8):
                    piece = self.board[row][col]
                    if piece != '_' and piece.color == 'b':
                        for row2 in range(8):
                            for col2 in range(8):
                                taken_piece = self.board[row2][col2]
                                if piece.is_move_valid(row2, col2,
                                                       self.board) is True:
                                    self.board[row2][col2] = piece
                                    self.board[row][col] = '_'
                                    piece.row = row2
                                    piece.col = col2
                                    if self.is_in_check('b') is False:
                                        self.board[row2][col2] = taken_piece
                                        self.board[row][col] = piece
                                        piece.row = row
                                        piece.col = col
                                        return False
                                    else:
                                        self.board[row2][col2] = taken_piece
                                        self.board[row][col] = piece
                                        piece.row = row
                                        piece.col = col
        return True

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
        # Updates the is_in_check status of the opponent if move places their
        # king in check.
        if self.turn == 'w':
            if self.is_in_check('w') is True:
                self.board[new_row][new_col] = taken_piece
                self.board[row][col] = piece
                piece.row = row
                piece.col = col
                return False
            if isinstance(piece, Pawn) is True:
                if new_row == 0 or new_row == 7:
                    while True:
                        new_piece = input(
                            'What piece would you like to promote to? ')
                        if new_piece == 'queen' or new_piece == 'Queen':
                            self.board[new_row][new_col] = Queen(new_row,
                                                                 new_col, 'w')
                            break
                        if new_piece == 'rook' or new_piece == 'Rook':
                            self.board[new_row][new_col] = Rook(new_row,
                                                                new_col, 'w')
                            break
                        if new_piece == 'bishop' or new_piece == 'Bishop':
                            self.board[new_row][new_col] = Bishop(new_row,
                                                                  new_col, 'w')
                            break
                        if new_piece == 'knight' or new_piece == 'Knight':
                            self.board[new_row][new_col] = Knight(new_row,
                                                                  new_col, 'w')
                            break
                        else:
                            print('That is an invalid piece. Try again.')
            if self.is_in_check('b') is True:
                if self.is_in_mate('b') is True:
                    self.state = 'WHITE_WON'
            else:
                if self.is_in_mate('b') is True:
                    self.state = 'DRAW'
        if self.turn == 'b':
            if self.is_in_check('b') is True:
                self.board[new_row][new_col] = taken_piece
                self.board[row][col] = piece
                piece.row = row
                piece.col = col
                return False
            if isinstance(piece, Pawn) is True:
                if new_row == 0 or new_row == 7:
                    while True:
                        new_piece = input(
                            'What piece would you like to promote to? ')
                        if new_piece == 'queen' or new_piece == 'Queen':
                            self.board[new_row][new_col] = Queen(new_row,
                                                                 new_col, 'b')
                            break
                        if new_piece == 'rook' or new_piece == 'Rook':
                            self.board[new_row][new_col] = Rook(new_row,
                                                                new_col, 'b')
                            break
                        if new_piece == 'bishop' or new_piece == 'Bishop':
                            self.board[new_row][new_col] = Bishop(new_row,
                                                                  new_col, 'b')
                            break
                        if new_piece == 'knight' or new_piece == 'Knight':
                            self.board[new_row][new_col] = Knight(new_row,
                                                                  new_col, 'b')
                            break
                        else:
                            print('That is an invalid piece. Try again.')
            if self.is_in_check('w') is True:
                if self.is_in_mate('w') is True:
                    self.state = 'BLACK_WON'
            else:
                if self.is_in_mate('w') is True:
                    self.state = 'DRAW'

        # Updates the turn tracker.
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'
        return True


a = Chess()
a.game_board.print_board()
print(a.move(6, 2, 4, 2))
a.game_board.print_board()
print(a.move(0, 4, 0, 5))
a.game_board.print_board()
print(a.move(4, 2, 3, 2))
a.game_board.print_board()
print(a.move(0, 5, 0, 6))
a.game_board.print_board()
print(a.move(3, 2, 2, 2))
a.game_board.print_board()
print(a.move(0, 6, 0, 7))
a.game_board.print_board()
print(a.move(2, 2, 1, 2))
a.game_board.print_board()
print(a.move(0, 7, 0, 6))
a.game_board.print_board()
print(a.move(1, 2, 0, 2))
a.game_board.print_board()
print(a.state)