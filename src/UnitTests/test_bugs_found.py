import unittest
from Main.sudoku_game import SudokuGame

class TestBugFound(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()
        self.duplicate_number_entry = "1231"
        self.exit_option = "Q"
        self.strig_entry = "abc"
        
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
    