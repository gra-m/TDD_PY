from cmath import isclose

from Board import Board
from TicTacToe import TicTacToe

class Round:
    def __init__(self, instance_of_game):
        self.instance_of_game = instance_of_game
        self.player = 1

    def print_game_layout(self):
        print(self.instance_of_game.get_board())
        one_valid_zero_invalid = self.instance_of_game.get_valid_moves()
        only_valid_positions = [ index for index,value in enumerate(one_valid_zero_invalid)if value == 1]
        print(f"valid_moves {only_valid_positions}")
        print(f"{self.player}:", end='')

    def play_game(self, action):
        if self.__is_invalid_move__(action):
            return True
        self.__update_board_with_move__(action)
        return self.__has_game_ended__(self.instance_of_game.get_game_ended(self.instance_of_game.get_board(), self.player))

    def __is_invalid_move__(self, action):
        valid_moves = self.instance_of_game.get_valid_moves()
        if valid_moves[action] == 0:
            print("action not valid")
            return True
        return False

    def __update_board_with_move__(self, action):
        self.instance_of_game._board = self.instance_of_game.get_next_state(self.instance_of_game.get_board(), self.player, action)

    def __has_game_ended__(self, answer):
        if isclose(answer, 1, rel_tol=1e-9) | isclose(answer, -1, rel_tol=1e-9):
            print(self.instance_of_game.get_board())
            print(f"{answer} won")
            return False
        if isclose(answer, 0.0001, rel_tol=1e-9):
            print(self.instance_of_game.get_board())
            print("draw")
            return False
        self.player = self.instance_of_game.get_opponent(self.player)
        return True

def main():
    first_round = Round(TicTacToe(Board()))
    is_playing = True
    while is_playing:
        first_round.print_game_layout()
        choose = int(input())
        is_playing = first_round.play_game(choose)

if __name__ == '__main__':
    main()
