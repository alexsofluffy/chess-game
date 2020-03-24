from piece import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    """Represents a chess game board."""
    def __init__(self):
        """Creates a new game board and initializes the starting locations of
        the game pieces.
        """

        # A chess board consists of 8 rows by 8 columns. The rows are known as
        # "ranks" and the columns are known as "files"."""
        self.board = [['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_', '_']]

        # The pieces are labeled by the first letter in their name on the
        # board. For example, 'K' and 'k' represent the king pieces for black
        # and white respectively. The only exception to this rule are 'N' and
        # 'n', which represent the knight pieces. White pieces start on the
        # bottom of the board (rank 8) and black pieces start on the top of the
        # board (rank 1) by default.
        self.board[1][0] = Pawn(1, 0, 'b')
        self.board[1][1] = Pawn(1, 1, 'b')
        self.board[1][2] = Pawn(1, 2, 'b')
        self.board[1][3] = Pawn(1, 3, 'b')
        self.board[1][4] = Pawn(1, 4, 'b')
        self.board[1][5] = Pawn(1, 5, 'b')
        self.board[1][6] = Pawn(1, 6, 'b')
        self.board[1][7] = Pawn(1, 7, 'b')
        self.board[0][0] = Rook(0, 0, 'b')
        self.board[0][7] = Rook(0, 7, 'b')
        self.board[0][1] = Knight(0, 1, 'b')
        self.board[0][6] = Knight(0, 6, 'b')
        self.board[0][2] = Bishop(0, 2, 'b')
        self.board[0][5] = Bishop(0, 5, 'b')
        self.board[0][3] = Queen(0, 3, 'b')
        self.board[0][4] = King(0, 4, 'b')

        """
        self.board[6][0] = Pawn(6, 0, 'w')
        self.board[6][1] = Pawn(6, 1, 'w')
        self.board[6][2] = Pawn(6, 2, 'w')
        self.board[6][3] = Pawn(6, 3, 'w')
        self.board[6][4] = Pawn(6, 4, 'w')
        self.board[6][5] = Pawn(6, 5, 'w')
        self.board[6][6] = Pawn(6, 6, 'w')
        """
        self.board[6][7] = Pawn(6, 7, 'w')
        self.board[7][0] = Rook(7, 0, 'w')
        self.board[7][7] = Rook(7, 7, 'w')
        """
        self.board[7][1] = Knight(7, 1, 'w')
        self.board[7][6] = Knight(7, 6, 'w')
        self.board[7][2] = Bishop(7, 2, 'w')
        self.board[7][5] = Bishop(7, 5, 'w')
        self.board[7][3] = Queen(7, 3, 'w')
        """
        self.board[7][4] = King(7, 4, 'w')

    def print_board(self):
        """Prints out the game board."""
        file_labels = '    ' + '0' + '    ' + '1' + '    ' + '2' + '    ' + \
                      '3' + '    ' + '4' + '    ' + '5' + '    ' + '6' + \
                      '    ' + '7'
        rank_label = 0
        # Prints file labels above board.
        print(file_labels)
        # Prints rank label before/after each rank.
        for rank in self.board:
            print(rank_label, end='')
            for square in rank:
                # Prints appropriate labels representing each game piece.
                if square == '_':
                    print('   ' + '_' + ' ', end='')
                else:
                    if isinstance(square, Pawn) is True:
                        if square.color == 'b':
                            print('   ' + 'P' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'p' + ' ', end='')
                    if isinstance(square, Rook) is True:
                        if square.color == 'b':
                            print('   ' + 'R' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'r' + ' ', end='')
                    if isinstance(square, Knight) is True:
                        if square.color == 'b':
                            print('   ' + 'N' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'n' + ' ', end='')
                    if isinstance(square, Bishop) is True:
                        if square.color == 'b':
                            print('   ' + 'B' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'b' + ' ', end='')
                    if isinstance(square, Queen) is True:
                        if square.color == 'b':
                            print('   ' + 'Q' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'q' + ' ', end='')
                    if isinstance(square, King) is True:
                        if square.color == 'b':
                            print('   ' + 'K' + ' ', end='')
                        if square.color == 'w':
                            print('   ' + 'k' + ' ', end='')
            print(rank_label)
            rank_label += 1
        # Prints file labels below board.
        print(file_labels)
