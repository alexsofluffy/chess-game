class Piece:
    """Represents a game piece."""

    def __init__(self, row, col, color):
        """Creates a new game piece.

        Keyword arguments:
        row -- the row on the game board that piece is located
        col -- the column on the game board that piece is located
        color -- the color of the piece (white or black)
        """
        self.row = row
        self.col = col
        self.color = color


class Pawn(Piece):
    """Represents a pawn piece."""

    def __init__(self, row, col, color):
        """Creates a new pawn piece, inherits properties from Piece class."""
        super().__init__(row, col, color)
        self.moved_2 = False
        self.en_passant = False
        self.turn_moved = None

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if self.color == 'w':
            if new_row >= self.row:
                return False
            if new_col == self.col:
                if self.row == 6:
                    if self.row - new_row > 2:
                        return False
                    if self.row - new_row == 2:
                        if board[self.row - 1][self.col] != '_':
                            return False
                        self.moved_2 = True
                if self.row < 6:
                    if self.row - new_row != 1:
                        return False
                if board[new_row][new_col] != '_':
                    return False
            else:
                if self.row - new_row != 1:
                    return False
                if new_col < self.col:
                    if self.col - new_col != 1:
                        return False
                    if self.row == 3 and \
                        board[new_row][new_col] == '_' and \
                        isinstance(board[self.row][self.col - 1], Pawn) \
                            is True:
                        self.en_passant = True
                        return True
                if new_col > self.col:
                    if new_col - self.col != 1:
                        return False
                    if self.row == 3 and \
                        board[new_row][new_col] == '_' and \
                        isinstance(board[self.row][self.col + 1], Pawn) \
                            is True:
                        self.en_passant = True
                        return True
                if board[new_row][new_col] == '_':
                    return False
        if self.color == 'b':
            if new_row <= self.row:
                return False
            if new_col == self.col:
                if self.row == 1:
                    if new_row - self.row > 2:
                        return False
                    if new_row - self.row == 2:
                        if board[new_row - 1][self.col] != '_':
                            return False
                        self.moved_2 = True
                if self.row > 1:
                    if new_row - self.row != 1:
                        return False
                if board[new_row][new_col] != '_':
                    return False
            else:
                if new_row - self.row != 1:
                    return False
                if new_col < self.col:
                    if self.col - new_col != 1:
                        return False
                    if self.row == 4 and \
                        board[new_row][new_col] == '_' and \
                        isinstance(board[self.row][self.col - 1], Pawn) \
                            is True:
                        self.en_passant = True
                        return True
                if new_col > self.col:
                    if new_col - self.col != 1:
                        return False
                    if self.row == 4 and \
                        board[new_row][new_col] == '_' and \
                        isinstance(board[self.row][self.col + 1], Pawn) \
                            is True:
                        self.en_passant = True
                        return True
                if board[new_row][new_col] == '_':
                    return False
        return True


class Rook(Piece):
    """Represents a rook piece."""

    def __init__(self, row, col, color):
        """Creates a new rook piece."""
        super().__init__(row, col, color)
        self.moved = False

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if new_row != self.row and new_col != self.col:
            return False
        else:
            if new_row == self.row:
                if new_col < self.col:
                    for col in range(new_col + 1, self.col):
                        if board[self.row][col] != '_':
                            return False
                if new_col > self.col:
                    for col in range(self.col + 1, new_col):
                        if board[self.row][col] != '_':
                            return False
            if new_col == self.col:
                if new_row < self.row:
                    for row in range(new_row + 1, self.row):
                        if board[row][self.col] != '_':
                            return False
                if new_row > self.row:
                    for row in range(self.row + 1, new_row):
                        if board[row][self.col] != '_':
                            return False
            return True


class Knight(Piece):
    """Represents a knight piece."""

    def __init__(self, row, col, color):
        """Creates a new knight piece."""
        super().__init__(row, col, color)

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if new_row == self.row or new_col == self.col:
            return False
        else:
            if new_row < self.row:
                if self.row - new_row > 2:
                    return False
                if new_col < self.col:
                    if self.row - new_row == 1:
                        if self.col - new_col != 2:
                            return False
                    if self.row - new_row == 2:
                        if self.col - new_col != 1:
                            return False
                if new_col > self.col:
                    if self.row - new_row == 1:
                        if new_col - self.col != 2:
                            return False
                    if self.row - new_row == 2:
                        if new_col - self.col != 1:
                            return False
            if new_row > self.row:
                if new_row - self.row > 2:
                    return False
                if new_col < self.col:
                    if new_row - self.row == 1:
                        if self.col - new_col != 2:
                            return False
                    if new_row - self.row == 2:
                        if self.col - new_col != 1:
                            return False
                if new_col > self.col:
                    if new_row - self.row == 1:
                        if new_col - self.col != 2:
                            return False
                    if new_row - self.row == 2:
                        if new_col - self.col != 1:
                            return False
            return True


