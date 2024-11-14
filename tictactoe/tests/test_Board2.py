import unittest

import numpy as np

from tictactoe.Board import Board


class TestGetValidMovesFunction(unittest.TestCase):
    def setUp(self):
        self.board3x3 = Board(3, 3)

    def test_get_valid_moves_empty_board(self):
        expected_output = np.ones(9, dtype=np.uint8)
        np.testing.assert_array_equal(self.board3x3.get_valid_moves(), expected_output)

    def test_get_valid_moves_one_move_made(self):
        self.board3x3.pieces = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
        expected_output = np.array((0, 1, 1, 1, 1, 1, 1, 1, 1), dtype=np.uint8)
        np.testing.assert_array_equal(self.board3x3.get_valid_moves(), expected_output)

    def test_get_valid_moves_full_board(self):
        self.board3x3.pieces = np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]])
        expected_output = np.zeros(9, dtype=np.uint8)
        np.testing.assert_array_equal(self.board3x3.get_valid_moves(), expected_output)


    def tearDown(self):
        del self.board3x3


if __name__ == '__main__':
    unittest.main(verbosity=2)
