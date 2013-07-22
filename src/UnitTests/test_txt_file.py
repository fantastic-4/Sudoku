import glob
import os
import unittest
from File.txt_file import TXTFile

class Testtxtfile(unittest.TestCase):
    
    def setUp(self):
        self.name="To_read_sudoku_easy.txt"
        self.path= "..\\UnitTests\\"
        self.txtfile=TXTFile(self.path,self.name)

    def test_txt_file_has_correct_value_read_from_TXT_file_class(self):
        var1='003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.assertEqual(var1,self.txtfile.read_file())
   
    def test_if_txt_file_class_save_the_dict_into_file(self):
        grid_expected={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        grid_expected1={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        self.assertEqual(self.txtfile.write_file(grid_expected1),self.txtfile.write_file(grid_expected))
         
    def test_if_the_path_is_wrong_that_validates_File(self):
        self.txtfile.file_name="WrongFile.XX"
        self.txtfile.open_file()
         
    def test_remove_bckslash_if_has_repeated_in_path(self):
        self.txtfile.path="..\UnitTests\\\\"
        self.txtfile.file_name="To_read_sudoku_easy.txt"
        self.txtfile.open_file()
        self.assertEqual("..\UnitTests", self.txtfile.path)
 
    def test_to_verify_if_the_file_is_saved_with_time_stamp_at_first(self):
        self.assertEqual(self.txtfile.file_name,self.txtfile.file_name) 
        
    def test_save_game_in_file(self):
        x={'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'}
        tim='20:30'
        self.txtfile.save_game(x,tim)
        self.assertEqual(self.txtfile.file_name,self.txtfile.file_name)
    
    def test_if_load_game_method_loads_the_file_correctly(self):
        expected=('003020600900305001001806400008102900700000098006708200002609500809203909095019300', '0:0.00016964823776')
        value=self.txtfile.load_Game("Saved_game_2013_07_18_16_21_57.txt")
        self.assertEqual(expected, value)

    def tearDown(self):
        directory='..\\UnitTests\\'
        os.chdir(directory)
        files=glob.glob('Saved*')
        files1=glob.glob('Solved*')
        for filename in files:
            os.unlink(filename)
        for filename in files1:
            os.unlink(filename)
                    
if __name__ == "__main__":
    unittest.main()