class Bishop(Piece):
    """Represents a bishop piece."""

    def __init__(self, row, col, color):
        """Creates a new bishop piece."""
        super().__init__(row, col, color)

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if new_row == self.row or new_col == self.col:
            return False
        else:
            if new_row < self.row:
                if new_col < self.col:
                    if self.col - new_col != self.row - new_row:
                        return False
                    test_row = new_row + 1
                    test_col = new_col + 1
                    while test_row != self.row:
                        if board[test_row][test_col] != '_':
                            return False
                        else:
                            test_row += 1
                            test_col += 1
                if new_col > self.col:
                    if new_col - self.col != self.row - new_row:
                        return False
                    test_row = new_row + 1
                    test_col = new_col - 1
                    while test_row != self.row:
                        if board[test_row][test_col] != '_':
                            return False
                        else:
                            test_row += 1
                            test_col -= 1
            if new_row > self.row:
                if new_col < self.col:
                    if self.col - new_col != new_row - self.row:
                        return False
                    test_row = new_row - 1
                    test_col = new_col + 1
                    while test_row != self.row:
                        if board[test_row][test_col] != '_':
                            return False
                        else:
                            test_row -= 1
                            test_col += 1
                if new_col > self.col:
                    if new_col - self.col != new_row - self.row:
                        return False
                    test_row = new_row - 1
                    test_col = new_col - 1
                    while test_row != self.row:
                        if board[test_row][test_col] != '_':
                            return False
                        else:
                            test_row -= 1
                            test_col -= 1
            return True


class Queen(Piece):
    """Represents a queen piece."""

    def __init__(self, row, col, color):
        """Creates a new queen piece."""
        super().__init__(row, col, color)

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if new_row < self.row and new_col != self.col:
            if new_col < self.col:
                if self.col - new_col != self.row - new_row:
                    return False
                test_row = new_row + 1
                test_col = new_col + 1
                while test_row != self.row:
                    if board[test_row][test_col] != '_':
                        return False
                    else:
                        test_row += 1
                        test_col += 1
            if new_col > self.col:
                if new_col - self.col != self.row - new_row:
                    return False
                test_row = new_row + 1
                test_col = new_col - 1
                while test_row != self.row:
                    if board[test_row][test_col] != '_':
                        return False
                    else:
                        test_row += 1
                        test_col -= 1
        if new_row > self.row and new_col != self.col:
            if new_col < self.col:
                if self.col - new_col != new_row - self.row:
                    return False
                test_row = new_row - 1
                test_col = new_col + 1
                while test_row != self.row:
                    if board[test_row][test_col] != '_':
                        return False
                    else:
                        test_row -= 1
                        test_col += 1
            if new_col > self.col:
                if new_col - self.col != new_row - self.row:
                    return False
                test_row = new_row - 1
                test_col = new_col - 1
                while test_row != self.row:
                    if board[test_row][test_col] != '_':
                        return False
                    else:
                        test_row -= 1
                        test_col -= 1
        if new_row == self.row and new_col != self.col:
            if new_col < self.col:
                for col in range(new_col + 1, self.col):
                    if board[self.row][col] != '_':
                        return False
            if new_col > self.col:
                for col in range(self.col + 1, new_col):
                    if board[self.row][col] != '_':
                        return False
        if new_col == self.col and new_row != self.row:
            if new_row < self.row:
                for row in range(new_row + 1, self.row):
                    if board[row][self.col] != '_':
                        return False
            if new_row > self.row:
                for row in range(self.row + 1, new_row):
                    if board[row][self.col] != '_':
                        return False
        return True


class King(Piece):
    """Represents a king piece."""

    def __init__(self, row, col, color):
        """Creates a new king piece."""
        super().__init__(row, col, color)
        self.moved = False

    def is_move_valid(self, new_row, new_col, board):
        """Returns True if move is valid.

        Keyword arguments:
        new_row -- the row on the game board that piece is trying to move to
        new_col -- the column on the game board that piece is trying to move to
        board -- the game board that piece is currently on
        """
        if new_row == self.row and new_col == self.col:
            return False
        if new_row - self.row in range(-1, 2) and \
                new_col - self.col in range(-1, 2):
            return True
        if self.moved is False:
            if self.color == 'w':
                if new_row == 7 and new_col == 2:
                    rook = board[7][0]
                    if isinstance(rook, Rook) is True and rook.moved is False:
                        for i in range(1, 4):
                            if board[new_row][i] != '_':
                                return False
                        return True
                if new_row == 7 and new_col == 6:
                    rook = board[7][7]
                    if isinstance(rook, Rook) is True and rook.moved is False:
                        for i in range(5, 7):
                            if board[new_row][i] != '_':
                                return False
                        return True
            if self.color == 'b':
                if new_row == 0 and new_col == 2:
                    rook = board[0][0]
                    if isinstance(rook, Rook) is True and rook.moved is False:
                        for i in range(1, 4):
                            if board[new_row][i] != '_':
                                return False
                        return True
                if new_row == 0 and new_col == 6:
                    rook = board[0][7]
                    if isinstance(rook, Rook) is True and rook.moved is False:
                        for i in range(5, 7):
                            if board[new_row][i] != '_':
                                return False
                        return True
        return False
