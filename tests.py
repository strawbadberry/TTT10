import unittest
from unittest.mock import patch
from logic import TicTacToe, Bot

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game_instance = TicTacToe()

    def test_initialization_empty_board(self):
        expected_board = [[None, None, None], [None, None, None], [None, None, None]]
        self.assertEqual(self.game_instance.get_empty_board(), expected_board, "The board should be initialized with all None")

    def test_player_switch(self):
        initial_player = self.game_instance.current_player
        self.game_instance.switch_player()
        self.assertNotEqual(self.game_instance.current_player, initial_player, "Switching players should change the current player")

    def test_no_winner_check(self):
        self.assertIsNone(self.game_instance.check_winner(), "No winner is expected for an empty board")

    def test_winner_check_row(self):
        self.game_instance.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(self.game_instance.check_winner(), 'X', "Player X should win with a complete row")

    def test_winner_check_column(self):
        self.game_instance.board = [['O', None, None], ['O', None, None], ['O', None, None]]
        self.assertEqual(self.game_instance.check_winner(), 'O', "Player O should win with a complete column")

    def test_winner_check_diagonal(self):
        self.game_instance.board = [['X', None, None], [None, 'X', None], [None, None, 'X']]
        self.assertEqual(self.game_instance.check_winner(), 'X', "Player X should win with a diagonal")

    def test_draw_check(self):
        self.game_instance.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(self.game_instance.check_winner(), 'draw', "The game should be a draw with no empty spaces and no winner")

class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot_instance = Bot()
        self.board_instance = [[None, None, None], [None, None, None], [None, None, None]]

    def test_bot_make_move(self):
        row, col = self.bot_instance.make_move(self.board_instance)
        self.assertIsNone(self.board_instance[row][col], "The bot should select an empty position")

if __name__ == '__main__':
    unittest.main()

