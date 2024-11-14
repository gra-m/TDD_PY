from typing import Tuple, Union

import numpy as np

EMPTY = 0
WHITE = 1
BLACK = -1


class Board:
    """
    Board class for the game of TicTacToe.
    The default board size is 3x3.
    Board data:
      1=white(O), -1=black(X), 0=empty
      first dim is row, second is column:
         pieces[0][0] is the top left square,
         pieces[2][0] is the bottom left square,
    Squares are stored and manipulated as (x,y) tuples.

    Based on the board for the game of TicTacToe by Evgeny Tyurin, github.com/evg-tyurin
    """
    def __init__(self, num_rows: int = 3, num_cols: int = 3):
        """Set up the initial board configuration"""
        self._num_rows = num_rows
        self._num_cols = num_cols
        # Create an empty board (numpy 2-dimensional array)
        self._pieces = np.zeros((self._num_rows, self._num_cols), dtype = np.int8)

    def get_board_size(self):
        return self._num_rows * self._num_cols

    def get_action_size(self):
        return self._num_rows * self._num_cols

    def create_new_board(self):
        return Board(self._num_rows, self._num_cols)

    def copy(self):
        """Create a deep copy of the board"""
        board = Board(self._num_rows, self._num_cols)
        board.pieces = np.copy(self.pieces)
        return board

    def __getitem__(self, index: Tuple[int, int]):
        row, column = index
        return self._pieces[row][column]

    def __setitem__(self, index, value):
        row, column = index
        self._pieces[row, column] = value

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        self._pieces = value

    @property
    def size(self):
        return self._num_cols

    def has_valid_moves(self) -> bool:
        return np.sum(self._pieces == EMPTY) > 0

    def get_valid_moves(self):
        array_init_as_nine_zeros = np.zeros(9, dtype=np.uint8)

        for row in range(3):
            for column in range(3):
                if self._pieces[row, column] == 0:
                    array_init_as_nine_zeros[row * 3 + column] = 1
        return array_init_as_nine_zeros

    def is_win(self, player: int) -> bool:
        """Check whether the given player has collected a triplet in any direction on a rectangular board"""
        # not possible to have winner until 5 moves but board size can be changed
        # if np.sum(self.get_valid_moves() == 0) > 3:
         #   return False

        for i in range(3):
            if (np.all(self._pieces[i, :] == player) or np.all(self._pieces[:, i] == player)):
                print("row/col WIN")
                return True

        if (np.all(np.diag(self._pieces) == player) or np.all(np.diag(np.fliplr(self._pieces))== player)):
            print("diagonal WIN")
            return True

        print("NO WIN")
        return False

    def execute_move(self, player: int, action: int):
        """Perform the given action on the board"""
        try:
            assert self.get_valid_moves()[action] == EMPTY, "Invalid move: Attempting to play in a non-empty square."
            three_d_move: tuple[int, int] = (action // 3, action % 3)
            self.__setitem__(three_d_move, player)
        except AssertionError as e:
            print(f"Assertion failed: {e}")


    def __str__(self):
        board_str = []
        for x in range(self._num_rows):
            for y in range(self._num_cols):
                piece = self[x, y]
                if piece == WHITE:
                    board_str.append("X")
                elif piece == BLACK:
                    board_str.append("O")
                elif piece == EMPTY:
                    board_str.append("-")
            board_str.append("\n")
        return "".join(board_str)

    def get_encoded_state(self):
        encoded_state = None # numpy stack of three masks
        return encoded_state

    def get_player(self, action):
        row = action // self.size
        column = action % self.size
        return self[row, column]
