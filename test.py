import unittest
from game import Chess
from piece import Pawn, Rook, Knight, Bishop, Queen, King


chess = Chess()
board = chess.board


class TestChessClass(unittest.TestCase):
    """Tests for the Chess class."""
    def test_turn(self):
        """Tests the turn data member."""
        self.assertEqual(chess.turn, 'w')

    def test_state(self):
        """Tests the state data member."""
        self.assertEqual(chess.state, 'UNFINISHED')

    def test_turn_count(self):
        """Tests the turn_count data member."""
        self.assertEqual(chess.turn_count, 1)

    def test_is_in_check(self):
        """Tests the is_in_check method."""
        self.assertEqual(chess.is_in_check('w'), False)
        self.assertEqual(chess.is_in_check('b'), False)

    def test_is_in_mate(self):
        """Tests the is_in_mate method."""
        self.assertEqual(chess.is_in_mate('w'), False)
        self.assertEqual(chess.is_in_mate('b'), False)


class TestBoardClass(unittest.TestCase):
    """Tests for the Board class."""
    def test_board(self):
        """Tests the board data member."""
        for i in range(8):
            self.assertTrue(isinstance(chess.board[1][i], Pawn))
            self.assertTrue(isinstance(chess.board[6][i], Pawn))
        self.assertTrue(isinstance(chess.board[0][0], Rook))
        self.assertTrue(isinstance(chess.board[0][7], Rook))
        self.assertTrue(isinstance(chess.board[0][1], Knight))
        self.assertTrue(isinstance(chess.board[0][6], Knight))
        self.assertTrue(isinstance(chess.board[0][2], Bishop))
        self.assertTrue(isinstance(chess.board[0][5], Bishop))
        self.assertTrue(isinstance(chess.board[0][3], Queen))
        self.assertTrue(isinstance(chess.board[0][4], King))
        self.assertTrue(isinstance(chess.board[7][0], Rook))
        self.assertTrue(isinstance(chess.board[7][7], Rook))
        self.assertTrue(isinstance(chess.board[7][1], Knight))
        self.assertTrue(isinstance(chess.board[7][6], Knight))
        self.assertTrue(isinstance(chess.board[7][2], Bishop))
        self.assertTrue(isinstance(chess.board[7][5], Bishop))
        self.assertTrue(isinstance(chess.board[7][3], Queen))
        self.assertTrue(isinstance(chess.board[7][4], King))


class TestPieceClass(unittest.TestCase):
    """Tests for the Piece class."""
    def test_row(self):
        """Tests the row data member."""
        self.assertEqual(chess.board[7][0].row, 7)
        self.assertEqual(chess.board[0][2].row, 0)
        self.assertEqual(chess.board[1][3].row, 1)
        self.assertEqual(chess.board[6][5].row, 6)

    def test_col(self):
        """Tests the col data member."""
        self.assertEqual(chess.board[7][2].col, 2)
        self.assertEqual(chess.board[0][6].col, 6)
        self.assertEqual(chess.board[0][4].col, 4)
        self.assertEqual(chess.board[7][5].col, 5)

    def test_color(self):
        """Tests the color data member."""
        self.assertEqual(chess.board[0][4].color, 'b')
        self.assertEqual(chess.board[7][4].color, 'w')
        self.assertEqual(chess.board[1][4].color, 'b')
        self.assertEqual(chess.board[6][7].color, 'w')


if __name__ == '__main__':
    unittest.main()
