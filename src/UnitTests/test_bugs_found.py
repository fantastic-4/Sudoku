import unittest
from Main.sudoku_game import SudokuGame
from Main.play_sudoku import PlaySudoku

class TestBugFound(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()
        self.algorithm = "norvig"
        self.path = "c:\\sudoku\\save\\"
        self.command = "solve"
        self.expected_message_when_the_grid_cannot_be_solved = "Current grid cannot be solved."
        
        self.duplicate_number_entry = "1231"
        self.exit_option = "Q"
        self.strig_entry = "abc"
        self.wrong_string="0123456789"

    def test_verify_if_the_sudoku_game_allows_to_enter_duplicate_numbers_in_row(self):
        '''This test raise a flag when duplicating a number on row'''
        result = self.game.validate_text(self.duplicate_number_entry)[1]
        self.assertFalse(result)
        
    def test_verify_if_menu_py_fails_when_entering_the_Q_command(self):
        result = self.game.validate_text(self.exit_option)[1]
        self.assertFalse(result)
    
    def test_verify_if_the_sudoku_game_allows_to_enter_a_string(self):
        result = self.game.validate_text(self.strig_entry)[1]
        self.assertFalse(result)
        
    def test_verify_if_menu_py_fails_when_entering_0123456789_and_executing_solve_command(self):
        dictionary = self.game.validate_text(self.wrong_string)[0]
        play = PlaySudoku(self.game, dictionary, self.algorithm, self.path)
        result = play.play(self.command)
        self.assertEqual(self.expected_message_when_the_grid_cannot_be_solved,result)