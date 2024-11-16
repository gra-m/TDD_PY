from typing import Tuple

import numpy as np

BLACK_MIN_ONE = -1
EMPTY_ZERO = 0
WHITE_ONE = 1


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
        self._pieces =  self.__getpieces__()

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

    def __getpieces__(self, type_for_array = np.int8):
        value = np.zeros((self._num_rows, self._num_cols), dtype = type_for_array)
        return value


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
        return np.sum(self._pieces == EMPTY_ZERO) > 0

    def get_valid_moves(self):
        array_init_as_all_zeros = np.zeros(self.get_action_size(), dtype=np.uint8)

        for row in range(self.size):
            for column in range(self.size):
                if self._pieces[row, column] == 0:
                    array_init_as_all_zeros[row * self.size + column] = 1
        return array_init_as_all_zeros

    def is_win(self, player: int) -> bool:
        """Check whether the given player has collected a triplet in any direction on a rectangular board"""
        # not possible to have winner until 5 moves but board size can be changed
        # if np.sum(self.get_valid_moves() == 0) > 3:
         #   return False

        for i in range(self.size):
            if np.all(self._pieces[i, :] == player) or np.all(self._pieces[:, i] == player):
                return True

        if np.all(np.diag(self._pieces) == player) or np.all(np.diag(np.fliplr(self._pieces)) == player):
            return True

        return False

    def execute_move(self, player: int, action: int):
        """Perform the given action on the board"""
        try:
            assert self.get_valid_moves()[action] == WHITE_ONE, "Invalid move: Attempting to play in a non-empty square."
            three_d_move: tuple[int, int] = (action // self.size,  action % self.size)
            self.__setitem__(three_d_move, player)
        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise e  # Re-raise the exception after logging for test


    def __str__(self):
        board_str = []
        for x in range(self._num_rows):
            for y in range(self._num_cols):
                piece = self[x, y]
                if piece == WHITE_ONE:
                    board_str.append("X")
                elif piece == BLACK_MIN_ONE:
                    board_str.append("O")
                elif piece == EMPTY_ZERO:
                    board_str.append("-")
            board_str.append("\n")
        return "".join(board_str)

    def get_encoded_state(self):
        return_stack = np.stack([self.__create_encoded_state_for__(value) for value in [BLACK_MIN_ONE, EMPTY_ZERO, WHITE_ONE]])

        print(f"encoded state is ${return_stack}")
        return return_stack

    def __create_encoded_state_for__(self, value_to_find: int):
        # init pieces array as np.float32, this contains 0s by default
        pieces_mask = self.__getpieces__(np.float32)
        # set pieces where it equals value to find to the value in pieces (always 0) plus one
        pieces_mask [self._pieces == value_to_find] += 1
        return pieces_mask




    def get_player(self, action):
        row = action // self.size
        column = action % self.size
        return self[row, column]
