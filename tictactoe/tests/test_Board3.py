import unittest

import numpy as np
from tictactoe.Board import Board


class TestBoardGetEncodedState(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_get_encoded_state_empty_board(self):
        self.board.pieces = np.zeros((3, 3))
        encoded_state = self.board.get_encoded_state()
        expected_state = np.stack([np.zeros((3, 3)), np.ones((3, 3)), np.zeros((3, 3))])
        np.testing.assert_array_equal(encoded_state, expected_state)

    def test_get_encoded_state_white_and_black_moves(self):
        self.board.pieces = np.array([
            [1, -1, 0],
            [0, 1, -1],
            [-1, 0, 0]
        ])
        encoded_state = self.board.get_encoded_state()
        expected_state = np.stack([
            np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),  # Black's -1 positions
            np.array([[0, 0, 1], [1, 0, 0], [0, 1, 1]]),  # Empty's 0 positions
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]]),  # White 1 positions with 1s
        ])
        np.testing.assert_array_equal(encoded_state, expected_state)

    def test_get_encoded_state_white_wins(self):
        self.board.pieces = np.array([
            [1, 1, 1],
            [0, -1, -1],
            [0, 0, 0]
        ])
        encoded_state = self.board.get_encoded_state()
        expected_state = np.stack([
            np.array([[0, 0, 0], [0, 1, 1], [0, 0, 0]]),  # Black's positions
            np.array([[0, 0, 0], [1, 0, 0], [1, 1, 1]]),  # Empty positions with 1s
            np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])  # White's positions
        ])
        np.testing.assert_array_equal(encoded_state, expected_state)

    def test_get_encoded_state_black_wins(self):
        self.board.pieces = np.array([
            [-1, -1, -1],
            [0, 1, 0],
            [0, 1, 0]
        ])
        encoded_state = self.board.get_encoded_state()
        expected_state = np.stack([
            np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]]),  # Black's positions
            np.array([[0, 0, 0], [1, 0, 1], [1, 0, 1]]),  # Empty positions with 1s
            np.array([[0, 0, 0], [0, 1, 0], [0, 1, 0]])  # White's positions
        ])
        np.testing.assert_array_equal(encoded_state, expected_state)


if __name__ == '__main__':
    unittest.main()
