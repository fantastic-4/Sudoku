import unittest
import os
import time

from Main.play_sudoku import PlaySudoku
from Main.sudoku_game import SudokuGame

class TestPlaySudoku(unittest.TestCase):

    def setUp(self):
        
        self.game = SudokuGame()
        self.algorithm = "norvig"
        
        self.dictA = {"I6": "0", "H9": "9", "I2": "0", "E8": "0", "H3": "0", "H7": "0", "I7": "3", "I4": "0", "H5": "0", "F9": "0", "G7": "5", "G6": "9", "G5": "0", "E1": "7", "G3": "2", "G2": "0", "G1": "0", "I1": "0", "C8": "0", "I3": "5", "E5": "0", "I5": "1", "C9": "0", "G9": "0", "G8": "0", "A1": "0", "A3": "3", "A2": "0", "A5": "2", "A4": "0", "A7": "6", "A6": "0", "C3": "1", "C2": "0", "C1": "0", "E6": "0", "C7": "4", "C6": "6", "C5": "0", "C4": "8", "I9": "0", "D8": "0", "I8": "0", "E4": "0", "D9": "0", "H8": "0", "F6": "8", "A9": "0", "G4": "6", "A8": "0", "E7": "0", "E3": "0", "F1": "0", "F2": "0", "F3": "6", "F4": "7", "F5": "0", "E2": "0", "F7": "2", "F8": "0", "D2": "0", "H1": "8", "H6": "3", "H2": "0", "H4": "2", "D3": "8", "B4": "3", "B5": "0", "B6": "5", "B7": "0", "E9": "8", "B1": "9", "B2": "0", "B3": "0", "D6": "2", "D7": "9", "D4": "1", "D5": "0", "B8": "0", "B9": "1", "D1": "0"}
        self.expected_dictA = {"I6": "2", "H9": "9", "I2": "0", "E8": "0", "H3": "0", "H7": "0", "I7": "3", "I4": "0", "H5": "0", "F9": "0", "G7": "5", "G6": "9", "G5": "0", "E1": "7", "G3": "2", "G2": "0", "G1": "0", "I1": "0", "C8": "0", "I3": "5", "E5": "0", "I5": "1", "C9": "0", "G9": "0", "G8": "0", "A1": "0", "A3": "3", "A2": "0", "A5": "2", "A4": "0", "A7": "6", "A6": "0", "C3": "1", "C2": "0", "C1": "0", "E6": "0", "C7": "4", "C6": "6", "C5": "0", "C4": "8", "I9": "0", "D8": "0", "I8": "0", "E4": "0", "D9": "0", "H8": "0", "F6": "8", "A9": "0", "G4": "6", "A8": "0", "E7": "0", "E3": "0", "F1": "0", "F2": "0", "F3": "6", "F4": "7", "F5": "0", "E2": "0", "F7": "2", "F8": "0", "D2": "0", "H1": "8", "H6": "3", "H2": "0", "H4": "2", "D3": "8", "B4": "3", "B5": "0", "B6": "5", "B7": "0", "E9": "8", "B1": "9", "B2": "0", "B3": "0", "D6": "2", "D7": "9", "D4": "1", "D5": "0", "B8": "0", "B9": "1", "D1": "0"}
        self.dict_complete = {"B8": "2", "H1": "8", "C7": "4", "B3": "7", "D3": "8", "G9": "4", "G8": "1", "B9": "1", "A3": "3", "G7": "5", "G6": "9", "G5": "8", "G4": "6", "G3": "2", "G2": "7", "G1": "3", "B5": "4", "I1": "6", "I3": "5", "I2": "9", "I5": "1", "I4": "4", "I7": "3", "I6": "7", "A1": "4", "C9": "3", "C8": "9", "A5": "2", "E8": "3", "A7": "6", "A6": "1", "E5": "6", "C2": "5", "C1": "2", "E6": "4", "E1": "7", "A2": "8", "C5": "7", "A4": "9", "I9": "2", "B2": "6", "I8": "8", "H2": "1", "D9": "6", "F2": "3", "D5": "3", "C3": "1", "A9": "7", "C6": "6", "E4": "5", "B1": "9", "E7": "1", "F1": "1", "H8": "6", "H9": "9", "F4": "7", "F5": "9", "F6": "8", "F7": "2", "F8": "4", "H3": "4", "F3": "6", "H6": "3", "H7": "7", "H4": "2", "H5": "5", "B4": "3", "A8": "5", "B6": "5", "B7": "8", "E9": "8", "E3": "9", "D8": "7", "F9": "5", "D6": "2", "D7": "9", "D4": "1", "C4": "8", "D2": "4", "E2": "2", "D1": "5"}
        self.dictB = {"I6": "0", "H9": "0", "I2": "0", "E8": "5", "H3": "0", "H7": "0", "I7": "0", "I4": "7", "H5": "3", "F9": "0", "G7": "0", "G6": "0", "G5": "0", "E1": "6", "G3": "1", "G2": "4", "G1": "0", "I1": "0", "C8": "0", "I3": "8", "E5": "0", "I5": "0", "C9": "0", "G9": "0", "G8": "0", "A1": "5", "A3": "0", "A2": "2", "A5": "0", "A4": "0", "A7": "0", "A6": "6", "C3": "0", "C2": "0", "C1": "3", "E6": "0", "C7": "0", "C6": "0", "C5": "0", "C4": "0", "I9": "0", "D8": "0", "I8": "0", "E4": "0", "D9": "0", "H8": "2", "F6": "0", "A9": "0", "G4": "8", "A8": "0", "E7": "0", "E3": "0", "F1": "0", "F2": "0", "F3": "0", "F4": "0", "F5": "0", "E2": "0", "F7": "0", "F8": "0", "D2": "0", "H1": "0", "H6": "0", "H2": "0", "H4": "0", "D3": "0", "B4": "0", "B5": "0", "B6": "0", "B7": "7", "E9": "0", "B1": "0", "B2": "0", "B3": "0", "D6": "0", "D7": "8", "D4": "4", "D5": "0", "B8": "0", "B9": "1", "D1": "0"}
        
        self.wrong_dict = {"I6": "9", "H9": "9", "I2": "9", "E8": "9", "H3": "9", "H7": "9", "I7": "3", "I4": "0", "H5": "0", "F9": "0", "G7": "5", "G6": "9", "G5": "0", "E1": "7", "G3": "2", "G2": "0", "G1": "0", "I1": "0", "C8": "0", "I3": "5", "E5": "0", "I5": "1", "C9": "0", "G9": "0", "G8": "0", "A1": "0", "A3": "3", "A2": "0", "A5": "2", "A4": "0", "A7": "6", "A6": "0", "C3": "1", "C2": "0", "C1": "0", "E6": "0", "C7": "4", "C6": "6", "C5": "0", "C4": "8", "I9": "0", "D8": "0", "I8": "0", "E4": "0", "D9": "0", "H8": "0", "F6": "8", "A9": "0", "G4": "6", "A8": "0", "E7": "0", "E3": "0", "F1": "0", "F2": "0", "F3": "6", "F4": "7", "F5": "0", "E2": "0", "F7": "2", "F8": "0", "D2": "0", "H1": "8", "H6": "3", "H2": "0", "H4": "2", "D3": "8", "B4": "3", "B5": "0", "B6": "5", "B7": "0", "E9": "8", "B1": "9", "B2": "0", "B3": "0", "D6": "2", "D7": "9", "D4": "1", "D5": "0", "B8": "0", "B9": "1", "D1": "0"}
        self.move_to_play = "I6:2"
        self.expected_dictA = {"I6": "2", "H9": "9", "I2": "0", "E8": "0", "H3": "0", "H7": "0", "I7": "3", "I4": "0", "H5": "0", "F9": "0", "G7": "5", "G6": "9", "G5": "0", "E1": "7", "G3": "2", "G2": "0", "G1": "0", "I1": "0", "C8": "0", "I3": "5", "E5": "0", "I5": "1", "C9": "0", "G9": "0", "G8": "0", "A1": "0", "A3": "3", "A2": "0", "A5": "2", "A4": "0", "A7": "6", "A6": "0", "C3": "1", "C2": "0", "C1": "0", "E6": "0", "C7": "4", "C6": "6", "C5": "0", "C4": "8", "I9": "0", "D8": "0", "I8": "0", "E4": "0", "D9": "0", "H8": "0", "F6": "8", "A9": "0", "G4": "6", "A8": "0", "E7": "0", "E3": "0", "F1": "0", "F2": "0", "F3": "6", "F4": "7", "F5": "0", "E2": "0", "F7": "2", "F8": "0", "D2": "0", "H1": "8", "H6": "3", "H2": "0", "H4": "2", "D3": "8", "B4": "3", "B5": "0", "B6": "5", "B7": "0", "E9": "8", "B1": "9", "B2": "0", "B3": "0", "D6": "2", "D7": "9", "D4": "1", "D5": "0", "B8": "0", "B9": "1", "D1": "0"}
        
        self.specific_hint_command = "I6:HiNt"
        self.expected_specific_hint_message = "Hint: I6:7"
        self.hint_command = "HiNt"
        self.expected_hint_message = "Hint: H9:8"
        
        self.verify_command = "VeRiFy"
        self.expected_verify_message = "Congratulations, You solved the Grid!!"
        self.expected_wrong_verify_message = "ERROR, The grid is not fulfilled as expected."
        
        self.wrong_move_to_play = "Z6:20"
        self.expected_wrong_coordinate_message = "ERROR, Wrong Square"
        
        self.solve_command = "SoLvE"
        self.expected_solve_message = "The grid was solved"
        self.expected_wrong_solve_message = "Current grid cannot be solved."
        
        self.time_command = "TiMe"
        self.time_elapsed = "1:30"
        self.time_playing = 3
        
        self.save_command = "SavE"
        self.path = "c:\\sudoku\\save\\"
        
        self.reset_command = "ReSeT"
        
        self.undo_command = "UnDo"
        self.last_good_square_command = "ReTuRn"
        
    def test_if_a_number_can_be_set_as_move_played(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        ps.play(self.move_to_play)
        self.assertDictEqual(ps.dictionary,self.expected_dictA)
           
    def test_if_a_wrong_move_returns_false(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        self.assertTrue(ps.play(self.wrong_move_to_play), self.expected_wrong_coordinate_message)
           
    def test_if_specific_hint_is_displayed(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        m = ps.play(self.specific_hint_command)
        self.assertEquals(m,self.expected_specific_hint_message)
           
    def test_if_verify_command_validates_current_grid(self):
        ps = PlaySudoku(self.game, self.dict_complete, self.algorithm, self.path)
        m = ps.play(self.verify_command)
        self.assertEquals(m,self.expected_verify_message)
           
    def test_if_verify_command_validates_wrong_current_grid(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        m = ps.play(self.verify_command)
        self.assertEquals(m,self.expected_wrong_verify_message)
       
    def test_if_current_grid_can_be_solved(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        m = ps.play(self.solve_command)
        self.assertEquals(m,self.expected_solve_message)
           
    def test_if_current_grid_cannot_be_solved(self):
        ps = PlaySudoku(self.game, self.wrong_dict, self.algorithm, self.path)
        m = ps.play(self.solve_command)
        self.assertEquals(m,self.expected_wrong_solve_message)
           
    def test_if_time_elapsed_can_be_retrieved(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        time.sleep(1)
        m = ps.get_time()
        m = m.split(":")
        time_in_seconds = (float(m[0])*60) + (float(m[1]))
        self.assertTrue(time_in_seconds > 0)
           
    def test_if_time_elapsed_can_be_retrieved_after_load_previous_time(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        ps.set_elapsed_time(self.time_elapsed)
        m = ps.get_time()
        m = m.split(":")
        time_in_seconds = (float(m[0])*60) + float(m[1])
        self.assertTrue(time_in_seconds > 90)
           
    def test_if_current_grid_can_be_saved(self):
        ps = PlaySudoku(self.game, self.wrong_dict, self.algorithm, self.path)
        first_files = os.listdir(self.path)
        files_saved = len([name for name in os.listdir(self.path) if os.path.isfile(self.path+name)])
        ps.play(self.save_command)
        current_files = os.listdir(self.path)
        new_files_saved = len([name for name in os.listdir(self.path) if os.path.isfile(self.path+name)])
        self.assertTrue((files_saved + 1) == new_files_saved)
        for f in current_files:
            if not f in first_files: os.remove(self.path + f)
          
    def test_if_hint_is_displayed(self):
        ps = PlaySudoku(self.game, self.dictB, self.algorithm, self.path)
        self.assertTrue(ps.play(self.hint_command),self.expected_hint_message)
          
    def test_if_reset_command_restart_the_grid(self):
        ps = PlaySudoku(self.game, self.dictB, self.algorithm, self.path)
        ps.play(self.move_to_play)
        ps.play(self.reset_command)
        self.assertTrue(ps.dictionary,self.dictB)
         
    def test_if_reset_command_restart_the_time(self):
        ps = PlaySudoku(self.game, self.dictB, self.algorithm, self.path)
        ps.play(self.move_to_play)
        time.sleep(self.time_playing)
        ps.play(self.reset_command)
        m = ps.get_time()
        m = m.split(":")
        time_in_seconds = (float(m[0])*60) + float(m[1])
        self.assertTrue(time_in_seconds < self.time_playing)
        
    def test_if_undo_remove_last_move_played(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        ps.play(self.move_to_play)
        ps.play(self.undo_command)
        self.assertDictEqual(ps.dictionary,self.dictA)
        
    def test_if_game_can_be_returned_to_last_good_state(self):
        ps = PlaySudoku(self.game, self.dictA, self.algorithm, self.path)
        ps.play(self.move_to_play)
        ps.play("I2:9")
        ps.play("I8:9")
        ps.play(self.last_good_square_command)
        self.assertDictEqual(self.dictA,ps.dictionary)
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()