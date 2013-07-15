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
    
    
    def test_resolve_a_sudoku_game_with_default_configuration(self):
        self.assertEqual(self.dict_expected, self.game.solve_sudoku(self.path, self.name)[0])
    
    def test_modify_xml_value_for_algorithm_from_Norvig_to_Brute(self):
        expected_value = "Brute"
        self.assertEqual(expected_value, self.game.xml_config_file.set_xml_value("Brute","default_algorithm"))
        
    def tearDown(self):
        self.game.xml_config_file.set_xml_value("Norvig","default_algorithm")
    
if __name__ == "__main__":
    unittest.main()

