import unittest
from File.txt_file import TXT_File
 
from Main.sudoku_game import SudokuGame

class Test_SudokuGame(unittest.TestCase):


    def setUp(self):
        self.path= "..\UnitTests"
        self.name="To_read_sudoku_easy.txt"
#        self.file=File(self.path,self.name)
        self.txtfile=TXT_File(self.path,self.name)
        self.dict_expected={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        self.game = SudokuGame()
        
        self.wrong_entry = "abcdef"        
        self.one_character = "1"
        self.fifty_characters = "74236815939657124858149236781475392697528643126314"
        self.expected_text_with_one_character = "100000000000000000000000000000000000000000000000000000000000000000000000000000000"
        self.expected_text_with_fifty_characters = "742368159396571248581492367814753926975286431263140000000000000000000000000000000"
        
        self.level="Easy"
    
    
    def test_resolve_a_sudoku_game_with_default_configuration_from_a_file(self):
        self.assertEqual(self.dict_expected, self.game.solve_sudoku_from_file(self.path, self.name))
    
    def test_modify_xml_value_for_algorithm_from_Norvig_to_Brute(self):
        expected_value = "Brute"
        self.assertEqual(expected_value, self.game.xml_config_file.set_xml_value("Brute","default_algorithm"))
    
    def test_resolve_a_sudoku_game_with_default_configuration_from_console(self):
        self.assertEqual(self.dict_expected, self.game.solve_sudoku_from_console({'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}))
        
    def test_if_wrong_entry_return_false_flag(self):
        flag = self.game.validate_text(self.wrong_entry)[1]
        self.assertFalse(flag)
        
    def test_if_numeric_entries_return_true_flag(self):
        flag = self.game.validate_text(self.fifty_characters)[1]
        self.assertTrue(flag)
        
       

    def test_get_xml_value_for_difficulty_level(self):
        self.assertEqual(self.level, self.game.get_xml_value("difficulty_level"))
       
    
    def test_set_xml_value_for_algorithm_from_Norvig_to_Brute(self):
        expected_value = "Brute"
        self.game.set_xml_value("Brute","default_algorithm")
        self.assertEqual(expected_value, self.game.get_xml_value("default_algorithm"))
        
    def tearDown(self):
        self.game.xml_config_file.set_xml_value("Norvig","default_algorithm")
    
if __name__ == "__main__":
    unittest.main()

