import math
from abc import ABC

from tictactoe.GameInterface import Game


class TicTacToe(Game, ABC):
    def __init__(self, board):
        self._board = board

    def get_board(self):
        return self._board

    def get_next_state(self, board, player, action):
        board.execute_move(player, action)
        return board

    def get_valid_moves(self):
        return self._board.get_valid_moves()

    def get_game_ended(self, board, player):
        # Return 1 if passed player has won
        if board.is_win(player):
            return 1
        # -1 if passed player has lost,
        if board.is_win(-player):
            return -1
        # 0 if no-one has won but there is still a game to be had
        if board.has_valid_moves():
            return 0
        # if game board is full
        return 1e-4

    def get_canonical_form(self, player):
        # return state if player==1, else return -state if player==-1
        return player * self._board

    def get_opponent(self, player):
        # Return the opponent player
        return -player

    def get_opponent_value(self, value):
        return value if math.isclose(value, 1e-4) else -value

    def change_perspective(self, board, player):
        # Change 1 to -1 and vice versa for -1 player and save it in changed_board
        if player == 1:
            return board
        board_changed = board.copy()
        board_changed._pieces = -board_changed._pieces
        return board_changed
