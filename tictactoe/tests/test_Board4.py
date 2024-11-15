import unittest

from tictactoe.Board import Board


class BoardExecuteMoveTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_execute_move_valid_move(self):
        action = 0  # Top-left corner
        player = 1  # Player 1
        self.board.execute_move(player, action)
        self.assertEqual(self.board.pieces[0, 0], player)

    def test_execute_move_invalid_move(self):
        action = 0  # Top-left corner
        player1 = 1  # Player 1
        player2 = -1  # Player 2

        self.board.execute_move(player1, action)  # First move by Player 1
        self.assertEqual(self.board.pieces[0, 0], player1)

        with self.assertRaisesRegex(AssertionError, "Invalid move: Attempting to play in a non-empty square."):
            self.board.execute_move(player2, action)


    def test_execute_move_on_populated_board(self):
        player1 = 1  # Player 1
        player2 = -1  # Player 2
        actions = [0, 1, 4, 3]  # Various positions on the board

        self.board.execute_move(player1, actions[0])
        self.board.execute_move(player2, actions[1])
        self.board.execute_move(player1, actions[2])
        self.board.execute_move(player2, actions[3])

        self.assertEqual(self.board.pieces[0, 0], player1)
        self.assertEqual(self.board.pieces[0, 1], player2)
        self.assertEqual(self.board.pieces[1, 1], player1)
        self.assertEqual(self.board.pieces[1, 0], player2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
