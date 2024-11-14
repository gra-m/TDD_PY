import unittest

import numpy as np

from tictactoe.Board import Board


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_win_no_winner(self):
        self.board.pieces = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertFalse(self.board.is_win(1))
        self.assertFalse(self.board.is_win(-1))

    def test_is_win_row_winner(self):
        self.board.pieces = np.array([[1, 1, 1], [-1, -1, 0], [1, 0, -1]])
        self.assertTrue(self.board.is_win(1))
        self.assertFalse(self.board.is_win(-1))

    def test_is_win_column_winner(self):
        self.board.pieces = np.array([[1, -1, 0], [1, -1, 0], [1, 0, -1]])
        self.assertTrue(self.board.is_win(1))
        self.assertFalse(self.board.is_win(-1))

    def test_is_win_diagonal_winner(self):
        self.board.pieces = np.array([[1, -1, 0], [0, 1, -1], [-1, 0, 1]])
        self.assertTrue(self.board.is_win(1))
        self.assertFalse(self.board.is_win(-1))

    def test_is_win_other_diagonal_winner(self):
        self.board.pieces = np.array([[-1, 0, 1], [0, 1, -1], [1, -1, 0]])
        self.assertTrue(self.board.is_win(1))
        self.assertFalse(self.board.is_win(-1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
