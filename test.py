import unittest
from game import Chess


chess = Chess()
board = chess.board


class TestChessGame(unittest.TestCase):
    """Represents unit tests that check whether certain functionalities of the
    Chess class work.
    """
    def test_pawn(self):
        # Tests forward movement.
        piece = board[6][3]
        chess.move(6, 3, 5, 3)
        self.assertEqual(board[6][3], '_')
        self.assertEqual(board[5][3], piece)
        piece = board[1][4]
        chess.move(1, 4, 3, 4)
        self.assertEqual(board[1][4], '_')
        self.assertEqual(board[2][4], '_')
        self.assertEqual(board[3][4], piece)

        # Tests
        piece = board[5][3]
        self.assertEqual(chess.move(5, 3, 6, 3), False)
        self.assertEqual(chess.move(5, 3, 6, 2), False)
        self.assertEqual(chess.move(5, 3, 6, 2), False)
        chess.game_board.print_board()


if __name__ == '__main__':
    unittest.main()